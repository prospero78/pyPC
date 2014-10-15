# -*- coding: utf8 -*-
'''
Класс регистра для остановки процессора.
'''

class clsRegBP:
    def __init__(self, root=None, adr_break=0, act=0, adr_proc=0):
        '''
        adr_break -- aдрес, на который бряк
        act -- активность регистра
        adr_proc -- куда перекинуть управление
        '''
        self.root=root
        self.adr_break=adr_break
        self.adr_old=0
        self.act=act
        self.adr_proc=adr_proc
