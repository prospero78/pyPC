# -*- coding: utf8 -*-
'''
Инициализация класса графики.
'''

class ClsGUI:
    def __init__(self, root=None):
        self.root=root
        # импорт главного класса окна
        from pak_win_main.mod_win_main import ClsWinMain
        self.winMain=ClsWinMain(root=self.root)
        
        # импорт окна "О программе"
        from pak_win_about.mod_win_about import clsWinAbout
        self.winAbout=clsWinAbout(root=self.root)
        
        # импорт окна лицензии
        from pak_win_license.mod_win_license import clsWinLicense
        self.winLicense=clsWinLicense(root=self.root)
        
        # импорт окна экрана виртуального компьютера
        from pakWinScreen.mod_win_screen import ClsWinScreen
        self.winScreen=ClsWinScreen(root=self.root)
        
        # импорт окна для создания нового диска
        from pakWinCreateDisk.mod_win_create_disk import clsWinCreateDisk
        self.winCreateDisk=clsWinCreateDisk(root=self.root)
        
        # импорт окна создания/монтирования дисков (IDC)
        from pakWinIDC.mod_win_idc import clsWinIDC
        self.winIDC=clsWinIDC(root=self.root)
        
        # импорт окна редактирования настроек регистра программного прерывания (winBP)
        from pakWinEditBP.modWinEditBP import clsWinEditBP
        self.winEditBP=clsWinEditBP(root=self.root)
        
        
    def run(self):
        '''
        Класс загружает графику, должен запускаться последним!!!
        '''
        # запуск бесконечной петли
        self.winMain.begin()
        pass
