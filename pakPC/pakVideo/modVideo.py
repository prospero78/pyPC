# -*- coding: utf8 -*-
'''
Класс видеокарты.
Видеокарта приписана жёстко к портам.
0 -- порт запросов от CPU
1 -- координата х
2 -- координата y
3 -- монохром (установить/сбросить)

Команды запроса:
1 -- установить режим
    (
'''


class clsVideo:
    def __init__(self, root=None):
        self.root=root
        self.mode=0
        
        self.command=0
        self.buf=''
        self.adr={}
        for i in xrange(0, 3888000):
            self.adr[i]=0
    
    def fill(self, color='#000'):
        '''
        Заполнение экрана виртуального компьютера заданным цветом.
        '''
        pass
