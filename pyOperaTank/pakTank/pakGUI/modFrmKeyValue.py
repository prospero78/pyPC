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
        
        self.__key=key
        self.__value=value
        
        self.__lblKey = Label(master=self, text=key)
        self.__lblKey.pack(side='left', fill='x')
        
        self.__entValue = Entry(master=self)
        self.__entValue.pack(side='right')
        self.__entValue.insert(0, value)
    
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
