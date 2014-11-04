# -*- coding: utf8 -*-
'''
Класс регистра для остановки процессора.
'''

cdef class clsRegBP:
    cdef int adr_break, adr_proc, adr_old, flag_act
    def __init__(self, adr_break=6, flag_act=1, adr_proc=0):
        '''
        adr_break -- aдрес, на который бряк
        flag_act -- активность регистра
        adr_proc -- куда перекинуть управление
        '''
        self.adr_break = adr_break
        self.adr_old = 0
        self.flag_act = flag_act
        self.adr_proc = adr_proc

    cpdef get_adr_break(self):
        return self.adr_break

    cpdef set_adr_break(self, int adr_break):
        self.adr_break = adr_break

    cpdef get_adr_proc(self):
        return self.adr_proc

    cpdef set_adr_proc(self, int adr_proc):
        self.adr_proc = adr_proc

    cpdef get_act(self):
        return self.flag_act

    cpdef set_act(self, int flag_act):
        self.flag_act = flag_act

    cpdef get_adr_old(self):
        return self.adr_old

    cpdef set_adr_old(self, int adr_old):
        self.adr_old = adr_old
