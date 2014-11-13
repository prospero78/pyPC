# -*- coding: utf8 -*-
"""
Фрейм отображающий пару "ключ:значение".
"""

from Tkinter import Frame, Label, Entry

class clsFrmKeyValue(Frame):
    """
    Класс обеспечивает пару "ключ:значение"
    """
    def __init__(self, root=None, key='key', value='None'):
        Frame.__init__(self, master=root, border=3, relief='groove')
        self.pack(side='top', fill='x')
        
        self.key=key
        self.value=value
        
        self.lblKey = Label(master=self, text=key)
        self.lblKey.pack(side='left', fill='x')
        
        self.entValue = Entry(master=self)
        self.entValue.pack(side='right')
        self.entValue.insert(0, value)
