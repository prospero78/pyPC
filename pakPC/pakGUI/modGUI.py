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
        # импорт глвного класса окна
        from pakWinMain.modWinMain import clsWinMain
        self.winMain=clsWinMain(root=self.root)
        # запуск беконечной петли
        self.winMain.begin()
        pass
