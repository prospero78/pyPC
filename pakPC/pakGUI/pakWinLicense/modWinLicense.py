# -*- coding: utf8 -*-
'''
Класс окна "Лицензия".
'''

from Tkinter import Toplevel

class clsWinLicense(Toplevel):
    def __init__(self, root=None):
        self.root=root
        Toplevel.__init__(self)
        self.title(self.root.Res.winLicense_title)
