# -*- coding: utf8 -*-
'''
Инициализация пакета виджета выбора диска.
'''

from Tkinter import Frame, Label, Button
from tkFileDialog import askopenfilename

class ClsFrmDiskSelect(Frame):
    def __init__(self,
                master=None,
                root=None,
                text='Disk-0:',
                path='./data/default.dsk'):
        def create_self():
            def open_disk(event=''):
                d=askopenfilename(defaultextension='.dsk',
                        initialfile='./data/default.dsk',
                        filetypes=[('Disk images','.dsk'),],
                        title=self.root.res.winIDC_OpenDiskImage)
                self.root.gui.win_idc.lift()
                self.root.gui.win_idc.focus_get()
            Frame.__init__(self, master=self.master)
            self.pack(side='top', fill='x')
            
            self.lblPath=Label(self, text=self.text, border=2, relief='raised')
            self.lblPath.pack(side='left')
            
            self.lblDiskPath=Label(self, text=self.path, anchor='w', border=2, relief='groove')
            self.lblDiskPath.pack(side='left', fill='both', expand=1)
            
            self.btnCreate=Button(self, text=self.lang['win_idc_image_create'], command=self.root.control.create_disk)
            self.btnCreate.pack(side='left')
            
            self.btnOpen=Button(self, text=self.lang['win_idc_open'], command=open_disk)
            self.btnOpen.pack(side='left')
            
            self.btnClear=Button(self, text=self.lang['win_idc_image_unpath'])
            self.btnClear.pack(side='left')
            
            
        self.root=root
        self.lang=root.res.lang_str.lang_dict
        self.master=master
        self.path=path
        self.text=text
        create_self()
