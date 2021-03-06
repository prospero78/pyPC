# -*- coding: utf8 -*-
"""
Левый фрейм со своим танком и всякими измерялками.
"""

from Tkinter import Frame

from pakTank.pakGUI.modLfrTank import clsLfrTank
from pakTank.pakGUI.modFrmKeyValue import clsFrmKeyValue

class clsFrmLeft(Frame):
    """
    Левый фрейм содержит всякие расчётные данные по своему танку.
    """
    def __init__(self,
                 root=None,
                 clb=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='left', fill='both', expand=1)
        self.lfrMyTank = clsLfrTank(root=self,
                                    label = 'Мой танк',
                                    clb=clb)
        self.lfrMyTank.kvVer1 = clsFrmKeyValue(root=self.lfrMyTank,
                                            key='[Вероятность 1]',
                                            value=0,
                                            clb=clb)
        self.lfrMyTank.kvVer2 = clsFrmKeyValue(root=self.lfrMyTank,
                                            key='[Вероятность 2]',
                                            value=0,
                                            clb=clb)
