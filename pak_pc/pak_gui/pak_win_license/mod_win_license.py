# -*- coding: utf8 -*-
"""
Класс окна "Лицензия".
"""

from Tkinter import Frame, Button, Scrollbar, Text

from pak_pc.pak_gui.pak_widgets.mod_top_win import ClsTopWin

class ClsWinLicense(ClsTopWin):
    """
    Окно для показа лицензии.
    """
    def __init__(self, root=None):
        """
        Создаёт окно для показа лицензии
        :param root:
        :return:
        """

        def create_frm_btn():
            """
            Создание фрейма кнопок.
            :return:
            """
            def btn_eng_lic_click(event=None):
                """
                Событие нажатия на кнопку лицензии на английском языке.
                :param event:
                :return:
                """
                txt = self.__root.res.lang_str.lang_dict['win_license_origin']
                self.txt_license.delete('1.0', 'end')
                self.txt_license.insert('end', txt)

            def btn_locals_lic_click(event=None):
                """
                Событие нажатия на кнопку показа лицензии на местном языке.
                :param event:
                :return:
                """
                txt = self.__root.res.lang_str.lang_dict['win_license_locale']
                self.txt_license.delete('1.0', 'end')
                self.txt_license.insert('end', txt)

            self.frm_btn = Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_eng_licence = Button(self.frm_btn,
                                          text='England',
                                          bg='gray',
                                          command=btn_eng_lic_click)
            self.btn_eng_licence.pack(side='left')

            self.btn_local_license = Button(self.frm_btn,
                                            text=self.lang['win_license_btn_local_text'],
                                            bg='gray',
                                            command=btn_locals_lic_click)
            self.btn_local_license.pack(side='left')

            self.btn_close = Button(self.frm_btn,
                                    text=self.lang['win_license_btn_close_win'],
                                    bg='gray',
                                    command=self.destroy)
            self.btn_close.pack(side='right')

        def create_frm_up():
            """
            Создание верхнего фрейма.
            :return:
            """
            self.frm_up = Frame(self, border=3, relief='groove')
            self.frm_up.pack(fill='both', expand=1, side='top')

            self.scb_license = Scrollbar(self.frm_up)
            self.scb_license.pack(side='right', fill='y')

            self.txt_license = Text(self.frm_up, height=12, width=30,
                                    font='Courier 9')
            self.txt_license.pack(fill='both', expand=1, side='left')
            self.txt_license.insert('end', self.lang['win_license_locale'])

            self.scb_license.config(command=self.txt_license.yview)
            self.txt_license.config(yscrollcommand=self.scb_license.set)

        self.__root = root
        self.lang = root.res.lang_str.lang_dict

        self.frm_btn = None
        self.txt_license = None
        self.btn_close = None
        self.scb_license = None
        self.btn_local_license = None
        self.frm_up = None
        self.btn_eng_licence = None
        ClsTopWin.__init__(self, title=self.lang['win_license_title'])

        create_frm_btn()
        create_frm_up()


    def destroy(self):
        """
        Скрыть окно.
        :return:
        """
        ClsTopWin.destroy(self)
        self.__root.control.hide_win_license()

