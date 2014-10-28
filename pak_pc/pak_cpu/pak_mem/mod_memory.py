# -*- coding: utf8 -*-
'''
Класс памяти. Будем со временем дорабатывать.
'''

class ClsMemory:
    def __init__(self, max_adr=2**22):
        # максимально допустимое количество памяти
        self.max_adr=max_adr
        # текущее количество памяти
        self.act_mem=1024
        # инициализация памяти виртуального компьютера
        self.adr={}
        for i in xrange(0, self.act_mem):
            self.adr[i]=0
    
    def get_adr(self, adr):
        return self.adr[adr]
        
    def set_adr(self, adr, val):
        self.adr[adr]=val
        
    def get_max_adr(self):
        return self.max_adr
        
    def add_memory(self):
        if self.act_mem<self.max_adr-1024:
            for i in xrange(self.act_mem, self.act_mem+1024):
                self.adr[i]=0
            self.act_mem+=1024
