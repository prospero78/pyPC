# -*- coding: utf8 -*-
'''
Класс окна интерфейса дискового кластера.
'''

from Tkinter import Toplevel, Frame, Button, Label

from pak_pc.pak_gui.pak_widgets.mod_frm_disk_select import clsFrmDiskSelect

class ClsWinIDC(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.lang['win_idc_name'])
            self.minsize(350, 200)
        
        def create_frmBtn():
            self.frm_btn=Frame(self, border=2, relief='sunken')
            self.frm_btn.pack(side='bottom', fill='x')
            
            self.btnCancel=Button(self.frm_btn, text=self.lang['win_idc_cancel'], command=self.root.control.winIDC_cancel)
            self.btnCancel.pack(side='right')
            
            self.btnReset=Button(self.frm_btn, text=self.lang['win_idc_reset'])
            self.btnReset.pack(side='right')
            
            self.btn_ok=Button(self.frm_btn, text=' Ok ', command=self.lang['win_idc_ok'])
            self.btn_ok.pack(side='right')
            
        def create_frmIDC():
            self.frm_idc=Frame(self, border=2, relief='sunken')
            self.frm_idc.pack(side='top', fill='both', expand=1)
            
            self.frmDisk0=clsFrmDiskSelect(master=self.frm_idc, root=self.root, text='Disk-0:')
            self.frmDisk1=clsFrmDiskSelect(master=self.frm_idc, root=self.root, text='Disk-1:', path='None')
            self.frmDisk2=clsFrmDiskSelect(master=self.frm_idc, root=self.root, text='Disk-2:', path='None')
            self.frmDisk3=clsFrmDiskSelect(master=self.frm_idc, root=self.root, text='Disk-3:', path='None')
            
        self.root=root
        self.lang=root.res.lang_str.lang_dict
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
        
    def win_exit(self):
        self.destroy()
