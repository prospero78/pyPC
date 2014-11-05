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

    def _get_lang_dict(self):
        """
        Возвращает словарь для перевода надписей.
        """
        return self.__lang_dict

    def _set_lang_dict(self, val_dict= {}):
        """
        Устанавливает новый словарь для переводов.
        """
        if val_dict == {} or val_dict == None:
            print 'ClsLang._set_lang_dict(): invalid val_dict language!'
        else:
            self.__lang_dict = val_dict

    lang_dict = property(_get_lang_dict, _set_lang_dict)

    def _get_lang(self):
        """
        Возвращает установленный язык.
        """
        return self.__lang

    def _set_lang(selfself, val='ru'):
        """
        Устанавливает текущий язык.
        Если значение неприемлимое -- ничего не делает.
        """
        if val == None or val == '':
            print 'ClsLang._set_lang(): invalid val language!'
        else:
            self.__lang = val

    lang = property(_get_lang, _set_lang)

