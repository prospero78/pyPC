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
        from pak_pc.pak_resurs.mod_resurs import ClsRes
        self.res = ClsRes(root=self, lang='ru', arg=arg)

        # импорт класса видеокарты
        from pak_pc.pak_cpu.pak_video.mod_video import ClsVideo
        self.video = ClsVideo()

        # импорт клаcса центрального процессора
        from pak_pc.pak_cpu.mod_cpu import ClsCPU
        self.cpu = ClsCPU(vcom=self.video.vcom,
                          vinfo=self.video.vinfo)

        # импорт класса общей логики
        from pak_pc.pak_logic.mod_logic import clsLogic
        self.logic = clsLogic(root=self)

        # импорт класса контроллера
        from pak_pc.pak_controller.mod_controller import clsController
        self.control = clsController(root=self)

        # импорт класса графики
        from pak_pc.pak_gui.mod_gui import ClsGUI
        self.gui = ClsGUI(root=self)

        # импорт класса интерфейса дискового кластера
        from pak_pc.pak_idc.mod_idc import clsIDC
        self.idc = clsIDC(root=self)

    def run(self):
        '''
        Запускает главный цикл изменений.
        '''
        self.control.run()
        return 0
