# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Toplevel, Frame

class clsWinAbout(Toplevel):
    def __init__(self, root=None):
        self.root=root
        Toplevel.__init__(self)
        self.state('withdrawn')
        self.title(self.root.Res.winAbout_name)
        
        self.frmUp=Frame(self, border=3, relief='groove')
        self.frmUp.pack(fill='both', expand=1, side='top')
        
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
        
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
