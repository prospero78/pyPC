# -*- coding: utf8 -*-
"""
Класс окна экрана виртуального компьютера.
"""

from Tkinter import Frame, Button

from pak_pc.pak_gui.pak_widgets.mod_frm_key_value import ClsFrmKeyValue
from pak_pc.pak_gui.pak_widgets.mod_top_win import ClsTopWin


class ClsWinCreateDisk(ClsTopWin):
    """
    Окно для создания нового диска.
    """
    def __init__(self, root=None):
        """
        Создание окна и элементов окна.
        :param root:
        :return:
        """

        def create_frm_btn():
            """
            Создания фрейма кнопок.
            :return:
            """
            self.frm_btn = Frame(self, border=2, relief='sunken')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_ok = Button(self.frm_btn, text=' Ok ',
                                 command=self.__lang['win_idc_image_create'])
            self.btn_ok.pack(side='right')

            self.btn_cancel = Button(self.frm_btn, text='Cancel',
                                     command=self.destroy)
            self.btn_cancel.pack(side='right')

        def create_frm_disk_param():
            """
            Создание фрейма для параметров нового диска.
            :return:
            """
            self.frm_disk_param = Frame(self, border=2, relief='sunken')
            self.frm_disk_param.pack(side='top', fill='both', expand=1)

            self.fkv_name = ClsFrmKeyValue(root=self.frm_disk_param,
                                           key='Name Disk', value='default')
            self.fkv_size = ClsFrmKeyValue(root=self.frm_disk_param,
                                           key='Size Disk (kB)', value='1')

        self.__root = root
        self.__lang = root.res.lang_str.lang_dict
        self.fkv_name = None
        self.btn_cancel = None
        self.fkv_size = None
        self.btn_ok = None
        self.frm_btn = None
        self.frm_disk_param = None
        ClsTopWin.__init__(self, title=self.__lang['win_create_disk_title'])
        create_frm_btn()
        create_frm_disk_param()

    def show(self):
        """
        Показать окно.
        :return:
        """
        ClsTopWin.show(self)
        # показать поверх всех
        self.grab_set()
        self.wait_window()

    def destroy(self):
        """
        Спрятать окно.
        :return:
        """
        ClsTopWin.destroy(self)
        self.__root.gui.win_idc.focus_set()
        self.__root.gui.win_idc.grab_set()
