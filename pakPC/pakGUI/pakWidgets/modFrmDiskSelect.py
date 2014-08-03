# -*- coding: utf8 -*-
'''
Инициализация пакета виджета выбора диска.
'''

from Tkinter import Frame, Label, Button

class clsFrmDiskSelect(Frame):
    def __init__(self, root=None, text='Disk-0:', path='./data/default.dsk'):
        def create_self():
            Frame.__init__(self, master=self.root)
            self.pack(side='top', fill='x')
            
            self.lblPath=Label(self, text=self.text, border=2, relief='raised')
            self.lblPath.pack(side='left')
            
            self.lblDiskPath=Label(self, text=self.path, anchor='w', border=2, relief='groove')
            self.lblDiskPath.pack(side='left', fill='x', expand=1)
            
            self.btnCreate=Button(self, text='Create')
            self.btnCreate.pack(side='left')
            
            self.btnOpen=Button(self, text='Open')
            self.btnOpen.pack(side='left')
            
            self.btnClear=Button(self, text='Clear')
            self.btnClear.pack(side='left')
            
            
        self.root=root
        self.path=path
        self.text=text
        create_self()
