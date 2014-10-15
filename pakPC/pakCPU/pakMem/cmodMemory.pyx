# -*- coding: utf8 -*-
'''
Класс памяти с компиляцией. Будем со временем дорабатывать.
'''
cdef struct Mem: # описание структуры памяти
    int adr[16777216] # 2**24
    int max_adr

cdef class clsMemory:
    cdef public Mem *Mem           # память виртуального компьютера
    def __init__(self, max_adr=16777216):
        self.Mem.max_adr=max_adr
        # инициализация памяти виртуального компьютера
        for i in xrange(0,self.Mem.max_adr):
            self.Mem.adr[i]=0
