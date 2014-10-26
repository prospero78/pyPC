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
        
'''

class clsVideo:
    def __init__(self, root=None):
        '''
        По умолчанию создаётся один экран в текстовом режиме, монохромный,
        размером 80*40 знакомест (3200 позиций).
        '''
        self.root=root
        # максимальный режим видеокарты
        self.mode_max=0
        # текущий режим видеокарты
        self.mode_current=0
        
        self.command=0
        self.buf=''
        self.adr={}
        self.clear_screen()
        #self.adr=' '*3200 # будет символный экран на 3200 символов.
    
    def clear_screen(self):
        '''
        Очищает терминал от текста.
        Процедура заливки фактически это и делает.
        '''
        print 'VIDEO: clear_screen()'
        self.fill_screen()
        
    def fill_screen(self, sym=' '):
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
        print 'VIDEO: set_current_mode()', mode
        if mode>self.mode_max:
            self.mode_current=self.mode_max
        elif mode<0 or mode==None:
            self.mode_current=0
        else:
            self.mode_current=mode
        return self.mode_current
