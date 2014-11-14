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
        
    def load_oper_data(self):
        """
        Загружает оперативные данные из модуля базы данных.
        Работает при старте системы.
        """
        self.myTank.atak = self.dbData.myTank['atak']
        
    def update_gui(self):
        """
        Обновляет изменяемые данные в гуе.
        """
        # --- обновления по своему танку ---
        my_tank = self.winMain.frmLeft.lfrMyTank
        my_tank.kvAtak.value = self.myTank.atak
        my_tank.kvBron.value = self.myTank.bron
        my_tank.kvToch.value = self.myTank.toch
        my_tank.kvProch.value = self.myTank.proch
        my_tank.kvMosh.value = self.myTank.mosh
        
        tank1 = self.winMain.frmRight.lfrTank1
        tank1.kvAtak.value = self.Tank1.atak
        tank1.kvBron.value = self.Tank1.bron
        tank1.kvToch.value = self.Tank1.toch
        tank1.kvProch.value = self.Tank1.proch
        tank1.kvMosh.value = self.Tank1.mosh
        
        tank2 = self.winMain.frmRight.lfrTank2
        tank2.kvAtak.value = self.Tank2.atak
        tank2.kvBron.value = self.Tank2.bron
        tank2.kvToch.value = self.Tank2.toch
        tank2.kvProch.value = self.Tank2.proch
        tank2.kvMosh.value = self.Tank2.mosh
        
    def run(self):
        """
        Выполняется при запуске всей программы.
        """
        self.dbData = self.root.dbData
        self.winMain = self.root.winMain
        self.myTank = self.root.myTank
        self.Tank1 = self.root.Tank1
        self.Tank2 = self.root.Tank2
        
        self.load_oper_data()
        self.update_gui()
        
        self.winMain.mainloop()
        self.dbData.close_base()
    
    def stop(self):
        """
        Выполняется при остановке всей программы.
        По окончании работы графики сохраняет базу данных.
        """
        pass
