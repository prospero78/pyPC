# -*- coding: utf8 -*-
'''
Класс памяти с компиляцией. Будем со временем дорабатывать.
'''

class clsMemory:
    def __init__(self, int max_adr=2**20):
        self.max_adr=max_adr
        # инициализация памяти виртуального компьютера
        self.adr={}
        cdef int i
        for i in xrange(0, max_adr):
            self.adr[i]=0
