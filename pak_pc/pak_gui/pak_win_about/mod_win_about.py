# -*- coding: utf8 -*-
"""
Класс окна "О программе".
"""

from Tkinter import Frame, Button, Label, Text, Scrollbar
from pak_pc.pak_gui.pak_widgets.mod_win import ClsWin

class ClsWinAbout(ClsWin):
    """
    Окно "О программе".
    """
    def __init__(self, root=None):
        """
        Сощдание окна "О программе".
        :param root:
        :return:
        """

        def create_frm_up():
            """
            Создание верхнего фрейма.
            :return:
            """
            self.frm_up = Frame(self, border=3, relief='groove')
            self.frm_up.pack(fill='both', expand=1, side='top')

            self.lbl_py_pc = Label(self.frm_up, border=3, relief='sunken',
                                   text=' pyPC \n' + self.__root.res.build,
                                   bg='white', fg='red', font='Arial 24 bold')
            self.lbl_py_pc.pack(side='left', fill='y')

            self.lbl_git = Label(self.frm_up, text=self.lang['win_about_url'],
                                 fg='blue', cursor='hand2')
            self.lbl_git.pack(side='bottom', fill='x')

            self.scb_about = Scrollbar(self.frm_up)
            self.scb_about.pack(side='right', fill='y')

            self.txt_about = Text(self.frm_up, height=12, width=30,
                                  font='Courier 9')
            self.txt_about.pack(fill='both', expand=1, side='left')
            self.txt_about.insert('end', self.lang['win_about_txt'])

            self.scb_about.config(command=self.txt_about.yview)
            self.txt_about.config(yscrollcommand=self.scb_about.set)

        def create_frm_btn():
            """
            Создание нижнего фрейма
            :return:
            """
            self.frm_btn = Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_close_about = Button(self.frm_btn,
                                          text=self.lang['win_about_close'],
                                          bg='gray', command=self.destroy)
            self.btn_close_about.pack(side='right')

            control = self.__root.control

            self.btn_license = Button(self.frm_btn,
                                      text=self.lang['win_about_license'],
                                      bg='gray',
                                      command=control.show_win_license)
            self.btn_license.pack()

        self.__root = root
        self.lang = root.res.lang_str.lang_dict
        self.frm_up = None
        self.scb_about = None
        self.btn_close_about = None
        self.btn_license = None
        self.lbl_py_pc = None
        self.txt_about = None
        self.frm_btn = None
        self.lbl_git = None

        ClsWin.__init__(self, title=self.lang['win_about_name'])
        create_frm_up()
        create_frm_btn()


    def show(self):
        """
        Показать окно.
        :return:
        """
        ClsWin.show(self)
        # показать поверх всех
        self.grab_set()
        self.wait_window()
