# /usr/bin/python27
# -*- coding: utf8 -*-
"""
Модуль содержит класс отображающий окно поверх всех окон.
"""
__author__ = 'prospero78'

from pak_pc.pak_gui.pak_widgets.mod_win import ClsWin

class ClsTopWin(ClsWin):
    """
    Класс созаёт окно поверх всех окон.
    """

    def __init__(self, title='ClsWinTop'):
        """
        Создаёт класс окна для показа поверх всех окон.
        :type title: string
        :param title:
        """
        self.title_txt = title
        ClsWin.__init__(self, title=self.title_txt)

    def show(self):
        """
        Показать окно.
        :return:
        """
        ClsWin.show(self)
        self.grab_set()
        self.wait_window()
