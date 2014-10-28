# -*- coding: utf8 -*-
'''
Класс регистра для остановки процессора.
'''

class clsRegBP:
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
    
    def get_adr_break(self):
        return self.adr_break
        
    def set_adr_break(self, adr_break):
        self.adr_break=adr_break
        
    def get_adr_proc(self):
        return self.adr_proc
        
    def set_adr_proc(self, adr_proc):
        self.adr_proc=adr_proc
        
    def get_act(self):
        return self.act
        
    def set_act(self, act):
        self.act=act
    
    def get_adr_old(self):
        return self.adr_old
        
    def set_adr_old(self, adr_old):
        self.adr_old=adr_old
