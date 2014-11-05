# -*- coding: utf8 -*-
"""
Инициализация класса графики.
"""


class ClsGUI(object):
    """
    Главный класс GUI для приложения. Является точкой подключения всех
    графических ресурсов.
    """
    def __init__(self, root=None):
        """
        Импорт всех возможных окон.
        :param root:
        :return:
        """
        self.__root = root
        # импорт главного класса окна
        from pak_pc.pak_gui.pak_win_main.mod_win_main import ClsWinMain

        self.win_main = ClsWinMain(root=self.__root)

        # импорт окна "О программе"
        from pak_pc.pak_gui.pak_win_about.mod_win_about import ClsWinAbout

        self.win_about = ClsWinAbout(root=self.__root)

        # импорт окна лицензии
        from pak_pc.pak_gui.pak_win_license.mod_win_license import ClsWinLicense

        self.win_license = ClsWinLicense(root=self.__root)

        # импорт окна экрана виртуального компьютера
        from pak_pc.pak_gui.pak_win_screen.mod_win_screen import ClsWinScreen

        self.win_screen = ClsWinScreen(root=self.__root)

        # импорт окна для создания нового диска
        from pak_pc.pak_gui.pak_win_create_disk.mod_win_create_disk \
            import ClsWinCreateDisk

        self.win_create_disk = ClsWinCreateDisk(root=self.__root)

        # импорт окна создания/монтирования дисков (IDC)
        from pak_pc.pak_gui.pak_win_idc.mod_win_idc import ClsWinIDC

        self.win_idc = ClsWinIDC(root=self.__root)

        # импорт окна редактирования настроек регистра программного
        # прерывания (winBP)
        from pak_pc.pak_gui.pak_win_edit_bp.mod_win_edit_bp import ClsWinEditBP

        self.win_edit_bp = ClsWinEditBP(root=self.__root)


    def run(self):
        """
        Класс загружает графику, должен запускаться последним!!!
        """
        # запуск бесконечной петли
        self.win_main.begin()
