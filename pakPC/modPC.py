# -*- coding: utf8 -*-
'''
Главный класс для работы pyPC.
'''

class clsPC:
    '''
    Класс реализует логику работы всей системы.
    '''
    def __init__(self, arg=None):
        # импорт класса ресурсов
        from pakPC.pakResurs.modResurs import clsRes
        self.Res = clsRes(root=self, lang='ru', arg=arg)

        # импорт класса видеокарты
        from pakPC.pakCPU.pakVideo.modVideo import clsVideo
        self.Video = clsVideo()

        # импорт клаcса центрального процессора
        from pakPC.pakCPU.modCPU import clsCPU
        self.CPU = clsCPU(max_value=self.Res.max_reg_val,
                          max_adr=self.Res.max_adr,
                          vcom=self.Video.vcom,
                          vinfo=self.Video.vinfo)

        # импорт класса общей логики
        from pakPC.pakLogic.modLogic import clsLogic
        self.Logic = clsLogic(root=self)

        # импорт класса контроллера
        from pakPC.pakController.modController import clsController
        self.Control = clsController(root=self)

        # импорт класса графики
        from pakPC.pakGUI.modGUI import clsGUI
        self.GUI = clsGUI(root=self)

        # импорт класса интерфейса дискового кластера
        from pakPC.pakIDC.modIDC import clsIDC
        self.IDC = clsIDC(root=self)

    def run(self):
        '''
        Запускает главный цикл изменений.
        '''
        self.Control.run()
        return 0
