# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Toplevel

class clsWinAbout(Toplevel):
    def __init__(self, root=None):
        self.root=root
        Toplevel.__init__(self)
        self.state('withdrawn')
        self.title('About')
        
    def show(self):
        self.state('normal')
        
    def destroy(self):
        self.state('withdrawn')
