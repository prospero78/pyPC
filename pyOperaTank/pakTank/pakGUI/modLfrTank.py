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
                 tank=None):
        LabelFrame.__init__(self,
                            master=root,
                            text = label,
                            border=3,
                            relief='raised',
                            font='Consolas 12 bold')
        self.pack(side='top', fill='y')
        
        self.kvAtak = clsFrmKeyValue(root=self, key='Атака', value=tank.atak)
        self.kvBron = clsFrmKeyValue(root=self, key='Броня', value=tank.bron)
        self.kvBron = clsFrmKeyValue(root=self, key='Точность', value=tank.toch)
        self.kvBron = clsFrmKeyValue(root=self, key='Прочность', value=tank.proch)
        self.kvMosh = clsFrmKeyValue(root=self, key='Мощность*', value=tank.name)
