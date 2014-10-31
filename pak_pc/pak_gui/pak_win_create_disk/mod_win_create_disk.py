# -*- coding: utf8 -*-
'''
Класс окна экрана виртуального компьютера.
'''

from Tkinter import Toplevel, Frame, Button, Canvas
from pak_pc.pak_gui.pak_widgets.modFrmKeyValue import clsFrmKeyValue

class ClsWinCreateDisk(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.lang['win_create_disk_title'])
            self.minsize(350, 200)
            
        def create_frmBtn():
            self.frm_btn=Frame(self, border=2, relief='sunken')
            self.frm_btn.pack(side='bottom', fill='x')
            
            self.btn_ok=Button(self.frm_btn, text=' Ok ', command=self.lang['win_idc_image_create'])
            self.btn_ok.pack(side='right')
            
            self.btnCancel=Button(self.frm_btn, text='Cancel', command=self.destroy)
            self.btnCancel.pack(side='right')
        
        def create_frmDiskParam():
            self.frmDiskParam=Frame(self, border=2, relief='sunken')
            self.frmDiskParam.pack(side='top', fill='both', expand=1)
            
            #TODO: надо запилить виджет -- пара ключ:значение
            self.fkvName=clsFrmKeyValue(root=self.frmDiskParam, key='Name Disk', value='default')
            self.fkvSize=clsFrmKeyValue(root=self.frmDiskParam, key='Size Disk (kB)', value='1')
            
        self.root=root
        self.lang=root.res.lang_str.lang_dict
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
        self.root.gui.winIDC.focus_set()
        self.root.gui.winIDC.grab_set()
        
    def win_exit(self):
        self.destroy()
