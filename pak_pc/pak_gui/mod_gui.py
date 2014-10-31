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
        from pak_win_screen.mod_win_screen import ClsWinScreen
        self.winScreen=ClsWinScreen(root=self.root)
        
        # импорт окна для создания нового диска
        from pak_win_create_disk.mod_win_create_disk import ClsWinCreateDisk
        self.winCreateDisk=ClsWinCreateDisk(root=self.root)
        
        # импорт окна создания/монтирования дисков (IDC)
        from pak_win_idc.mod_win_idc import ClsWinIDC
        self.winIDC=ClsWinIDC(root=self.root)
        
        # импорт окна редактирования настроек регистра программного прерывания (winBP)
        from pak_win_edit_bp.mod_win_edit_bp import ClsWinEditBP
        self.winEditBP=ClsWinEditBP(root=self.root)
        
        
    def run(self):
        '''
        Класс загружает графику, должен запускаться последним!!!
        '''
        # запуск бесконечной петли
        self.winMain.begin()
        pass
