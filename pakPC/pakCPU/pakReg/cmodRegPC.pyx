# -*- coding: utf8 -*-
'''
Класс регистра счётчика команд.
По умолчанию класс имеет 16 бит (0...MAX_ADR)
'''

cdef class clsRegPC:
    cdef readonly int val # значение счётчика
    cdef readonly int max_adr # максимальное значение адреса
    def __init__(self, root=None, int max_adr=0xFFFF):
        self.root=root
        self.max_adr=max_adr
        # сбросить регистр в ноль
        self.val=0
        
    def get(self):
        return self.val
        
    def set(self, int new_val):
        if new_val<self.max_adr and new_val>=0:
            self.val=new_val
