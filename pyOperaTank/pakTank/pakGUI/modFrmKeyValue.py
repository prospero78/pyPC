# -*- coding: utf8 -*-
"""
Фрейм отображающий пару "ключ:значение".
"""

from Tkinter import Frame, Label, Entry, Button

class clsFrmKeyValue(Frame):
    """
    Класс обеспечивает пару "ключ:значение"
    """
    def __init__(self, root=None, key='key', value='None', clb=None):
        Frame.__init__(self, master=root, border=3, relief='groove')
        self.pack(side='top', fill='both', expand=1)
        
        self.__key=key
        self.__value=value
        self.callback = clb
        
        self.__lblKey = Label(master=self, text=key, anchor='e')
        self.__lblKey.pack(side='left', fill='x', expand=1)
        
        self.__entValue = Entry(master=self, width=5)
        self.__entValue.after(100, self.__control_change)
        self.__entValue.pack(side='left')
        self.__entValue.insert(0, value)
        
        self.__btnReset = Button(self, text='R', border=4, relief='groove', fg='blue', command=self.__btnReset_click)
        self.__btnReset.pack(side='left')
        
        self.__btnSave = Button(self, text='S', border=4, relief='groove', fg='blue', command=self.__btnSave_click, state='disabled')
        self.__btnSave.pack(side='left')
    
    def __btnSave_click(self, event=None):
        """
        При нажатии на кнопку сохранить происходит сохранение в файл.
        """
        txt = self.__entValue.get()
        self.__value = txt
        self.callback()
        self.__btnSave['fg'] = 'blue'
        self.__btnSave['state'] = 'disabled'
        
    def __btnReset_click(self, event=None):
        """
        При нажатии на кнопку сброс происходит сброс значения value.
        """
        self.__entValue.delete(0, 'end')
        self.__entValue.insert(0, self.__value)
    
    def __control_change(self):
        """
        Процедурка фиксрует изменения в поле ввода.
        """
        txt = self.__entValue.get()
        if txt != str(self.__value):
            self.__btnReset['fg'] = 'red'
            self.__btnSave['fg'] = 'red'
            self.__btnSave['state'] = 'normal'
        else:
            self.__btnReset['fg'] = 'blue'
            self.__btnSave['fg'] = 'blue'
            self.__btnSave['state'] = 'disabled'
        self.__entValue.after(100, self.__control_change)
    
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
