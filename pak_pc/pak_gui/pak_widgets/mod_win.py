# -*- coding: utf8 -*-
"""
Общий модуль предок для всех окон в программе, которые наследуются от Toplevel.
"""
__author__ = 'prospero78'

from Tkinter import Toplevel

class ClsWin(Toplevel):
    """
    Класс окна с нормальными атрибутами скрытия и появления.
    """
    def __init__(self, title='ClsWin'):
        """
        Создаёт окно и скрывает его.
        :param title:
        :return:
        """
        self.title_txt = title
        Toplevel.__init__(self)
        self.title(self.title_txt)
        self.state('withdrawn')
        self.minsize(640, 480)
        # признак отображённости окна терминала
        self.win_screen_show = 0

    def show(self):
        """
        Показывает окно.
        :return:
        """
        self.win_screen_show = 1
        self.state('normal')
        # показать поверх всех с фокусом без удержания фокуса
        self.focus_set()

    def destroy(self):
        """
        Скрывает окно.
        :return:
        """
        self.win_screen_show = 0
        self.state('withdrawn')
        self.grab_release()

    def win_exit(self):
        """
        Выполняется при уничтожении окна (выход из программы).
        :return:
        """
        self.destroy()
