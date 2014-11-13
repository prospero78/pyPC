# -*- coding: utf8 -*-
"""
Фрейм для кнопок.
"""

import sys

from Tkinter import Frame, Button

class clsFrmButton(Frame):
    """
    Класс добавляет фрейм с кнопками для пересчёта значений.
    """
    def __init__(self, root=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='bottom', fill='x')
        
        self.btnExit = Button(self, text='Выход', command=lambda:(root.destroy()))
        self.btnExit.pack(side='right')
        
        self.btnCalc = Button(self, text='Пересчёт')
        self.btnCalc.pack(side='right')
