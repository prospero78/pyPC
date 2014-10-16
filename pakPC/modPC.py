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
        
        # импорт клаcса центрального процессора
        from pakCPU.modCPU import clsCPU
        self.CPU=clsCPU(root=self)
        self.CPU.start()
        
        # импорт класса общей логики
        from pakLogic.modLogic import clsLogic
        self.Logic=clsLogic(root=self)
        
        # импорт класса контроллера
        from pakController.modController import clsController
        self.Control=clsController(root=self)
        
        # импорт класса графики
        from pakGUI.modGUI import clsGUI
        self.GUI=clsGUI(root=self)
        
        # импрот класса видеокарты
        from pakVideo.modVideo import clsVideo
        self.Video=clsVideo(root=self)
        
        # импорт класса интерфейса дискового кластера
        from pakIDC.modIDC import clsIDC
        self.IDC=clsIDC(root=self)
        
        
        
    def run(self):
        '''
        Запускает главный цикл изменений.
        '''
        self.Control.run()
        return 0
