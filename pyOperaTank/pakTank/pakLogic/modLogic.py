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
        # --- обновления по своему танку ---
        my_tank = self.winMain.frmLeft.lfrMyTank
        my_tank.kvAtak.entValue.delete(0, 'end')
        my_tank.kvAtak.entValue.insert(0, self.dbData.my_tank['atak'])
        
        my_tank.kvBron.entValue.delete(0, 'end')
        my_tank.kvBron.entValue.insert(0, self.dbData.my_tank['bron'])
        
    def run(self):
        """
        Выполняется при запуске всей программы.
        """
        self.dbData = self.root.dbData
        self.winMain = self.root.winMain
        
        self.update_gui()
        
        self.winMain.mainloop()
        self.dbData.close_base()
    
    def stop(self):
        """
        Выполняется при остановке всей программы.
        По окончании работы графики сохраняет базу данных.
        """
        pass
