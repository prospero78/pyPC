# -*- coding: utf8 -*-
'''
Класс окна "Лицензия".
'''

from Tkinter import Toplevel, Frame, Button, Scrollbar, Text

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
        
        def create_frmUp():
            self.frmUp=Frame(self, border=3, relief='groove')
            self.frmUp.pack(fill='both', expand=1, side='top')
            
            self.scbLicense=Scrollbar(self.frmUp)
            self.scbLicense.pack(side='right', fill='y')
            
            self.txtLicense=Text(self.frmUp, height=12, width=30, font='Courier 9')
            self.txtLicense.pack(fill='both', expand=1, side='left')
            self.txtLicense.insert('end', self.root.Res.winLicense_locale)
            
            self.scbLicense.config(command=self.txtLicense.yview)
            self.txtLicense.config(yscrollcommand=self.scbLicense.set)
        self.root=root
        create_self()
        create_frmBtn()
        create_frmUp()
        
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