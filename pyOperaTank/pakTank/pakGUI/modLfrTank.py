# -*- coding: utf8 -*-
"""
Фрейм отображающий базовый класс танка.
"""

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
        
        self.kvAtak = ClsKeyValue(root=self, key='Атака', value=tank[0])
        self.kvBron = ClsKeyValue(root=self, key='Броня', value=tank[1])
        self.kvBron = ClsKeyValue(root=self, key='Точность', value=tank[2])
        self.kvBron = ClsKeyValue(root=self, key='Прочность', value=tank[3])
        self.kvMosh = ClsKeyValue(root=self, key='Мощность*', value='?')
