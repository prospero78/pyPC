# -*- coding: utf8 -*-
'''
Класс описывающий массив портов.
Не вижу смысла задавать портов более,
чем 65 тыс. (2**16)

Посколько портов будут тонны, здесь видимо, придётся прописывать 
процедуры для каждого порта отдельно.
'''

import multiprocessing

class clsPort:
    def __init__(self, max_port=2**16, vinfo=None, vcom=None):
        # максимально допустимое количество портов
        self.max_port=max_port
        
        # инициализация адресов портов виртуального компьютера
        self.adr={}
        for i in xrange(0, max_port):
            self.adr[i]=0
        
        self.vinfo=vinfo
        self.vcom=vcom
    
    def get_adr(self, adr):
        '''
        Получить состояние порта
        '''
        return self.adr[adr]
        
    def set_adr(self, adr, val):
        '''
        Установить состояние порта
        '''
        print 'PORT: set(', adr, ')=', val
        self.adr[adr]=val
        
    def detect_port(self, port=None, com=None):
        '''
        Тут собственно сам детектор портов.
        '''
        print '   ## PORT: detector   port=', port
        if port == 0:   # порт запроса поддерживаемых режимов видеокарты
            vcom={'com':{'get_max_mode':0}}
            self.vcom.put(vcom)
            while self.vinfo.empty():
                sleep(0.05)
            info=self.vinfo.get()
            if info.has_key('max_mode'):
                max_mode=info['max_mode']
                return max_mode
            else:
                return 0
        elif port == 1: # порт установки режима видеокарты
            vcom={'com':{'set_mode':self.adr[1]}}
            self.vcom.put(vcom)
        elif port == 2:  # режим исполнения команд
            if com == 1:    # получена команда очистки экрана
                vcom={'com':{'clear_screen':0}}
                self.vcom.put(vcom)
        elif port == 3: # режим заливки экрана
            vcom={'com':{'char':chr(com)}}
            self.vcom.put(vcom) # залить символом переданным в параметре
