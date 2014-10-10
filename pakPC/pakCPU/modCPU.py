# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''
from pakReg.modReg import clsReg
from pakMem.modMemory import clsMemory
from pakReg.modRegSP import clsRegSP
from pakReg.modRegPC import clsRegPC
from pakReg.modReg   import clsReg

# константы для кодов операций
if True:
    A_rset=0
    A_radd=1
    A_rsub=2
    A_rinc=3
    A_rdec=4
    A_rnot=5
    A_rxor=6
    A_ror =7
    A_rand=8
    A_rshr=9
    A_rshl=10
    #----------------------
    A_nset=11
    A_nadd=12
    A_nsub=13
    A_nnot=14
    A_nxor=15
    A_nor =16
    A_nand=17
    #---------------------
    A_mget=18
    A_madd=19
    A_msub=20
    A_minc=21
    A_mdec=22
    A_mnot=23
    A_mxor=24
    A_mor =25
    A_mand=26
    A_mshr=27
    A_mshl=28
    #-----------------
    A_getf =29
    A_setf =30
    #---------------
    A_ifz =31
    A_ncmp=32
    A_ifnz=33
    A_mset=34
    A_push=35
    A_pop =36
    A_call=37
    A_ret =38
    A_in  =39
    A_out =40
    A_vin =40
    
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
        self.detect()
