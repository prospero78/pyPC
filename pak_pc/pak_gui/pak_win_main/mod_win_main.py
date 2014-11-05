# -*- coding: utf8 -*-
"""
Инициализация класса главного окна.
"""
from Tkinter import Tk, Frame, Button, Menubutton, Menu

from pak_pc.pak_gui.pak_widgets.mod_frm_cpu import ClsFrmCPU


class ClsWinMain(Tk):
    """
    Главное окно программы.
    """
    def __init__(self, root=None):
        """
        Создание главного окна прогарммы.
        :param root:
        :return:
        """
        def create_self():
            """
            Создание самого окна.
            :return:
            """
            def create_frm_btn():
                """
                Создание кнопок на главном окне.
                :return:
                """
                # укорочение ссылки
                control = self.__root.control
                # нижний фрейм главного окна
                self.frm_btn = Frame(self, border=3, relief='sunken')
                self.frm_btn.pack(side='bottom', fil='x')

                # кнопка "шаг" главного окна
                self.btn_step = Button(self.frm_btn,
                                       text='Step >',
                                       command=control.win_main_step_cpu)
                self.btn_step.pack(side='left')

                # кнопка "Отлдака" главного окна
                self.btn_debug = Button(self.frm_btn,
                                        text='Debug >>',
                                        command=control.win_main_debug)
                self.btn_debug.pack(side='left')

                # кнопка "выход" главного окна
                self.btn_exit = Button(self.frm_btn,
                                       text='Exit [X]',
                                       command=control.exit)
                self.btn_exit.pack(side='right')

                # кнопка для показа экрана виртуального компьютера
                self.btn_show_screen = Button(self.frm_btn,
                                              text='PC Screen',
                                              command=control.show_screen)
                self.btn_show_screen.pack(side='left')

                # кнопка для сброса виртуального компьютера
                self.btn_reset = Button(self.frm_btn,
                                        text='Reset (x)',
                                        command=control.reset_pc)
                self.btn_reset.pack(side='left')

            def create_menu():
                """
                Создание менб для главного окна.
                :return:
                """
                def create_mnu_file():
                    """
                    Создание меню "Файл".
                    :return:
                    """
                    # добавление менюхи файл
                    self.mbt_file = Menubutton(self.frm_menu, text='File',
                                               relief='raised', border=3)
                    self.mbt_file.pack(side='left')

                def create_mnu_edit():
                    """
                    Создание меню "Правка".
                    :return:
                    """
                    # добавление менюхи правка
                    self.mbt_edit = Menubutton(self.frm_menu, text='Edit',
                                               relief='raised', border=3)
                    self.mbt_edit.pack(side='left')

                def create_mnu_custom():
                    """
                    Создание меню "Настройки".
                    :return:
                    """
                    # добавление менюхи настройка
                    self.mbt_custom = Menubutton(self.frm_menu, text='Custom',
                                                 relief='raised', border=3)
                    self.mbt_custom.pack(side='left')

                    self.mnu_custom = Menu(self.mbt_custom)
                    self.mnu_custom.add_command(
                        label=self.lang['win_main_mbt_edit_bp'],
                        accelerator='F11',
                        command=self.__root.control.show_win_edit_bp)
                    self.mnu_custom.add_separator()
                    self.mnu_custom.add_command(
                        label=self.lang['win_main_mbt_edit_disk'],
                        accelerator='F12',
                        command=self.__root.control.show_win_idc)

                    self.mbt_custom.config(menu=self.mnu_custom)

                def create_mnu_help():
                    """
                    Создание меню "Помощь".
                    :return:
                    """
                    # добавление менюхи справка
                    self.btm_help = Menubutton(self.frm_menu,
                                               text=self.lang[
                                                   'win_main_mbt_help_name'],
                                               relief='raised',
                                               border=3)
                    self.btm_help.pack(side='right')

                    self.mnu_help = Menu(self.btm_help)
                    self.mnu_help.add_command(
                        label=self.lang['win_main_mbt_help_help'],
                        accelerator='F1')
                    self.mnu_help.add_separator()
                    self.mnu_help.add_command(
                        label=self.lang['win_main_mbt_help_about'],
                        accelerator='Ctrl-F1', command=self.__root.control.about)

                    self.btm_help.config(menu=self.mnu_help)

                # фрейм меню (в верхней части)
                self.frm_menu = Frame(self, border=3, relief='sunken')
                self.frm_menu.pack(side='top', fil='x')

                create_mnu_file()
                create_mnu_edit()
                create_mnu_custom()
                create_mnu_help()

            def create_frm_cpu():
                """
                Создание ырема для отображения состояния ЦП.
                :return:
                """
                self.frm_cpu = ClsFrmCPU(root=self)

            Tk.__init__(self)
            self.minsize(320, 400)
            self.title(self.lang['win_main_name'])
            self.after(100, self.win_update)

            create_frm_btn()
            create_menu()
            create_frm_cpu()

        self.__root = root
        self.lang = root.res.lang_str.lang_dict
        self.btn_debug = None
        self.frm_cpu = None
        self.btn_reset = None
        self.mbt_edit = None
        self.btm_help = None
        self.mbt_file = None
        self.btn_step = None
        self.mnu_custom = None
        self.frm_menu = None
        self.btn_show_screen = None
        self.frm_button = None
        self.btn_exit = None
        self.mbt_custom = None
        self.frm_btn = None
        self.mnu_help = None

        create_self()

    def win_update(self):
        """
        Обновление окна по таймеру.
        :return:
        """
        self.__root.logic.update_monitor()
        self.after(100, self.win_update)

    def begin(self):
        """
        В целях ухода от конфликтов имён пришлось назвать вот так ))).
        """
        self.mainloop()

    def win_exit(self):
        """
        При закрытии главного окна -- завершается всё приложение.
        :return:
        """
        self.destroy()
