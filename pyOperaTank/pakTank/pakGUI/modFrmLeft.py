# -*- coding: utf8 -*-
"""
Левый фрейм со своим танком и всякими измерялками.
"""

from Tkinter import Frame

from pakTank.pakGUI.modLfrTank import clsLfrTank

class clsFrmLeft(Frame):
    """
    Левый фрейм содержит всякие расчётные данные по своему танку.
    """
    def __init__(self,
                 root=None,
                 my_tank=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='left', fill='y')
        self.lfrMyTank = clsLfrTank(root=self,
                                    label = 'Мой танк',
                                    tank=my_tank)
        self.lfrMyTank.kvVer1 = ClsKeyValue(root=self.lfrMyTank,
                                            key='Вероятность 1*',
                                            value='?')
        self.lfrMyTank.kvVer2 = ClsKeyValue(root=self.lfrMyTank,
                                            key='Вероятность 2*',
                                            value='?')
