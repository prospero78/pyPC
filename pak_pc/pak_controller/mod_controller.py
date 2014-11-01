# -*- coding: utf8 -*-
"""
Главный класс контроллера
"""


class ClsController(object):
    """
    Класс обеспечивает связь логики программы и графического интерфейса
    пользователя.
    :param root:
    """

    def __init__(self, root=None):
        """
        Инициализация класса.
        Создание всех переменных, которые только могут встречаться.
        :param root: ссылка на корневой класс.
        """
        self.root = root
        # ссылка на класс графики. Будет присвоена позже.
        self.gui = None
        # ссылка на класс логики. Будет создана позже.
        self.logic = None

    def reset_pc(self, event=None):
        """
        Вызывается при сбросе виртуального компьютера.
        :param event: событие при сбросе состояния виртуальной машины.
        """
        print '.ClsController.reset_pc()'
        self.logic.reset_pc()

    def win_edit_bp_hide(self, event=''):
        # print  '.ClsController.win_edit_bp_hide()'
        """
        Вызывается при скрытии окна настроек регистра программного прерывания.
        :param event: событие при скрытии окна редактирования свойств
        регистра программного прерывания.
        """
        self.logic.win_edit_bp_hide()

    def show_win_edit_bp(self, event=''):
        # print  '.ClsController.show_win_edit_bp()'
        """
        Вызывается при показе окна редактирования свойств регистра
        программной отладки ВР.
        :param event: событие при показе окна регистра программного прерывания.
        """
        self.logic.show_win_edit_bp()

    def win_main_debug(self, event=''):
        # print  '.ClsController.win_main_debug()'
        """
        Вызывается при запуске виртуальной машины в режиме отладки.
        :param event: событие при запуске машины в режиме отладки.
        """
        self.logic.debug_CPU()

    def win_main_step_cpu(self, event=''):
        # print  '.ClsController.win_main_step_cpu()'
        self.logic.step_cpu()

    def win_create_disk_ok(self, event=''):
        # print '.ClsController.win_create_disk_ok()'
        self.logic.generate_new_disk()

    def create_new_disk(self, event=None):
        # print '.ClsController.create_new_disk()'
        self.logic.create_new_disk()

    def win_idc_ok(self, event=None):
        # print '.ClsController.win_idc_ok()'
        """
        Вызывается при закрытии окна интерфейса дискового интерфейса.
        :param event: событие при закрытии окна интерфейса дискового
        кластера.
        """
        self.gui.win_idc.destroy()

    def win_idc_cancel(self, event=None):
        # print '.ClsController.win_idc_cancel()'
        """
        Вызывается при отмене действий в окне интерфейса дискового кластера.
        :param event: событие при отмене показа окна интерфейса дискового
        кластера.
        """
        self.gui.win_idc.destroy()

    def create_disk(self, event=None):
        # print '.ClsController.create_disk()'
        """
        Вызывается при создании нового виртуального диска из окна
        интерфейса дискового кластера.
        :param event: событие при создании нового диска.
        """
        self.logic.create_disk()

    def show_screen(self, event=None):
        # print '.ClsController.show_screen()'
        self.logic.show_screen()

    def run(self, event=None):
        """
        Вызывается при запуске всей системы.
        :param event: событие при запуске всей системы.
        """
        self.gui = self.root.gui
        self.logic = self.root.logic
        self.cpu = self.root.cpu
        # print '.ClsController.run()'
        self.logic.run()

    def about(self, event=None):
        # print 'about()'
        """
        Вызывается при показе окна "О программе"
        :param event: событие при показе окна о программе.
        """
        self.root.gui.win_about.show()

    def exit(self, event=None):
        # print '.ClsController.exit()'
        """
        Вызывает выход из всей программы.
        :param event: событие при закрытии главного окна.
        """
        self.root.logic.exit()

    def show_win_license(self, event=None):
        """
        :param event: событие при показе окна лицензии.
        """
        self.root.logic.show_win_license()

    def hide_win_license(self, event=None):
        """
        Вызывается при скрытии окна показа лицензии.
        :param event:  событие при скрытия окна показа лицензии.
        """
        self.root.logic.hide_win_license()

    def show_win_idc(self, event=None):
        """
        :type event: object
        :param event: передаётся из события показа окна интерфейса дискового
        кластера.
        """
        self.root.logic.show_win_idc()
