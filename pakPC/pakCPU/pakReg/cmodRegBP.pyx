# -*- coding: utf8 -*-
'''
Класс регистра для остановки процессора.
'''

cdef class clsRegBP:
    cdef int adr_break, adr_proc
    def __init__(self, adr_break=0, act=0, adr_proc=0):
        '''
        adr_break -- aдрес, на который бряк
        act -- активность регистра
        adr_proc -- куда перекинуть управление
        '''
        self.adr_break=adr_break
        self.adr_old=0
        self.act=act
        self.adr_proc=adr_proc
        
    cpdef get_adr_break(self):
        return self.adr_break
        
    cpdef set_adr_break(self, int adr_break):
        self.adr_break=adr_break
        
    cpdef get_adr_proc(self):
        return self.adr_proc
        
    cpdef set_adr_proc(self, int adr_proc):
        self.adr_proc=adr_proc
