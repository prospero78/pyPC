# -*- coding: utf8 -*-
'''
    Класс видеокарты.
    Видеокарта приписана жёстко к портам.
    Порт:
        0 -- запрос на поддерживаемые режимы 
        1 -- запрос на установку режима 

    Команды запроса:
    SET_VIDEO_MODE
        1 -- установить режим 80*40 текст
    Видеокарта работает в отдельном процессе, чтобы не тормозить работу ЦП,
    кроме тех случаев, когда ЦП не будет ожидать ответа от видеокарты.
    
'''

import multiprocessing
from time import sleep

class clsVideo(multiprocessing.Process):
    def __init__(self):
        '''
        По умолчанию создаётся один экран в текстовом режиме, монохромный,
        размером 80*40 знакомест (3200 позиций).
        '''
        # создание отдельного процесса
        multiprocessing.Process.__init__(self)
        self.daemon=True
        
        # очередь для получения команд
        self.vcom=multiprocessing.Queue()
        # очередь для отправки информации
        self.vinfo=multiprocessing.Queue()
        
        # максимальный режим видеокарты
        self.mode_max=0
        # текущий режим видеокарты
        self.mode_current=0
        
        self.command=0
        self.buf=''
        self.adr={}
        #self.adr=' '*3200 # будет символный экран на 3200 символов.
    
    def run(self):
        '''
        Вызывается при запуске отдельного процесса.
        '''
        self.clear_screen()
        while True:
            #print("The process VideoCard!")
            if not self.vcom.empty():
                com=self.vcom.get()
                print 'clsVideo.run(): com=', com
                if com.has_key('com'):
                    com=com['com']
                    if com.has_key('set_mode'):
                        com=com['set_mode']
                        print '       com=', com
                        self.set_current_mode(mode=com)
                    elif com.has_key('get_max_mode'):
                        info={'max_mode':self.mode_max}
                        self.vinfo.put(info)
                    elif com.has_key('clear_screen'):
                        self.clear_screen()
            sleep(0.1)
    
    def clear_screen(self):
        '''
        Очищает терминал от текста.
        Процедура заливки фактически это и делает.
        '''
        print 'VIDEO: clear_screen()'
        self.fill_screen()
        
    def fill_screen(self, sym='*'):
        '''
        Заливка экрана заданным символом.
        '''
        print 'VIDEO: fill_screen()'
        for i in xrange(0, 40):
            for i1 in xrange(0,81):
                if i1==81:
                    self.adr[i*i1]='\n'
                else:
                    self.adr[i*i1]=sym
    
    def get_max_mode(self):
        '''
        Возвращает допустимый предельный номер режима экрана.
        '''
        print 'VIDEO: get_max_mode()'
        return self.mode_max
        
    def set_current_mode(self, mode=None):
        '''
        Устанавливает новый режим экрана.
        '''
        print 'clsVideo.set_current_mode(): mode=', mode
        if mode>self.mode_max:
            self.mode_current=self.mode_max
        elif mode<0 or mode==None:
            self.mode_current=0
        else:
            self.mode_current=mode
        return self.mode_current
