# -*- coding: utf8 -*-
'''
Класс окна экрана виртуального компьютера.
'''

from Tkinter import Toplevel, Frame, Button, Label


class ClsWinScreen(Toplevel):
    """
    Показывает экран виртуального компьютера.
    """
    def __init__(self, root=None):
        """
        Создаёт отдельное окно под экран виртуального компьютера.
        :param root: ссылка на корневой объект
        :return:
        """
        def create_self():
            """
            Создание самого окна.
            :return:
            """
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.lang['win_screen_title'])
            self.minsize(640, 480)

        def create_frm_screen():
            """
            Создание формы для отображения окна вывода.
            :return:
            """
            self.frm_screen = Frame(self, border=3, relief='groove')
            self.frm_screen.pack(fill='both', expand=1, side='top')

            # self.cnvScreen=Canvas(self.frm_screen,
            #                       bg='white', width=640, height=480)
            #self.cnvScreen.pack(fill='both')

            self.lbl_screen = Label(self.frm_screen, bg='black', fg='yellow',
                                    font='Consolas 10')
            self.lbl_screen.pack(fill='both')

            str_out = ''
            for row in xrange(0, 40):
                for col in xrange(0, 80):
                    str_out += ' '
                    str_out += '\n'
            self.lbl_screen['text'] = str_out

        def create_frm_btn():
            """
            Создание фрейма с кнопками.
            :return:
            """
            self.frm_btn = Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_screen_close = Button(self.frm_btn, text=self.lang[
                'win_screen_btn_close_text'], bg='gray', command=self.destroy)
            self.btn_screen_close.pack(side='right')

        self.root = root
        self.lang = root.res.lang_str.lang_dict
        create_self()
        create_frm_btn()
        create_frm_screen()
        # признак отображённости окна терминала
        self.win_screen_show = 0


    def show(self):
        """
        Показывает окно экрана виртуального компьютера.
        :return:
        """
        self.win_screen_show = 1
        self.state('normal')
        # показать поверх всех с фокусом без удержания фокуса
        self.focus_set()
        # self.grab_set()
        #self.wait_window()
        self.root.gui.win_main.btn_show_screen[
            'text'] = self.root.res.winMain_btnShowScreen_hide

    def destroy(self):
        """
        Скрывает окно экрана виртуального компьютера.
        :return:
        """
        self.win_screen_show = 0
        self.state('withdrawn')
        self.grab_release()
        self.root.gui.win_main.btn_show_screen['text'] = self.lang[
            'win_main_btn_show_screen_show']

    def win_exit(self):
        self.destroy()
