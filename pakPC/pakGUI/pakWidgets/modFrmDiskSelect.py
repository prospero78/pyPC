# -*- coding: utf8 -*-
'''
Инициализация пакета виджета выбора диска.
'''

from Tkinter import Frame, Label, Button

class clsFrmDiskSelect(Frame):
    def __init__(self, root=None):
        def create_self():
            Frame.__init__(self, master=self.root)
            
            self.lblPath=Label(self, text='Disk-0:', border=2, relief='raised')
            self.lblPath.pack(side='left')
            
            
            self.lblDiskPath=Label(self, text='./data/default.dsk', anchor='w', border=2, relief='groove')
            self.lblDiskPath.pack(side='left', fill='x', expand=1)
            
            self.btnCreate=Button(self, text='Create')
            self.btnCreate.pack(side='left')
            
            self.btnOpen=Button(self, text='Open')
            self.btnOpen.pack(side='left')
            
            self.pack(side='top', fill='both', expand=1)
        self.root=root
        create_self()
