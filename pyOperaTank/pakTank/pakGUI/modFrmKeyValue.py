# -*- coding: utf8 -*-
"""
Фрейм отображающий пару "ключ:значение".
"""

from Tkinter import Frame, Label, Entry, Button

class clsFrmKeyValue(Frame):
    """
    Класс обеспечивает пару "ключ:значение"
    """
    def __init__(self, root=None, key='key', value='None'):
        Frame.__init__(self, master=root, border=3, relief='groove')
        self.pack(side='top', fill='both', expand=1)
        
        self.__key=key
        self.__value=value
        
        self.__lblKey = Label(master=self, text=key, justify='right')
        self.__lblKey.pack(side='left', fill='x', expand=1)
        
        self.__entValue = Entry(master=self, width=5)
        self.__entValue.pack(side='left')
        self.__entValue.insert(0, value)
        
        self.__btnReset = Button(self, text='R', border=4, relief='groove')
        self.__btnReset.pack(side='left')
    
    @property
    def key(self):
        return self.__key
        
    @key.setter
    def key(self, value=None):
        self.__lblKey['text'] = value
        self.__key = value
        
    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, value=None):
        self.__entValue.delete(0, 'end')
        self.__entValue.insert(0, value)
        self.__value = value
