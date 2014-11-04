# -*- coding: utf8 -*-
"""
Класс окна "Лицензия".
"""

from Tkinter import Toplevel, Frame, Button, Scrollbar, Text


class clsWinLicense(Toplevel):
    """
    Окно для показа лицензии.
    """
    def __init__(self, root=None):
        """
        Создаёт окно для показа лицензии
        :param root:
        :return:
        """
        def create_self():
            """
            Создание самого окна.
            :return:
            """
            Toplevel.__init__(self)
            self.title(self.lang['win_license_title'])
            self.minsize(350, 240)
            self.state('withdrawn')

        def create_frm_btn():
            """
            Создание фрейма кнопок.
            :return:
            """
            def btnEngLic_click(event=None):
                """
                Событие нажатия на кнопку лицензии на английском языке.
                :param event:
                :return:
                """
                self.txtLicense.delete('1.0', 'end')
                self.txtLicense.insert('end', self.root.res.winLicense_eng)

            def btnLocalsLic_click(event=None):
                """
                Событие нажатия на кнопку показа лицензии на местном языке.
                :param event:
                :return:
                """
                self.txtLicense.delete('1.0', 'end')
                self.txtLicense.insert('end', self.root.res.winLicense_locale)

            self.frm_btn = Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btnEngLicence = Button(self.frm_btn, text='England', bg='gray',
                                        command=btnEngLic_click)
            self.btnEngLicence.pack(side='left')

            self.btn_local_license = Button(self.frm_btn, text=self.lang[
                'win_license_btn_local_text'], bg='gray',
                                            command=btnLocalsLic_click)
            self.btn_local_license.pack(side='left')

            self.btn_close = Button(self.frm_btn, text='Close', bg='gray',
                                   command=self.destroy)
            self.btn_close.pack(side='right')

        def create_frm_up():
            """
            Создание верхнего фрейма.
            :return:
            """
            self.frm_up = Frame(self, border=3, relief='groove')
            self.frm_up.pack(fill='both', expand=1, side='top')

            self.scbLicense = Scrollbar(self.frm_up)
            self.scbLicense.pack(side='right', fill='y')

            self.txtLicense = Text(self.frm_up, height=12, width=30,
                                   font='Courier 9')
            self.txtLicense.pack(fill='both', expand=1, side='left')
            self.txtLicense.insert('end', self.lang['win_license_locale'])

            self.scbLicense.config(command=self.txtLicense.yview)
            self.txtLicense.config(yscrollcommand=self.scbLicense.set)

        self.root = root
        self.lang = root.res.lang_str.lang_dict
        self.frm_btn = None
        self.txtLicense = None
        self.btn_close = None
        create_self()
        create_frm_btn()
        create_frm_up()

    def show(self):
        """
        Показать окно.
        :return:
        """
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()

    def destroy(self):
        """
        Скрыть окно.
        :return:
        """
        self.state('withdrawn')
        self.grab_release()
        self.root.control.hide_win_license()

    def win_exit(self):
        """
        При выходе из программы  -- уничтожить это окно.
        :return:
        """
        self.destroy()
