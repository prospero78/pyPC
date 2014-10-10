# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''
from pakReg.modReg import clsReg
from pakMem.modMemory import clsMemory
from pakReg.modRegSP import clsRegSP
from pakReg.modRegPC import clsRegPC
from pakReg.modReg   import clsReg

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
        
        self.RegA=clsReg(root=self.root, mem=self.Mem, pc=self.RegPC)
        
    def run(self):
        pass
    
    def step(self):
        cop=self.Mem.adr[self.regPC.val]
        self.RegA.command(cop=cop)
