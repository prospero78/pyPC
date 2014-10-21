# -*- coding: utf8 -*-
'''
Класс описывающий массив портов.
Не вижу смысла задавать портов более,
чем 65 тыс. (2**16)

Посколько портов будут тонны, здесь видимо, придётся прописывать 
процедуры для каждого порта отдельно.
'''

class clsPort:
    def __init__(self, max_port=2**16, video=None):
        # максимально допустимое количество портов
        self.max_port=max_port
        # ссылка на видео-карту
        self.Video=video
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
        print 'PORT: set(', adr, ')=', val
        self.adr[adr]=val
        
    def detect_port(self, port=None):
        '''
        Тут собственно сам детектор портов.
        '''
        print 'PORT: detector   port=', port
        if port == 0:   # порт запроса поддерживаемых режимов видеокарты
            return self.Video.get_max_mode()
        elif port == 1: # порт установки режима видеокарты
            self.Video.set_current_mode(mode=self.adr[1])
        elif port ==2:  # режим исполнения команд
            com=self.adr[port]
            if com == 1:    # получена команда очистки экрана
                self.Video.clear_screen()
