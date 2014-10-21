# -*- coding: utf8 -*-
'''
Класс описывающий массив портов.
Не вижу смысла задавать портов более,
чем 65 тыс. (2**16)
'''

class clsPort:
    def __init__(self, max_port=2**16):
        # максимально допустимое количество портов
        self.max_port=max_port
        # инициализация адресов портов виртуального компьютера
        self.adr={}
        for i in xrange(0, max_port):
            self.adr[i]=0
    
    def get_adr(self, adr):
        '''
        Получить состояние порта
        '''
        return self.adr[adr]
        
    def set_adr(self, adr, val):
        '''
        Установить состояние порта
        '''
        self.adr[adr]=val
