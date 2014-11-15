# -*- coding: utf8 -*-
"""
Фрейм отображающий базовый класс танка.
"""

from Tkinter import LabelFrame

from pakTank.pakGUI.modFrmKeyValue import clsFrmKeyValue

class clsLfrTank(LabelFrame):
    """
    Класс создаёт фрейм для редактирования характеристик танка.
    """
    def __init__(self, root=None,
                 label='MyTank',
                 clb=None):
        LabelFrame.__init__(self,
                            master=root,
                            text = label,
                            border=3,
                            relief='raised',
                            font='Consolas 12 bold')
        self.pack(side='top', fill='x')
        
        self.kvAtak = clsFrmKeyValue(root=self, key='Атака', value=0, clb=clb)
        self.kvBron = clsFrmKeyValue(root=self, key='Броня', value=0, clb=clb)
        self.kvToch = clsFrmKeyValue(root=self, key='Точность', value=0, clb=clb)
        self.kvProch = clsFrmKeyValue(root=self, key='Прочность', value=0, clb=clb)
        self.kvMosh = clsFrmKeyValue(root=self, key='[Мощность]', value=0, clb=clb)
