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
                # нижний фрейм главного окна
                self.frm_btn = Frame(self, border=3, relief='sunken')
                self.frm_btn.pack(side='bottom', fil='x')

                # кнопка "шаг" главного окна
                self.btn_step = Button(self.frm_btn, text='Step >',
                                      command=self.root.control.win_main_step_cpu)
                self.btn_step.pack(side='left')

                # кнопка "Отлдака" главного окна
                self.btn_debug = Button(self.frm_btn, text='Debug >>',
                                       command=self.root.control.win_main_debug)
                self.btn_debug.pack(side='left')

                # кнопка "выход" главного окна
                self.btn_exit = Button(self.frm_btn,
                                      text='Exit [X]',
                                      command=self.root.control.exit)
                self.btn_exit.pack(side='right')

                # кнопка для показа экрана виртуального компьютера
                self.btn_show_screen = Button(self.frm_btn,
                                            text='PC Screen',
                                            command=self.root.control.show_screen)
                self.btn_show_screen.pack(side='left')

                # кнопка для сброса виртуального компьютера
                self.btn_reset = Button(self.frm_btn,
                                       text='Reset (x)',
                                       command=self.root.control.reset_pc)
                self.btn_reset.pack(side='left')

            def create_menu():
                """
                Создание менб для главного окна.
                :return:
                """
                def create_mnuFile():
                    """
                    Создание меню "Файл".
                    :return:
                    """
                    # добавление менюхи файл
                    self.mbt_file = Menubutton(self.frmMenu, text='File',
                                              relief='raised', border=3)
                    self.mbt_file.pack(side='left')

                def create_mnuEdit():
                    """
                    Создание меню "Правка".
                    :return:
                    """
                    # добавление менюхи правка
                    self.mbt_edit = Menubutton(self.frmMenu, text='Edit',
                                              relief='raised', border=3)
                    self.mbt_edit.pack(side='left')

                def create_mnuCustom():
                    """
                    Создание меню "Настройки".
                    :return:
                    """
                    # добавление менюхи настройка
                    self.mbt_custom = Menubutton(self.frmMenu, text='Custom',
                                                relief='raised', border=3)
                    self.mbt_custom.pack(side='left')

                    self.mnu_custom = Menu(self.mbt_custom)
                    self.mnu_custom.add_command(
                        label=self.lang['win_main_mbt_edit_bp'],
                        accelerator='F11',
                        command=self.root.control.show_win_edit_bp)
                    self.mnu_custom.add_separator()
                    self.mnu_custom.add_command(
                        label=self.lang['win_main_mbt_edit_disk'],
                        accelerator='F12',
                        command=self.root.control.show_win_idc)

                    self.mbt_custom.config(menu=self.mnu_custom)

                def create_mnuHelp():
                    """
                    Создание меню "Помощь".
                    :return:
                    """
                    # добавление менюхи справка
                    self.btmHelp = Menubutton(self.frmMenu, text=self.lang[
                        'win_main_mbt_help_name'], relief='raised', border=3)
                    self.btmHelp.pack(side='right')

                    self.mnu_help = Menu(self.btmHelp)
                    self.mnu_help.add_command(
                        label=self.lang['win_main_mbt_help_help'],
                        accelerator='F1')
                    self.mnu_help.add_separator()
                    self.mnu_help.add_command(
                        label=self.lang['win_main_mbt_help_about'],
                        accelerator='Ctrl-F1', command=self.root.control.about)

                    self.btmHelp.config(menu=self.mnu_help)

                # фрейм меню (в верхней части)
                self.frmMenu = Frame(self, border=3, relief='sunken')
                self.frmMenu.pack(side='top', fil='x')

                create_mnuFile()
                create_mnuEdit()
                create_mnuCustom()
                create_mnuHelp()

            def create_frmCPU():
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
            create_frmCPU()

        self.root = root
        self.lang = root.res.lang_str.lang_dict
        create_self()

    def win_update(self):
        """
        Обновление окна по таймеру.
        :return:
        """
        self.root.logic.update_monitor()
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
