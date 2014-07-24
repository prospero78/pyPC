# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Toplevel, Frame, Button

class clsWinAbout(Toplevel):
    def __init__(self, root=None):
        def create_self():
            self.root=root
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.root.Res.winAbout_name)
            self.minsize(300, 200)
        
        def create_frmUp():
            self.frmUp=Frame(self, border=3, relief='groove')
            self.frmUp.pack(fill='both', expand=1, side='top')
        
        def create_frmBtn():
            self.frmBtn=Frame(self, border=3, relief='raised')
            self.frmBtn.pack(side='bottom', fill='x')
            
            self.btnCloseAbout=Button(self.frmBtn, text='Close About', bg='gray', command=self.destroy)
            self.btnCloseAbout.pack(side='right')
        
        
        create_self()
        create_frmUp()
        create_frmBtn()
        
        
        
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
        
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
