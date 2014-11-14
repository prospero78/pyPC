# -*- coding: utf8 -*-
"""
Модуль для танковой логики.
"""

class clsLogic(object):
    """
    Класс предоставляет логику приложения для правильной работы.
    """
    def __init__(self, root=None):
        """
        Создание экземпляра класса танковой логики.
        """
        self.root = root
        
    def update_gui(self):
        """
        Обновляет изменяемые данные в гуе.
        """
        
        
    def run(self):
        """
        Выполняется при запуске всей программы.
        """
        self.update_gui()
        self.winMain = self.root.winMain
        self.dbData = self.root.dbData
        self.winMain.mainloop()
        self.dbData.close_base()
    
    def stop(self):
        """
        Выполняется при остановке всей программы.
        По окончании работы графики сохраняет базу данных.
        """
        pass
