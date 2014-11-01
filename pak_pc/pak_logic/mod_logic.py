# -*- coding: utf8 -*-

"""
Главный класс общей логики.
"""

import sys


class ClsLogic(object):
    """
    Класс логики, который связывает по действиям все классы.
    """

    def __init__(self, root=None):
        """
        Общая инициализация класса определение переменных.
        :param root: ссылка на корневой класс.
        """
        self.root = root
        # локальная переменная для регистра программного счётчика
        self.reg_pc_old = 0
        # значение регистра программного счётчика
        self.reg_pc_val = 0
        # признаки запущенности ЦП в debug mode
        self.debug = 0
        # признак активности регистра bp
        self.reg_bp_act = None
        # ссылка на ЦП
        self.cpu = None
        # ссылка на графический интерфейс
        self.gui = None
        # ссылка на экран виртуальной машины
        self.win_screen = None
        # ссылка на класс ресурсов
        self.res = None
        # ссылка на видеокарту
        self.video = None
        # ссылка на языковые ресурсы
        self.lang = None
        # ссылка на регистр bp, признак akt
        self.reg_pc_act = None
        # ссылка на регистр bp и его адрес прерывания
        self.reg_pc_adr_break = None
        # ссылка на регистр bp и его адрес обработки
        self.reg_pc_adr_proc = None

    def set_res_str(self):
        """
        Присваивает строковые ресурсы графическому интерфейсу.
        Процедура сделана с целью отвязки GUI от ресурсов
        (повышение атомарности класса).
        """
        win_main = self.gui.win_main
        win_main.btnStep['text'] = self.lang['win_main_btn_step']
        win_main.btnDebug['text'] = self.lang['win_main_btn_debug_0']
        win_main.btnExit['text'] = self.lang['win_main_btn_exit_name']
        win_main.btnShowScreen['text'] = self.lang[
            'win_main_btn_show_screen_show']
        win_main.btnReset['text'] = self.lang['win_main_btn_reset']
        win_main.mbtFile['text'] = self.lang['win_main_mbt_file_name']
        win_main.mbtEdit['text'] = self.lang['win_main_mbt_edit_name']
        win_main.mbtCustom['text'] = self.lang['win_main_mbt_custom_name']
        win_main.frm_cpu.frm_cpu_freq.lblKey['text'] = self.lang[
            'win_main_frm_cpu_freq_lbl_key']

    def reset_pc(self):
        """
        Сброс состояния виртуального компьютера.
        """
        info = {'com': 'reset'}
        self.cpu.qcom.put(info)

    def update_speed(self, dtime=0):
        """
        При отладке обновляет периодически монитор состояния ЦП и скорость
        виртуальной машины.
        :type self: object
        :param dtime: производит замер по времени между циклами исполнения
        блока команд ЦП.
        """
        freq_cpu = 1.0 / dtime * self.cpu.time_code
        # print dtime, self.cpu.frec
        res = freq_cpu / self.cpu.frec
        if res > 1.1 or res < 0.9:
            if freq_cpu > self.cpu.frec:
                self.cpu.frec += int(freq_cpu / 100)
            elif freq_cpu < self.cpu.frec:
                self.cpu.frec -= int(freq_cpu / 100)
            if freq_cpu > 1000:
                freq_cpu = str(int(self.cpu.frec / 1000)) + ' kHz'
            else:
                freq_cpu = str(int(self.cpu.frec)) + ' Hz'
            frec = self.gui.win_main.frm_cpu.frmCpuFrec
            frec.entVal.delete(0, 'end')
            frec.entVal.insert(0, freq_cpu)
            # self.gui.win_main.update()

    def win_edit_bp_hide(self):
        """
        Вызывается при скрытии окна редактирования свойств регистра
        программного прерывания.
        """
        print '  ClsLogic.win_edit_bp_hide()'
        # --- обновить содержимое реального регистра программных прерываний ----
        self.reg_pc_act = self.gui.winEditBP.Act.get()
        self.reg_pc_adr_break = int(self.gui.winEditBP.entAdrBreakVal.get())
        self.reg_pc_adr_proc = int(self.gui.winEditBP.entAdrProcVal.get())

        info = {'reg_pc': {'act': self.reg_pc_act,
                           'adr_break': self.reg_pc_adr_break,
                           'adr_proc': self.reg_pc_adr_proc}}
        self.cpu.qcom.put(info)

        # print 'act=', self.cpu.reg_pc.get_act()
        #self.update_monitor()

    def show_win_edit_bp(self):
        # print 'ClsLogic.show_win_edit_bp()'
        """
        Вызывается при показе окна редактирования свойств регистра
        программного прерывания.
        """
        self.gui.winEditBP.show()

    def debug_cpu(self):
        # print 'ClsLogic.debug_cpu()'
        """
        Вызывается при запуске ЦП в режиме отладки.
        """
        if self.debug == 0:
            self.debug = 1
            self.gui.win_main.btnDebug['text'] = self.res.winMain_btnDebug_1
            info = {'com': 'debug(on)'}
        else:
            self.debug = 0
            self.gui.win_main.btnDebug['text'] = self.res.winMain_btnDebug_0
            info = {'com': 'debug(off)'}
        self.cpu.qcom.put(info)

    def step_cpu(self):
        """
        Метод исполняет шаг процессора с выводом результата.
        Команды отправляются в очередь между процессами.
        """
        # print 'ClsLogic.step_cpu()'
        # self.pre_update_monitor()
        info = {'com': 'step()'}
        self.cpu.qcom.put(info)
        #self.post_update_monitor()

    def update_monitor(self):
        """
        Обновляет монитор ЦП через равные промежутки времени.
        Информацию для обновления берёт от двух дочерних процессов:
        1. ЦП.
        2. Видеокарта.
        """
        while not self.cpu.qinfo.empty():
            info = self.cpu.qinfo.get()
            if 'reg_a' in info:
                inf = info['reg_a']
                # print 'detect reg_a', inf
                reg_a = self.gui.win_main.frm_cpu.frm_reg_a
                # print 'have key "reg_a.val"!', info['reg_a.val']
                reg_a.lbl_val['text'] = inf['val']
                #print "have key \"reg_a.FlagZ\"!", info['reg_a.FlagZ']
                reg_a.lblValZ['text'] = inf['FlagZ']
                #print 'have key "reg_a.FlagO"!', info['reg_a.FlagO']
                reg_a.lblValO['text'] = inf['FlagO']
                #print 'have key "reg_a.FlagC"!', info['reg_a.FlagC']
                reg_a.lblValC['text'] = inf['FlagO']
            if 'reg_pc' in info:
                inf = info['reg_pc']
                # print 'detect reg_pc', inf
                # print 'have key "reg_pc.val"!', info['reg_pc.val']
                self.reg_pc_val = inf['val']
                self.gui.win_main.frm_cpu.frm_reg_pc.lbl_val[
                    'text'] = self.reg_pc_old
                self.reg_pc_old = self.reg_pc_val
            # ---------------------------
            if 'reg_bp' in info:
                inf = info['reg_bp']
                reg_bp = self.gui.win_main.frm_cpu.frm_reg_bp
                # print 'have key "reg_bp.act"!', info['reg_bp.act']
                reg_bp.lbl_act_val['text'] = inf['act']
                #print 'have key "reg_bp.adr_proc"!', info['reg_bp.adr_proc']
                reg_bp.lblProcVal['text'] = inf['adr_proc']
                #print 'have key "reg_pc.adr_break"!', info['reg_pc.adr_break']
                reg_bp.lblBreakVal['text'] = inf['adr_break']
            # ---------------------------
            if 'reg_sp' in info:
                inf = info['reg_sp']
                reg_sp = self.gui.win_main.frm_cpu.frm_reg_sp
                reg_sp.lblAdrVal['text'] = inf['adr']
                reg_sp.lblValVal['text'] = inf['val']
            #---------------------------
            if 'debug' in info:
                inf = info['debug']
                #print 'detect DEBUG', inf
            #---------------------------
            if 'dtime' in info:
                inf = info['dtime']
                #print 'detect dtime', inf
                self.update_speed(dtime=inf)
        while not self.video.vout.empty():
            vout = self.video.vout.get()
            self.win_screen.lblScreen['text'] = vout

    def generate_new_disk(self):
        # print 'generate_new_disk()'
        """
        Создаёт новый диск.
        """
        self.gui.winCreateDisk.destroy()
        disk_size = int(self.gui.winCreateDisk.fkvSize.get_val())
        disk_name = self.gui.winCreateDisk.fkvName.get_val()
        str_ = '0' * (2 ** 10)
        file_disk = open('./data/' + disk_name + '.dsk', 'wb')
        for i in xrange(0, disk_size):
            file_disk.write(str_)
            file_disk.close()

    def create_new_disk(self):
        # TODO: дописать процедуру создания нового диска
        """
        Вызывается при создании нового диска.
        """
        pass

    def create_disk(self):
        """
        Вызывается при создании виртуального диска.
        """
        print 'ClsLogic.create_disk()'
        self.gui.winCreateDisk.show()

    def show_screen(self):
        """
        Вызывается при показе экрана виртуальной машины.
        """
        if not self.gui.win_screen.winScreen_show:
            self.gui.win_screen.show()
        else:
            self.gui.win_screen.destroy()

    def run(self):
        """
        Вызывается при запуске всей системы.

        """
        self.cpu = self.root.cpu
        self.gui = self.root.gui
        self.win_screen = self.gui.win_screen
        self.res = self.root.res
        self.video = self.root.video
        self.lang = self.root.res.lang_str.lang_dict
        self.video.start()
        self.cpu.start()

        info = {'com': 'get_info()'}
        self.cpu.qcom.put(info)

        # присвоение строковых ресурсов
        self.set_res_str()

        self.gui.run()

    def exit(self):
        """
        Общесистемный выход из программы.
        Всякие финальные действия.
        """
        # print 'ClsLogic.exit()'
        try:
            self.root.gui.winEditBP.win_exit()
            self.root.gui.win_screen.win_exit()
            self.root.gui.winLicense.win_exit()
            self.root.gui.win_idc.win_exit()
            self.root.gui.winCreateDisk.win_exit()
            self.root.gui.win_about.win_exit()
            self.root.gui.win_main.win_exit()
            self.root.cpu.terminate()
            self.root.video.terminate()
            del self.root.cpu
        finally:
            sys.exit(0)

    def show_win_license(self):
        """
        Вызывается при показе окна показа лицензии (вот такая рекурсия)  )))
        """
        self.root.gui.winLicense.show()

    def show_win_idc(self):
        """

        Вызывается при показе окна интерфейса дискового кластера.
        """
        self.root.gui.win_idc.show()

    def hide_win_license(self):
        """
        Скрывает окно показа лицензии.
        """
        if 'lin' not in sys.platform:
            self.root.gui.win_about.grab_set()
