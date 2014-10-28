# -*- coding: utf8 -*-
'''
Главный класс для работы pyPC.
'''

class ClsPC(object):
    '''
    Класс реализует логику работы всей системы.
    '''
    def __init__(self, arg=None):
        # импорт класса ресурсов
        from pakPC.pakResurs.modResurs import ClsRes
        self.res = ClsRes(root=self, lang='ru', arg=arg)

        # импорт класса видеокарты
        from pakPC.pakCPU.pakVideo.modVideo import clsVideo
        self.video = clsVideo()

        # импорт клаcса центрального процессора
        from pakPC.pakCPU.modCPU import clsCPU
        self.cpu = clsCPU(max_value=self.res.max_reg_val,
                          max_adr=self.res.max_adr,
                          vcom=self.video.vcom,
                          vinfo=self.video.vinfo)

        # импорт класса общей логики
        from pakPC.pakLogic.modLogic import clsLogic
        self.logic = clsLogic(root=self)

        # импорт класса контроллера
        from pakPC.pakController.modController import clsController
        self.control = clsController(root=self)

        # импорт класса графики
        from pakPC.pakGUI.modGUI import clsGUI
        self.gui = clsGUI(root=self)

        # импорт класса интерфейса дискового кластера
        from pakPC.pakIDC.modIDC import clsIDC
        self.idc = clsIDC(root=self)

    def run(self):
        '''
        Запускает главный цикл изменений.
        '''
        self.control.run()
        return 0
