# -*- coding: utf8 -*-
'''
Инициализация пакета виджета выбора диска.
'''

from Tkinter import Frame, Label, Button
from tkFileDialog import askopenfilename

class clsFrmDiskSelect(Frame):
    def __init__(self, master=None, root=None, text='Disk-0:', path='./data/default.dsk'):
        def create_self():
            def open_disk(event=''):
                d=askopenfilename(defaultextension='.dsk',
                        initialfile='./data/default.dsk',
                        filetypes=[('Disk images','.dsk'),],
                        title='Open disk image...')
                self.root.GUI.winIDC.lift()
                self.root.GUI.winIDC.focus_get()
            Frame.__init__(self, master=self.master)
            self.pack(side='top', fill='x')
            
            self.lblPath=Label(self, text=self.text, border=2, relief='raised')
            self.lblPath.pack(side='left')
            
            self.lblDiskPath=Label(self, text=self.path, anchor='w', border=2, relief='groove')
            self.lblDiskPath.pack(side='left', fill='both', expand=1)
            
            self.btnCreate=Button(self, text='Create')
            self.btnCreate.pack(side='left')
            
            self.btnOpen=Button(self, text=self.root.Res.winIDC_open, command=open_disk)
            self.btnOpen.pack(side='left')
            
            self.btnClear=Button(self, text='Clear')
            self.btnClear.pack(side='left')
            
            
        self.root=root
        self.master=master
        self.path=path
        self.text=text
        create_self()
