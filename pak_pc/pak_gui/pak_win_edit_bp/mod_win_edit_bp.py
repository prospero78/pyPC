# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Frame, Button, Label, Entry, Checkbutton, IntVar
from pak_pc.pak_gui.pak_widgets.mod_top_win import ClsTopWin

class ClsWinEditBP(ClsTopWin):
    """
    Окно редактирования свойств регистра ВР.
    """
    def __init__(self, root=None):
        """
        Создаёт окно регистра программного прерывания.
        :param root:
        :return:
        """

        def create_frm_up():
            """
            Создание фрейма верхней части.
            :return:
            """
            self.frm_up = Frame(self, border=3, relief='groove')
            self.frm_up.pack(fill='both', expand=1, side='top')

            self.lbl_reg_pc = Label(self.frm_up,
                                    border=3,
                                    relief='raised',
                                    text=' reg_pc ',
                                    bg='white',
                                    fg='red',
                                    font='Arial 24 bold')
            self.lbl_reg_pc.pack(side='left', fill='y')
            # --------------------------------------------------------------
            self.frm_adr_break = Frame(self.frm_up, border=3, relief='groove')
            self.frm_adr_break.pack(fill='x', side='top')

            self.lbl_adr_break = Label(self.frm_adr_break,
                                       text='adr_break',
                                       relief='raised')
            self.lbl_adr_break.pack(side='top', fill='x')

            self.ent_adr_break_val = Entry(self.frm_adr_break, cursor='hand2')
            self.ent_adr_break_val.pack(side='top', fill='x')

            self.ent_adr_break_val.insert(0, '0')
            #--------------------------------------------------------------
            self.frm_adr_proc = Frame(self.frm_up, border=3, relief='groove')
            self.frm_adr_proc.pack(fill='x', side='top')

            self.lbl_adr_proc = Label(self.frm_adr_proc,
                                      text='adr_proc',
                                      relief='raised')
            self.lbl_adr_proc.pack(side='top', fill='x')

            self.ent_adr_proc_val = Entry(self.frm_adr_proc, cursor='hand2')
            self.ent_adr_proc_val.pack(side='top', fill='x')

            self.ent_adr_proc_val.insert(0, '0')
            #--------------------------------------------------------------
            self.frm_act = Frame(self.frm_up, border=3, relief='groove')
            self.frm_act.pack(fill='both', expand=1, side='top')

            self.lbl_act = Label(self.frm_act, text='flag_act', relief='raised')
            self.lbl_act.pack(side='top', fill='x')

            self.flag_act = IntVar()
            self.chek_act_val = Checkbutton(self.frm_act,
                                            cursor='hand2',
                                            state='active',
                                            text='active register',
                                            variable=self.flag_act)
            self.chek_act_val.select()
            self.chek_act_val.pack(side='top', fill='x')

        def create_frm_btn():
            """
            Создание фрейма кнопок.
            :return:
            """
            self.frm_btn = Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_close = Button(self.frm_btn,
                                    text=self.lang['win_edit_bp_btn_close'],
                                    bg='gray',
                                    command=self.destroy)
            self.btn_close.pack(side='right')

        self.__root = root
        self.lang = root.res.lang_str.lang_dict
        self.ent_adr_break_val = None
        self.frm_up = None
        self.frm_adr_break = None
        self.flag_act = None
        self.ent_adr_proc_val = None
        self.frm_btn = None
        self.frm_adr_proc = None
        self.lbl_act = None
        self.lbl_reg_pc = None
        self.lbl_adr_proc = None
        self.chek_act_val = None
        self.frm_act = None
        self.btn_close = None
        self.lbl_adr_break = None

        ClsTopWin.__init__(self, title=self.lang['win_edit_bp_title'])
        create_frm_up()
        create_frm_btn()


    def destroy(self):
        """
        Скрытие окна регистра программного прерывания.
        :return:
        """
        ClsTopWin.destroy(self)
        self.__root.control.win_edit_bp_hide()
