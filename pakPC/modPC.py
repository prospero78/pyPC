# -*- coding: utf8 -*-
'''
Главный класс для работы pyPC.
'''

class clsPC:
    '''
    Класс реализует логику работы всей системы.
    '''
    def __init__(self, arg=[]):
        # импорт класса ресурсов
        from pakResurs.modResurs import clsRes
        self.Res=clsRes(root=self, lang='ru', arg=arg)
        
        # импорт класса графики
        from pakGUI.modGUI import clsGUI
        self.GUI=clsGUI(root=self)
        
        # импорт клаcса центрального процессора
        from pakCPU.cmodCPU import clsCPU
        pass
        
    def run(self):
        '''
        Запускает главный цикл изменений.
        '''
        self.GUI.run()
        return 0
