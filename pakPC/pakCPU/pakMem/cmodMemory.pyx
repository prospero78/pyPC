# -*- coding: utf8 -*-
'''
Класс памяти с компиляцией. Будем со временем дорабатывать.
'''

class clsMemory:
    def __init__(self, max_adr=2**20):
        self.max_adr=max_adr
        # инициализация памяти виртуального компьютера
        self.adr={}
        for i in xrange(0,self.max_adr):
            self.adr[i]=0
