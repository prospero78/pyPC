# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''

from time import time
from pakReg.modReg import clsReg
from pakMem.modMemory import clsMemory
from pakReg.modRegSP import clsRegSP
from pakReg.modRegPC import clsRegPC
from pakReg.modReg   import clsReg
from pakReg.modRegBP import clsRegBP

class clsCPU:
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
    
    def __init__(self, root=None):
        self.root=root
        
        self.max_val=self.root.Res.max_reg_val
       
        self.Mem=clsMemory(root=self.root)
        
        self.RegSP=clsRegSP(root=self.root, val=self.root.Res.max_adr, min_adr=self.root.Res.max_adr-100)
        
        self.RegPC=clsRegPC(root=self.root, val=0, max_adr=self.root.Res.max_adr-1)
        
        # регистр для установки принудительного прерывания исполнения программы
        self.RegBP=clsRegBP(root=self.root, act=0, adr_break=0, adr_proc=0)
        
        self.RegA=clsReg(root=self, mem=self.Mem, pc=self.RegPC)
        
        
    def run(self):
        pass
    
    def step(self):
        self.RegA.command()
        
    def debug(self):
        i=0
        time1=time()
        while self.RegBP.adr_old==0:
            self.RegA.command()
            i+=1;
            if i==1000:
                i=0
                self.root.Logic.update_speed(dtime=time()-time1)
                time1=time()
