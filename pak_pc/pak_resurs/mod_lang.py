# -*- coding: utf8 -*-
'''
Модуль является базовым классом для для классов языков.
'''

class ClsLang(object):
    '''
    Базовый класс для всех классов языков.
    '''
    def __init__(self):
        self.__vers = 1

    @property
    def vers(self):
        '''
        Свойство возвращающее версию текущего класса.
        '''
        return self.__vers
