# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''

import multiprocessing

from time import time, sleep
from pakReg.modReg import clsReg
from pakMem.modMemory import clsMemory
#from pakMem.cmodMemory import clsMemory
from pakReg.modRegSP import clsRegSP
from pakReg.modRegPC import clsRegPC
from pakReg.modReg   import clsReg
from pakReg.modRegBP import clsRegBP
#from pakReg.cmodRegBP import clsRegBP

class clsCPU(multiprocessing.Process):
    '''
        Здесь надо хорошо подумать сколько элементарных операций будет выполнять процессор.
        Длина команды (без старшего бита) ограничена семью битами.
        Видимо, пока буду пилить один РОН, т. к. непонятно, сколько будет элементарных команд
        на один регистр. Теоретически, и одного регистра должно хватить с удовольствием. )
        ----------------------
        Класс центрального процессора обеспечивает выполнение кодов операций и 
        обработку данных.
        ----------------------
        FEDCBA98 7 6543210
                 |   |
                 |   код операции в регистре
                 два регистра общего назначения
           векторы прерываний
        расширенные команды процессора
        
        На каждый регистр отводится по 128 простых команд (7 бит)
    '''
    
    def __init__(self, max_value=0, max_adr=0, bios=None):
        def load_bios(bios):
            '''
            Загружает BIOS по умолчанию.
            BIOS содержится в py-файле, обычный хитрый словарь.
            '''
            for i in bios.data:
                print i, bios.data[i], '\n'
                self.Mem.adr[i] = bios.data[i]
        # создание отдельного процесса
        multiprocessing.Process.__init__(self)
        self.daemon=True
        # очередь для получения команд
        self.qcom=multiprocessing.Queue()
        # очередь для отправки информации
        self.qinfo=multiprocessing.Queue()
        
        # частота работы процессора
        self.frec=1.0
        # количество команд для замера
        self.time_code=5000
        
        self.max_val=max_value
        self.max_adr=max_adr
       
        self.Mem=clsMemory()
        load_bios(bios)
        
        self.RegSP=clsRegSP(val=self.max_adr, min_adr=self.max_adr-100)
        self.RegPC=clsRegPC(val=0, max_adr=self.RegSP.min_adr-1)
        
        # регистр для установки принудительного прерывания исполнения программы
        self.RegBP=clsRegBP(act=0, adr_break=0, adr_proc=0)
        
        self.RegA=clsReg(root=self, mem=self.Mem, pc=self.RegPC)
        
    def run(self):
        '''
        Метод необходим для запуска отдельного процесса.
        '''
        while True:
            #print("The process CPU!")
            if not self.qcom.empty():
                com=self.qcom.get()
                if com.has_key('com'):
                    self.RegA.command()
                    print 'com:step()    RegBP.adr_break=', self.RegBP.adr_break
                    info={  'RegA.val'  :self.RegA.val,
                            'RegA.FlagZ':self.RegA.FlagZ,
                            'RegA.FlagO':self.RegA.FlagO,
                            'RegA.FlagC':self.RegA.FlagC,
                            'RegPC.val' :self.RegPC.val,
                            'RegBP.act' :self.RegBP.act,
                            'RegBP.adr_proc':self.RegBP.adr_proc,
                            'RegBP.adr_break':self.RegBP.adr_break,}
                    self.qinfo.put(info)
                if com.has_key('RegBP'):
                    reg=com['RegBP']
                    self.RegBP.act=reg['act']
                    self.RegBP.adr_proc=reg['adr_proc']
                    self.RegBP.adr_break=reg['adr_break']
                    pass
            sleep(0.1)
        
    def debug(self):
        i=0
        time1=time()
        while self.RegBP.adr_old==0:
            self.RegA.command()
            i+=1;
            if i==self.time_code:
                i=0
                self.root.Logic.update_speed(dtime=time()-time1)
                time1=time()
