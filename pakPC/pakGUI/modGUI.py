# -*- coding: utf8 -*-
'''
Инициализация класса графики.
'''

class clsGUI:
    def __init__(self, root=None):
        self.root=root
        # импорт главного класса окна
        from pakWinMain.modWinMain import clsWinMain
        self.winMain=clsWinMain(root=self.root)
        
        # импорт окна "О программе"
        from pakWinAbout.modWinAbout import clsWinAbout
        self.winAbout=clsWinAbout(root=self.root)
        
        # импорт окна лицензии
        from pakWinLicense.modWinLicense import clsWinLicense
        self.winLicense=clsWinLicense(root=self.root)
        
        # импорт окна экрана виртуального компьютера
        from pakWinScreen.modWinScreen import clsWinScreen
        self.winScreen=clsWinScreen(root=self.root)
        
        # импорт окна создания/монтирования дисков (IDC)
        from pakWinIDC.modWinIDC import clsWinIDC
        
        
    def run(self):
        '''
        Класс загружает графику, должен запускаться последним!!!
        '''
        # запуск бесконечной петли
        self.winMain.begin()
        pass
