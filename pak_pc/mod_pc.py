# -*- coding: utf8 -*-
"""
Главный класс для работы pyPC.
"""

__version__ = 5

class ClsPC(object):
    """
    Класс реализует логику работы всей системы.
    """

    def __init__(self, arg=None):
        """
        Создание главного класса-приложения.
        :param arg: параметры командной строки.
        """
        # импорт класса ресурсов
        from pak_pc.pak_resurs.mod_resurs import ClsRes

        self.res = ClsRes(root=self, lang='ru', arg=arg)

        # импорт класса видеокарты
        #from pak_pc.pak_cpu.pak_video.mod_video import ClsVideo

        #self.video = ClsVideo()

        # импорт клаcса центрального процессора
        from pak_pc.pak_cpu.mod_cpu import ClsCPU

        self.cpu = ClsCPU()

        # импорт класса общей логики
        from pak_pc.pak_logic.mod_logic import ClsLogic

        self.logic = ClsLogic(root=self)

        # импорт класса контроллера
        from pak_pc.pak_controller.mod_controller import ClsController

        self.__control = ClsController(root=self)

        # импорт класса графики
        from pak_pc.pak_gui.mod_gui import ClsGUI

        self.gui = ClsGUI(root=self)

        # импорт класса интерфейса дискового кластера
        from pak_pc.pak_idc.mod_idc import ClsIDC

        self.idc = ClsIDC(root=self)

    @property
    def control(self):
        """
        Возвращает ссылку на контроллер програмы.
        """
        return self.__control

    def run(self):
        """
        Запускает главный цикл изменений.
        """
        self.control.run()
        return 0
