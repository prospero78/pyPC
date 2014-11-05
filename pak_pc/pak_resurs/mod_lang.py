# -*- coding: utf8 -*-
"""
Модуль является базовым классом для для классов языков.
"""


class ClsLang(object):
    """
    Базовый класс для всех классов языков.
    """

    def __init__(self, lang='ru'):
        """
        Корневой класс для всех классов языков.
        """
        self.vers = 4
        self.__lang = lang

        # словарь переводов
        self.__lang_dict = {}

    @property
    def lang(self):
        """
        Возвращает установленный язык.
        """
        return self.__lang

    @lang.setter
    def lang(self, val='ru'):
        """
        Устанавливает текущий язык.
        Если значение неприемлимое -- ничего не делает.
        """
        if val == None or val == '':
            print 'ClsLang._set_lang(): invalid val language!'
        else:
            self.__lang = val

    @property
    def lang_dict(self):
        """
        Свойство определения словаря перевода.
        """
        return self.__lang_dict

    @lang_dict.setter
    def lang_dict(self, val_dict=None):
        """
        Устанавливает новый словарь для переводов.
        """
        if val_dict == None:
            print 'ClsLang._set_lang_dict(): invalid val_dict language!'
        else:
            self.__lang_dict = val_dict

