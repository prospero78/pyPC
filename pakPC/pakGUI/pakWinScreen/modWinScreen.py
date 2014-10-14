# -*- coding: utf8 -*-
'''
Класс окна экрана виртуального компьютера.
'''

from Tkinter import Toplevel, Frame, Button, Canvas

class clsWinScreen(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.root.Res.winScreen_title)
            self.minsize(640, 480)
        
        def create_frmScreen():
            self.frmScreen=Frame(self, border=3, relief='groove')
            self.frmScreen.pack(fill='both', expand=1, side='top')
            
            self.cnvScreen=Canvas(self.frmScreen, bg='white', width=640, height=480)
            self.cnvScreen.pack(fill='both')
        
        def create_frmBtn():
            self.frmBtn=Frame(self, border=3, relief='raised')
            self.frmBtn.pack(side='bottom', fill='x')
            
            self.btnScreenClose=Button(self.frmBtn, text=self.root.Res.winScreen_btnScreenClose_text, bg='gray', command=self.destroy)
            self.btnScreenClose.pack(side='right')
            
        
        self.root=root
        create_self()
        create_frmBtn()
        create_frmScreen()
        
        
        
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
        
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
    
    def win_exit(self):
        self.destroy()
