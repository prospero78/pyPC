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
        # чтение конфигурации танков
        from pakTank.pakData.modData import clsData
        self.dbData = clsData()
        
        # создание логики
        from pakTank.pakLogic.modLogic import clsLogic
        self.logic = clsLogic(root=self)
        
        # создание танков
        from pakTank.modTank import clsTank
        self.myTank = clsTank()
        self.Tank1 = clsTank()
        self.Tank2 = clsTank()
        
        
        # создание графики
        from pakTank.pakGUI.modWinMain import clsWinMain
        self.winMain = clsWinMain(clb=self.logic.save_data)
        
    def run(self):
        """
        Выполняется один раз при запуске всей программы.
        """
        self.logic.run()
