# -*- coding: utf8 -*-
"""
Правый фрейм с чужими танками и всякими измерялками.
"""

from Tkinter import Frame

from pakTank.pakGUI.modLfrTank import clsLfrTank

class clsFrmRight(Frame):
    """
    Правый фрейм содержит всякие расчётные данные по чужим танкам.
    """
    def __init__(self, root=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='right', fill='y')
        self.lfrTank1 = clsLfrTank(root=self, label = 'Противник 1')
        self.lfrTank2 = clsLfrTank(root=self, label = 'Противник 2')
