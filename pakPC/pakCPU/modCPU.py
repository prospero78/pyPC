# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''

import multiprocessing



from time import time, sleep
from pakReg.modReg import clsReg
from pakMem.modMemory import clsMemory
#from pakMem.cmodMemory import clsMemory
from pakMem.modPort import clsPort
from pakReg.modRegSP import clsRegSP
from pakReg.modRegPC import clsRegPC
from pakReg.modReg   import clsReg
from pakReg.modRegBP import clsRegBP
#from pakReg.cmodRegBP import clsRegBP

# импрот класса видеокарты
from pakPC.pakVideo.modVideo import clsVideo

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
    
    def __init__(self, max_value=0, max_adr=0):
        def load_bios():
            '''
            Загружает BIOS по умолчанию.
            BIOS содержится в py-файле, обычный хитрый словарь.
            '''
            # инициализация биоса
            from pakPC.pakResurs.modBios import bios
            for i in bios:
                #print i, bios[i], type(i)
                if i>self.Mem.max_adr:
                    self.Mem.add_adr()
                self.Mem.adr[i] = bios[i]
            print '  = BIOS load OK ='
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
        self.time_code=50000
        # признак необходимости цикла отладки
        self.run_debug=0
        
        self.max_val=max_value
        self.max_adr=max_adr
       
        # инициализация памяти
        self.Mem=clsMemory()
        load_bios()
        
        # инициализация класса видео-терминала
        self.Video=clsVideo(root=self)
        
        # инициализация портов
        self.Port=clsPort(max_port=2**16, video=self.Video)
        
        self.RegSP=clsRegSP(val=self.Mem.act_mem,
                            min_adr=self.Mem.max_adr-100)
        self.RegPC=clsRegPC(val=0, max_adr=self.RegSP.min_adr-1)
        
        # регистр для установки принудительного прерывания исполнения программы
        self.RegBP=clsRegBP(act=0, adr_break=0, adr_proc=0)
        
        self.RegA=clsReg(root=self,
                        mem=self.Mem,
                        pc=self.RegPC,
                        sp=self.RegSP,
                        port=self.Port)
        
    def run(self):
        '''
        Метод необходим для запуска отдельного процесса.
        '''
        while True:
            #print("The process CPU!")
            if not self.qcom.empty():
                com=self.qcom.get()
                if com.has_key('com'):
                    com=com['com']
                    if com=='step()':
                        self.RegA.command()
                        #print 'com:step()    RegBP.adr_break=', self.RegBP.adr_break
                        RegA={  'val':self.RegA.val,
                                'FlagZ':self.RegA.FlagZ,
                                'FlagO':self.RegA.FlagO,
                                'FlagC':self.RegA.FlagC}
                        RegPC={'val':self.RegPC.val}
                        RegBP={ 'act':self.RegBP.act,
                                'adr_proc':self.RegBP.adr_proc,
                                'adr_break':self.RegBP.adr_break}
                        RegSP={'val':self.RegSP.val}
                        info={  'RegA':RegA,
                                'RegPC' :RegPC,
                                'RegBP' :RegBP,
                                'RegSP':RegSP,}
                        self.qinfo.put(info)
                        #print '***'
                    elif com=='debug(on)':
                        self.run_debug=1
                        info={'debug':'on'}
                        self.qinfo.put(info)
                        self.debug()
                    elif com=='debug(off)':
                        self.run_debug=0
                        info={'debug':'off'}
                        self.qinfo.put(info)
                elif com.has_key('RegBP'):
                    reg=com['RegBP']
                    self.RegBP.act=reg['act']
                    self.RegBP.adr_proc=reg['adr_proc']
                    self.RegBP.adr_break=reg['adr_break']
                    RegBP={ 'act':self.RegBP.act,
                                'adr_proc':self.RegBP.adr_proc,
                                'adr_break':self.RegBP.adr_break}
                    info={'RegBP':RegBP}
                    self.qinfo.put(info)
                    pass
            sleep(0.1)
        
    def debug(self):
        i=0
        while self.run_debug==1:
            time1=time()
            while i<self.time_code:
                self.RegA.command()
                i+=1;
            else:
                i=0
                dtime=time()-time1
                inf_time={'dtime':dtime}
                self.qinfo.put(inf_time)
                time1=time()
                if not self.qcom.empty():
                    com=self.qcom.get()
                    if com.has_key('com'):
                        self.run_debug=0
                        info={'debug':'off'}
                        self.qinfo.put(info)
        else:
            info={'debug':'end'}
            self.qinfo.put(info)
