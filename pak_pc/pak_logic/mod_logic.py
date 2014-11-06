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
        self.__root = root
        # локальная переменная для регистра программного счётчика
        self.__reg_pc_old = 0
        # значение регистра программного счётчика
        self.__reg_pc_val = 0
        # признаки запущенности ЦП в debug mode
        self.__debug = 0
        # признак активности регистра bp
        self.__reg_bp_act = None
        # ссылка на ЦП
        self.__cpu = None
        # ссылка на графический интерфейс
        self.__gui = None
        # ссылка на экран виртуальной машины
        self.__win_screen = None
        # ссылка на класс ресурсов
        self.__res = None
        # ссылка на видеокарту
        self.__video = None
        # ссылка на языковые ресурсы
        self.__lang = None
        # ссылка на регистр bp, признак akt
        self.__reg_pc_act = None
        # ссылка на регистр bp и его адрес прерывания
        self.reg_pc_adr_break = None
        # ссылка на регистр bp и его адрес обработки
        self.__reg_pc_adr_proc = None

    def __set_res_str(self):
        """
        Присваивает строковые ресурсы графическому интерфейсу.
        Процедура сделана с целью отвязки GUI от ресурсов
        (повышение атомарности класса).
        """
        win_main = self.__gui.win_main
        win_main.btn_step['text'] = self.__lang['win_main_btn_step']
        win_main.btn_debug['text'] = self.__lang['win_main_btn_debug_0']
        win_main.btn_exit['text'] = self.__lang['win_main_btn_exit_name']
        win_main.btn_show_screen['text'] = self.__lang[
            'win_main_btn_show_screen_show']
        win_main.btn_reset['text'] = self.__lang['win_main_btn_reset']
        win_main.mbt_file['text'] = self.__lang['win_main_mbt_file_name']
        win_main.mbt_edit['text'] = self.__lang['win_main_mbt_edit_name']
        win_main.mbt_custom['text'] = self.__lang['win_main_mbt_custom_name']
        win_main.frm_cpu.frm_cpu_freq.lbl_key['text'] = self.__lang[
            'win_main_frm_cpu_freq_lbl_key']

    def reset_pc(self):
        """
        Сброс состояния виртуального компьютера.
        """
        info = {'com': 'reset'}
        self.__cpu.qcom.put(info)

    def __update_speed(self, dtime=0):
        """
        При отладке обновляет периодически монитор состояния ЦП и скорость
        виртуальной машины.
        :type self: object
        :param dtime: производит замер по времени между циклами исполнения
        блока команд ЦП.
        """
        freq_cpu = 1.0 / dtime * self.__cpu.time_code
        # print dtime, self.__cpu.frec
        res = freq_cpu / self.__cpu.frec
        if res > 1.1 or res < 0.9:
            if freq_cpu > self.__cpu.frec:
                self.__cpu.frec += int(freq_cpu / 100)
            elif freq_cpu < self.__cpu.frec:
                self.__cpu.frec -= int(freq_cpu / 100)
            if freq_cpu > 1000:
                freq_cpu = str(int(self.__cpu.frec / 1000)) + ' kHz'
            else:
                freq_cpu = str(int(self.__cpu.frec)) + ' Hz'
            frec = self.__gui.win_main.frm_cpu.frm_cpu_frec
            frec.ent_val.delete(0, 'end')
            frec.ent_val.insert(0, freq_cpu)
            # self.__gui.win_main.update()

    def win_edit_bp_hide(self):
        """
        Вызывается при скрытии окна редактирования свойств регистра
        программного прерывания.
        """
        print '  ClsLogic.win_edit_bp_hide()'
        # --- обновить содержимое реального регистра программных прерываний ----
        win_edit_bp = self.__gui.win_edit_bp
        self.__reg_pc_act = win_edit_bp.flag_act.get()
        self.reg_pc_adr_break = int(win_edit_bp.ent_adr_break_val.get())
        self.__reg_pc_adr_proc = int(win_edit_bp.ent_adr_proc_val.get())

        info = {'reg_pc': {'flag_act': self.__reg_pc_act,
                           'adr_break': self.reg_pc_adr_break,
                           'adr_proc': self.__reg_pc_adr_proc}}
        self.__cpu.qcom.put(info)

        # print 'flag_act=', self.__cpu.reg_pc.get_act()
        #self.update_monitor()

    def show_win_edit_bp(self):
        # print 'ClsLogic.show_win_edit_bp()'
        """
        Вызывается при показе окна редактирования свойств регистра
        программного прерывания.
        """
        self.__gui.win_edit_bp.show()

    def debug_cpu(self):
        """
        Вызывается при запуске ЦП в режиме отладки.
        """
        # print 'ClsLogic.debug_cpu()'
        lang = self.__root.res.lang_str.lang_dict
        if self.__debug == 0:
            self.__debug = 1
            self.__gui.win_main.btn_debug['text'] = lang['win_main_btn_debug_1']
            info = {'com': 'debug(on)'}
        else:
            self.__debug = 0
            self.__gui.win_main.btn_debug['text'] = lang['win_main_btn_debug_0']
            info = {'com': 'debug(off)'}
        self.__cpu.qcom.put(info)

    def step_cpu(self):
        """
        Метод исполняет шаг процессора с выводом результата.
        Команды отправляются в очередь между процессами.
        """
        # print 'ClsLogic.step_cpu()'
        # self.pre_update_monitor()
        info = {'com': 'step()'}
        self.__cpu.qcom.put(info)
        #self.post_update_monitor()

    def update_monitor(self):
        """
        Обновляет монитор ЦП через равные промежутки времени.
        Информацию для обновления берёт от двух дочерних процессов:
        1. ЦП.
        2. Видеокарта.
        """
        while not self.__cpu.qinfo.empty():
            info = self.__cpu.qinfo.get()
            if 'reg_a' in info:
                inf = info['reg_a']
                # print 'detect reg_a', inf
                reg_a = self.__gui.win_main.frm_cpu.frm_reg_a
                # print 'have key "reg_a.val"!', info['reg_a.val']
                reg_a.lbl_val['text'] = inf['val']
                #print "have key \"reg_a.flag_z\"!", info['reg_a.flag_z']
                reg_a.lbl_val_z['text'] = inf['flag_z']
                #print 'have key "reg_a.flag_o"!', info['reg_a.flag_o']
                reg_a.lbl_val_o['text'] = inf['flag_o']
                #print 'have key "reg_a.flag_c"!', info['reg_a.flag_c']
                reg_a.lbl_val_c['text'] = inf['flag_o']
            if 'reg_pc' in info:
                inf = info['reg_pc']
                # print 'detect reg_pc', inf
                # print 'have key "reg_pc.val"!', info['reg_pc.val']
                self.__reg_pc_val = inf['val']
                self.__gui.win_main.frm_cpu.frm_reg_pc.lbl_val[
                    'text'] = self.__reg_pc_old
                self.__reg_pc_old = self.__reg_pc_val
            # ---------------------------
            if 'reg_bp' in info:
                inf = info['reg_bp']
                reg_bp = self.__gui.win_main.frm_cpu.frm_reg_bp
                # print 'have key "reg_bp.flag_act"!', info['reg_bp.flag_act']
                reg_bp.lbl_act_val['text'] = inf['flag_act']
                #print 'have key "reg_bp.adr_proc"!', info['reg_bp.adr_proc']
                reg_bp.lbl_proc_val['text'] = inf['adr_proc']
                #print 'have key "reg_pc.adr_break"!', info['reg_pc.adr_break']
                reg_bp.lbl_break_val['text'] = inf['adr_break']
            # ---------------------------
            if 'reg_sp' in info:
                inf = info['reg_sp']
                reg_sp = self.__gui.win_main.frm_cpu.frm_reg_sp
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
                self.__update_speed(dtime=inf)
        while not self.__video.vout.empty():
            vout = self.__video.vout.get()
            self.__win_screen.lbl_screen['text'] = vout

    def generate_new_disk(self):
        # print 'generate_new_disk()'
        """
        Создаёт новый диск.
        """
        self.__gui.win_create_disk.destroy()
        disk_size = int(self.__gui.win_create_disk.fkv_size.get_val())
        disk_name = self.__gui.win_create_disk.fkv_name.get_val()
        str_ = '0' * (2 ** 10)
        file_disk = open('./data/' + disk_name + '.dsk', 'wb')
        block_kb = 0
        while block_kb < disk_size:
            file_disk.write(str_)
            file_disk.close()
            block_kb += 1

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
        self.__gui.win_create_disk.show()

    def show_screen(self):
        """
        Вызывается при показе экрана виртуальной машины.
        """
        if not self.__gui.win_screen.win_screen_show:
            self.__gui.win_screen.show()
        else:
            self.__gui.win_screen.destroy()

    def run(self):
        """
        Вызывается при запуске всей системы.

        """
        self.__cpu = self.__root.cpu
        self.__gui = self.__root.gui
        self.__win_screen = self.__gui.win_screen
        self.__res = self.__root.res
        self.__video = self.__root.video
        self.__lang = self.__root.res.lang_str.lang_dict
        self.__video.start()
        self.__cpu.start()

        info = {'com': 'get_info()'}
        self.__cpu.qcom.put(info)

        # присвоение строковых ресурсов
        self.__set_res_str()

        self.__gui.run()

    def exit(self):
        """
        Общесистемный выход из программы.
        Всякие финальные действия.
        """
        # print 'ClsLogic.exit()'
        try:
            self.__root.gui.win_edit_bp.win_exit()
            self.__root.gui.win_screen.win_exit()
            self.__root.gui.win_license.win_exit()
            self.__root.gui.win_idc.win_exit()
            self.__root.gui.win_create_disk.win_exit()
            self.__root.gui.win_about.win_exit()
            self.__root.gui.win_main.win_exit()
            self.__root.cpu.terminate()
            self.__root.video.terminate()
            del self.__root.cpu
        finally:
            sys.exit(0)

    def show_win_license(self):
        """
        Вызывается при показе окна показа лицензии (вот такая рекурсия)  )))
        """
        self.__root.gui.win_license.show()

    def show_win_idc(self):
        """

        Вызывается при показе окна интерфейса дискового кластера.
        """
        self.__root.gui.win_idc.show()

    def hide_win_license(self):
        """
        Скрывает окно показа лицензии.
        """
        if 'lin' not in sys.platform:
            self.__root.gui.win_about.grab_set()
