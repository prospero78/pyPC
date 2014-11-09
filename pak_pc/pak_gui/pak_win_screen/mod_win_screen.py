# -*- coding: utf8 -*-
'''
Класс окна экрана виртуального компьютера.
'''

from Tkinter import Frame, Button, Label
from pak_pc.pak_gui.pak_widgets.mod_win import ClsWin


class ClsWinScreen(ClsWin):
    """
    Показывает экран виртуального компьютера.
    """
    def __init__(self, root=None):
        """
        Создаёт отдельное окно под экран виртуального компьютера.
        :param root: ссылка на корневой объект
        :return:
        """

        def __create_frm_screen():
            """
            Создание формы для отображения окна вывода.
            :return:
            """
            self.__frm_screen = Frame(self, border=3, relief='groove')
            self.__frm_screen.pack(fill='both', expand=1, side='top')

            # self.cnvScreen=Canvas(self.frm_screen,
            #                       bg='white', width=640, height=480)
            #self.cnvScreen.pack(fill='both')

            self.lbl_screen = Label(self.__frm_screen, bg='black', fg='yellow',
                                    font='Consolas 10')
            self.lbl_screen.pack(fill='both')

            str_out = ''
            for row in xrange(0, 40):
                for col in xrange(0, 80):
                    str_out += ' '
                    str_out += '\n'
            self.lbl_screen['text'] = str_out

        def __create_frm_btn():
            """
            Создание фрейма с кнопками.
            :return:
            """
            self.frm_btn = Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_screen_close = Button(self.frm_btn,
                                           text=self.__lang['win_screen_btn_close_text'],
                                           bg='gray',
                                           command=self.destroy)
            self.btn_screen_close.pack(side='right')

            self.btn_reset = Button(self.frm_btn,
                                    text=self.__lang['win_screen_btn_reset'],
                                    bg='gray',
                                    command=self.__root.control.reset_pc)
            self.btn_reset.pack(side='right')

        self.__root = root
        self.__lang = root.res.lang_str.lang_dict
        ClsWin.__init__(self, title=self.__lang['win_screen_title'])
        self.lbl_screen = None
        self.btn_screen_close = None
        self.__frm_button = None
        self.__frm_screen = None
        self.frm_btn = None
        self.btn_reset = None

        __create_frm_btn()
        __create_frm_screen()
        # признак отображённости окна терминала
        self.win_screen_show = 0


    def show(self):
        """
        Показывает окно экрана виртуального компьютера.
        :return:
        """
        lang = self.__lang
        self.__root.gui.win_main.btn_show_screen[
            'text'] = lang['win_screen_btn_close_text']
        ClsWin.show(self)

    def destroy(self):
        """
        Скрывает окно экрана виртуального компьютера.
        :return:
        """
        self.__root.gui.win_main.btn_show_screen['text'] = self.__lang[
            'win_main_btn_show_screen_show']
        ClsWin.destroy(self)
