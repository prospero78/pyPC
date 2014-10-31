# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''

import multiprocessing

from time import time, sleep
from pak_pc.pak_cpu.pak_mem.mod_memory import ClsMemory
#from pakMem.cmodMemory import clsMemory
from pak_pc.pak_cpu.pak_mem.mod_port import ClsPort
from pak_pc.pak_cpu.pak_reg.mod_reg_sp import ClsRegSP
from pak_pc.pak_cpu.pak_reg.mod_reg_pc import ClsRegPC
from pak_pc.pak_cpu.pak_reg.mod_reg   import ClsReg
from pak_pc.pak_cpu.pak_reg.mod_reg_bp import ClsRegBP
#from pakReg.cmodreg_pc import ClsRegPC


class ClsCPU(multiprocessing.Process):
    '''
        Здесь надо хорошо подумать сколько элементарных операций будет
        выполнять процессор. Длина команды (без старшего бита)
        ограничена семью битами. Видимо, пока буду пилить один РОН, т.
        к. непонятно, сколько будет элементарных команд на один регистр.
        Теоретически, и одного регистра должно хватить с удовольствием.)
        ----------------------
        Класс центрального процессора обеспечивает выполнение кодов
        операций и обработку данных.
        ----------------------
        FEDCBA98 7 6543210
                 |   |
                 |   код операции в регистре
                 два регистра общего назначения
           векторы прерываний
        расширенные команды процессора

        На каждый регистр отводится по 128 простых команд (7 бит)
    '''

    def __init__(self, max_value=0, max_adr=0, vcom=None, vinfo=None):
        def load_bios():
            '''
            Загружает BIOS по умолчанию.
            BIOS содержится в py-файле, обычный хитрый словарь.
            '''
            # инициализация биоса
            from pak_pc.pak_resurs.mod_bios import bios
            for i in bios:
                #print i, bios[i], type(i)
                if i > self.mem.max_adr:
                    self.mem.add_adr()
                self.mem.adr[i] = bios[i]
            print '  = BIOS load OK ='
        # создание отдельного процесса
        multiprocessing.Process.__init__(self)
        self.daemon = True
        # очередь для получения команд
        self.qcom = multiprocessing.Queue()
        # очередь для отправки информации
        self.qinfo = multiprocessing.Queue()

        # частота работы процессора
        self.frec = 1.0
        # количество команд для замера
        self.time_code = 50000
        # признак необходимости цикла отладки
        self.run_debug = 0

        self.max_val = max_value
        self.max_adr = max_adr

        # инициализация памяти
        self.mem = ClsMemory()
        load_bios()
         # инициализация портов
        self.port = ClsPort(max_port=2**16,
                            vinfo=vinfo,
                            vcom=vcom)

        self.reg_sp = ClsRegSP(val=self.mem.act_mem-1,
                               min_adr=self.mem.max_adr-101)
        self.reg_pc = ClsRegPC(val=0, max_adr=self.reg_sp.min_adr-1)

        # регистр для установки принудительного прерывания исполнения программы
        self.reg_bp = ClsRegBP(act=0, adr_break=0, adr_proc=0)

        self.reg_a = ClsReg(root=self,
                            mem=self.mem,
                            pc=self.reg_pc,
                            sp=self.reg_sp,
                            port=self.port)
    def run(self):
        '''
        Метод необходим для запуска отдельного процесса.
        '''
        while True:
            #print("The process CPU!")
            if not self.qcom.empty():
                com = self.qcom.get()
                if com.has_key('com'):
                    com = com['com']
                    if com == 'step()':
                        self.reg_a.command()
                        #print 'com:step()    reg_pc.adr_break=',
                        # self.reg_pc.adr_break
                        self.send_info()
                        #print '***'
                    elif com == 'debug(on)':
                        self.run_debug = 1
                        info = {'debug':'on'}
                        self.qinfo.put(info)
                        self.debug()
                    elif com == 'debug(off)':
                        self.run_debug = 0
                        info = {'debug':'off'}
                        self.qinfo.put(info)
                    elif com == 'reset':
                        self.reset_pc()
                        self.reset_pc()
                    elif com == 'get_info()':
                        self.send_info()
                elif com.has_key('reg_pc'):
                    reg = com['reg_pc']
                    self.reg_bp.act = reg['act']
                    self.reg_bp.adr_proc = reg['adr_proc']
                    self.reg_bp.adr_break = reg['adr_break']
                    reg_pc = {'act':self.reg_bp.act,
                             'adr_proc':self.reg_bp.adr_proc,
                             'adr_break':self.reg_bp.adr_break}
                    info = {'reg_pc':reg_pc}
                    self.qinfo.put(info)
                    pass
            sleep(0.1)

    def debug(self):
        i = 0
        while self.run_debug == 1:
            time1 = time()
            while i < self.time_code:
                self.reg_a.command()
                i += 1
            else:
                i = 0
                dtime = time() - time1
                inf_time = {'dtime':dtime}
                self.qinfo.put(inf_time)
                time1 = time()
                if not self.qcom.empty():
                    com = self.qcom.get()
                    if com.has_key('com'):
                        com = com['com']
                        if com == 'debug(off)':
                            self.run_debug = 0
                            info = {'debug':'off'}
                            self.qinfo.put(info)
                        elif com == 'reset':
                            self.reset_pc()
                            info = {'debug':'reset'}
                            self.qinfo.put(info)
        else:
            info = {'debug':'end'}
            self.qinfo.put(info)

    def reset_pc(self):
        '''
        Принудительно сбрасывает текущее состояние компьютера.
        Пока без сброса reg_pc, не подчищает стек.
        '''
        self.reg_a.val = 0
        self.reg_a.FlagZ = 1
        self.reg_a.FlagO = 0
        self.reg_a.FlagC = 0
        self.reg_pc.val = 0
        self.reg_sp.val = 0
        self.send_info()

    def send_info(self):
        RegA = {'val':self.reg_a.val,
                'FlagZ':self.reg_a.FlagZ,
                'FlagO':self.reg_a.FlagO,
                'FlagC':self.reg_a.FlagC}
        reg_pc = {'val':self.reg_pc.val}
        reg_pc = {'act':self.reg_bp.act,
                 'adr_proc':self.reg_bp.adr_proc,
                 'adr_break':self.reg_bp.adr_break}
        reg_sp = {'adr':self.reg_sp.val,
                 'val':self.mem.adr[self.reg_sp.val]}
        info = {'RegA':RegA,
                'reg_pc' :reg_pc,
                'reg_pc' :reg_pc,
                'reg_sp':reg_sp,}
        self.qinfo.put(info)
