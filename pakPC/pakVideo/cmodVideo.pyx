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

class clsVideo():
    cdef int Mem[3888000]=0 # блок видеопамяти рассчитанный на 1024х768х24 бита
    cdef int mode=0 # регистр отвечающий за режим видеокарты
    cdef int command=0 # регистр типа команды
    cdef char buf[1024]=' ' # строковый буфер для работы с экраном
    def __init__(self, root=None):
        self.root=root
    
    def fill(self, color='#000'):
        '''
        Заполнение экрана виртуального компьютера заданным цветом.
        '''
        pass