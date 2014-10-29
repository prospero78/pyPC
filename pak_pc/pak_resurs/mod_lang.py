# -*- coding: utf8 -*-
'''
Модуль является базовым классом для для классов языков.
'''

class ClsLang(object):
    '''
    Базовый класс для всех классов языков.
    '''
    def __init__(self, lang='ru'):
        '''
        Корневой класс для всех классов языков.
        '''
        self.vers = 2
        self.__lang = lang

        # словарь переводов
        self.lang_dict = {}

    @property
    def lang(self):
        '''
        Возвращает установленный язык.
        '''
        return self.__lang

    @lang.setter
    def lang(self, val=None):
        ''''
        Устанавливает текущий язык.
        Если значение неприемлимое -- ничего не делает.
        '''
        if val == None or val == '':
            print 'ClsLang.lang_setter(): invalid val language!'
        else:
            self.__lang = val
