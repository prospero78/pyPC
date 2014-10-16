# -*- coding: utf8 -*-
'''
Класс памяти. Будем со временем дорабатывать.
'''

class clsMemory:
    def __init__(self, max_adr=2**22):
        self.max_adr=max_adr
        # инициализация памяти виртуального компьютера
        self.adr={}
        for i in xrange(0, 1024):
            self.adr[i]=0
    
    def get_adr(self, adr):
        return self.adr[adr]
        
    def set_adr(self, adr, val):
        self.adr[adr]=val
        
    def get_max_adr(self):
        return self.max_adr
        
    def add_memory(self):
        for i in xrange(self.max_adr, self.max_adr+1024):
            self.adr[i]=0
        self.max_adr+=1024
