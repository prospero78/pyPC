# -*- coding: utf8 -*-
'''
Класс регистра общего назначения.
По умолчанию класс имеет 8 бит (0...255) -- MAX_REG_VAL
'''

class clsReg:
    def __init__(self, root=None, max_reg_val=0xFF, PC_val=0):
        self.root=root
        self.MaxRegVal=max_reg_val
        
        # сбросить регистр в ноль и установить флаг нуля
        self.val=0
        self.FlagZ=1
        self.FlagO=0
        self.FlagC=0
        
        # запомнить ссылку на программный счётчик
        self.PC=PC_val
    
    def init2(self, RegA=None, RegB=None):
        '''
        Это вторичная ссылка инициализации, т. к. процессор не знает какие регистры есть, и сколько.
        И это плохо, надо бы что-то с этим сделать.
        '''
        pass
        
    def command(self, cop=0):
        '''
        Вычисляет что за команда поступила на вход и
        далее обрабатывает её, в зависимости от кода
        --------------------
        cop - "код операции"
        -------------------
        '''
        if cop==0: # R.set(A) по сути ничего не делать
            self.val=self.A.val
            self.FlagZ=0
            self.FlagO=0
            self.FlagC=0
        elif cop==1: # R.set(B) установить регистр R значением регистра В
            self.val=self.B.val
            self.FlagZ=0
            self.FlagO=0
            self.FlagC=0
