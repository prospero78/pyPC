# -*- coding: utf8 -*-
"""
Главный класс для расчёта танковых баталий.
"""

class clsOperaTank(object):
    """
    Это корневой сводный объект для создания взаимных связей между
    частями программы.
    """
    def __init__(self):
        """
        Инициализация программы.
        """
        from pakTank.modTank import clsTank
        self.my_tank = clsTank()
        self.tank1 = clsTank()
        self.tank2 = clsTank()
        
        from pakTank.pakGui.modWinMain import clsWinMain
        self.winMain = clsWinMain()
        
    def run(self):
        self.winMain.mainloop()
