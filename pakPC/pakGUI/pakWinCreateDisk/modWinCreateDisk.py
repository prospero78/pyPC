# -*- coding: utf8 -*-
'''
Класс окна экрана виртуального компьютера.
'''

from Tkinter import Toplevel, Frame, Button, Canvas

class clsWinCreateDisk(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.root.Res.winCreateDisk_title)
            self.minsize(350, 200)
            
        def create_frmBtn():
            self.frmBtn=Frame(self, border=2, relief='sunken')
            self.frmBtn.pack(side='bottom', fill='x')
            
            self.btnOk=Button(self.frmBtn, text=' Ok ')#, command=self.root.Control.winIDC_ok)
            self.btnOk.pack(side='right')
            
            self.btnCancel=Button(self.frmBtn, text='Cancel')#, command=self.root.Control.winIDC_cancel)
            self.btnCancel.pack(side='right')
        
        def create_frmDiskParam():
            self.frmDiskParam=Frame(self, border=2, relief='sunken')
            self.frmDiskParam.pack(side='top', fill='both', expand=1)
            
            #TODO: надо запилить виджет -- пара ключ:значение
            
        self.root=root
        create_self()
        create_frmBtn()
        create_frmDiskParam()
        
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
        
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
