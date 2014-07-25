# -*- coding: utf8 -*-
'''
Инициализация класса графики.
'''

class clsGUI:
    def __init__(self, root=None):
        self.root=root
        
    def run(self):
        '''
        Класс загружает графику, должен запускаться последним!!!
        '''
        # импорт главного класса окна
        from pakWinMain.modWinMain import clsWinMain
        self.winMain=clsWinMain(root=self.root)
        
        # импорт окна "О программе"
        from pakWinAbout.modWinAbout import clsWinAbout
        self.winAbout=clsWinAbout(root=self.root)
        
        # импорт окна лицензии
        from pakWinLicense.modWinLicense import clsWinLicense
        self.winLicense=clsWinLicense(root=self)
        
        # запуск бесконечной петли
        self.winMain.begin()
        pass
