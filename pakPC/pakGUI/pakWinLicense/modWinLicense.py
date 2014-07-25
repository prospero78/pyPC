# -*- coding: utf8 -*-
'''
Класс окна "Лицензия".
'''

from Tkinter import Toplevel

class clsWinLicense(Toplevel):
    def __init__(self, root=none):
        Toplevel.__init__(self)
        self.title('License')
