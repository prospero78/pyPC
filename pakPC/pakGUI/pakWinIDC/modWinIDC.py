# -*- coding: utf8 -*-
'''
Класс окна интерфейса дискового кластера.
'''

from Tkinter import Toplevel, Frame, Button, Label

from pakPC.pakGUI.pakWidgets.modFrmDiskSelect import clsFrmDiskSelect

class clsWinIDC(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.root.Res.winIDC_name)
            self.minsize(350, 200)
        
        def create_frmBtn():
            self.frmBtn=Frame(self, border=2, relief='sunken')
            self.frmBtn.pack(side='bottom', fill='x')
            
            self.btnCancel=Button(self.frmBtn, text='Cancel', command=self.root.Control.winIDC_cancel)
            self.btnCancel.pack(side='right')
            
            self.btnReturn=Button(self.frmBtn, text='Return')
            self.btnReturn.pack(side='right')
            
            self.btnOk=Button(self.frmBtn, text=' Ok ')
            self.btnOk.pack(side='right')
            
        def create_frmIDC():
            self.frmIDC=Frame(self, border=2, relief='sunken')
            self.frmIDC.pack(side='top', fill='both', expand=1)
            
            self.frmDisk0=clsFrmDiskSelect(master=self.frmIDC, root=self.root, text='Disk-0:')
            self.frmDisk1=clsFrmDiskSelect(master=self.frmIDC, root=self.root, text='Disk-1:', path='None')
            self.frmDisk2=clsFrmDiskSelect(master=self.frmIDC, root=self.root, text='Disk-2:', path='None')
            self.frmDisk3=clsFrmDiskSelect(master=self.frmIDC, root=self.root, text='Disk-3:', path='None')
            
        self.root=root
        create_self()
        create_frmBtn()
        create_frmIDC()
    
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
        
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
