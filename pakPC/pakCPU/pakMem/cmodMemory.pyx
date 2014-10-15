# -*- coding: utf8 -*-
'''
Класс памяти с компиляцией. Будем со временем дорабатывать.
'''
DEF all_mem=2**24
cdef class clsMemory:
    cdef int adr[all_mem] # 2**24 16777216
    cdef int max_adr
    def __init__(self, long max_adr=2**24):
        self.max_adr=max_adr
        #cdef int adr[2**24] # 2**24
        # инициализация памяти виртуального компьютера
        cdef long i
        for i in xrange(0, max_adr):
            self.adr[i]=0
            
    cpdef int get_adr(self, int adr):
        return self.adr[adr]
        
    cpdef set_adr(self, int adr, int val):
        self.adr[adr]=val
        
    cpdef int get_max_adr(self):
        return self.max_adr
