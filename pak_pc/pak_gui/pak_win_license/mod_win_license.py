# -*- coding: utf8 -*-
'''
Класс окна "Лицензия".
'''

from Tkinter import Toplevel, Frame, Button, Scrollbar, Text

class clsWinLicense(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.title(self.lang['win_license_title'])
            self.minsize(350,240)
            self.state('withdrawn')
       
        def create_frmBtn():
            def btnEngLic_click(event=None):
                self.txtLicense.delete('1.0', 'end')
                self.txtLicense.insert('end',self.root.res.winLicense_eng)
            
            def btnLocalsLic_click(event=None):
                self.txtLicense.delete('1.0', 'end')
                self.txtLicense.insert('end',self.root.res.winLicense_locale)
                
            self.frm_btn=Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')
            
            self.btnEngLicence=Button(self.frm_btn, text='England', bg='gray', command=btnEngLic_click)
            self.btnEngLicence.pack(side='left')
            
            self.btn_local_license=Button(self.frm_btn, text=self.lang['win_license_btn_local_text'], bg='gray', command=btnLocalsLic_click)
            self.btn_local_license.pack(side='left')
            
            self.btnClose=Button(self.frm_btn, text='Close', bg='gray', command=self.destroy)
            self.btnClose.pack(side='right')
        
        def create_frmUp():
            self.frmUp=Frame(self, border=3, relief='groove')
            self.frmUp.pack(fill='both', expand=1, side='top')
            
            self.scbLicense=Scrollbar(self.frmUp)
            self.scbLicense.pack(side='right', fill='y')
            
            self.txtLicense=Text(self.frmUp, height=12, width=30, font='Courier 9')
            self.txtLicense.pack(fill='both', expand=1, side='left')
            self.txtLicense.insert('end', self.lang['win_license_locale'])
            
            self.scbLicense.config(command=self.txtLicense.yview)
            self.txtLicense.config(yscrollcommand=self.scbLicense.set)
            
        self.root=root
        self.lang=root.res.lang_str.lang_dict
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
        self.root.control.hide_winLicense()
    
    def win_exit(self):
        self.destroy()
