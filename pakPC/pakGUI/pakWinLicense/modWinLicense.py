# -*- coding: utf8 -*-
'''
Класс окна "Лицензия".
'''

from Tkinter import Toplevel, Frame, Button

class clsWinLicense(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.title(self.root.Res.winLicense_title)
            self.minsize(350,240)
            self.state('withdrawn')
       
        def create_frmBtn():
            self.frmBtn=Frame(self, border=3, relief='raised')
            self.frmBtn.pack(side='bottom', fill='x')
            
            self.btnEngLicence=Button(self.frmBtn, text='England', bg='gray', command=self.destroy)
            self.btnEngLicence.pack(side='left')
            
            self.btnLocalLicense=Button(self.frmBtn, text='Russian', bg='gray', command=self.root.Control.show_winLicense)
            self.btnLocalLicense.pack(side='left')
        self.root=root
        create_self()
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
        self.root.Control.hide_winLicense()
