# -*- coding: utf8 -*-
"""
Правый фрейм с чужими танками и всякими измерялками.
"""

from Tkinter import Frame

class clsFrmRight(Frame):
    """
    Правый фрейм содержит всякие расчётные данные по чужим танкам.
    """
    def __init__(self, root=None, tank1=None, tank2=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='right', fill='y')
        self.lfrTank1 = ClsLfrTank(root=self, label = 'Противник 1', tank=tank1)
        self.lfrTank2 = ClsLfrTank(root=self, label = 'Противник 2', tank=tank2)
