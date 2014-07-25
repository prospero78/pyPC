# -*- coding: utf8 -*-
'''
Класс окна "Лицензия".
'''

from Tkinter import Toplevel

class clsWinLicense(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.title(self.root.Res.winLicense_title)
            self.minsize(350,240)
            self.state('withdrawn')
       
        self.root=root
        create_self()
        
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
    
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
        self.root.Control.hide_winLicense()
