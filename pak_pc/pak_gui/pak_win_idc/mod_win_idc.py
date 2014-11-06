# -*- coding: utf8 -*-
"""
Класс окна интерфейса дискового кластера.
"""

from Tkinter import Frame, Button

from pak_pc.pak_gui.pak_widgets.mod_frm_disk_select import ClsFrmDiskSelect
from pak_pc.pak_gui.pak_widgets.mod_top_win import ClsTopWin


class ClsWinIDC(ClsTopWin):
    """
    Окно интерфейса дискового кластера.
    """
    def __init__(self, root=None):
        """
        Создаёт окно интерфейса дискового кластера.
        :param root:
        :return:
        """

        def create_frm_btn():
            """
            Создание фрейма для кнопок.
            :return:
            """
            self.frm_btn = Frame(self, border=2, relief='sunken')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_cancel = Button(self.frm_btn,
                                     text=self.lang['win_idc_cancel'],
                                     command=self.__root.control.win_idc_cancel)
            self.btn_cancel.pack(side='right')

            self.btn_reset = Button(self.frm_btn,
                                    text=self.lang['win_idc_reset'])
            self.btn_reset.pack(side='right')

            self.btn_ok = Button(self.frm_btn, text=' Ok ',
                                 command=self.lang['win_idc_image_create'])
            self.btn_ok.pack(side='right')

        def create_frm_idc():
            """
            Создание фрейма дискового контроллера.
            :return:
            """
            self.frm_idc = Frame(self, border=2, relief='sunken')
            self.frm_idc.pack(side='top', fill='both', expand=1)

            self.frm_disk0 = ClsFrmDiskSelect(master=self.frm_idc,
                                              root=self.__root, text='Disk-0:')
            self.frm_disk1 = ClsFrmDiskSelect(master=self.frm_idc,
                                              root=self.__root, text='Disk-1:',
                                              path='None')
            self.frm_disk2 = ClsFrmDiskSelect(master=self.frm_idc,
                                              root=self.__root, text='Disk-2:',
                                              path='None')
            self.frm_disk3 = ClsFrmDiskSelect(master=self.frm_idc,
                                              root=self.__root, text='Disk-3:',
                                              path='None')

        self.__root = root
        self.lang = root.res.lang_str.lang_dict
        self.frm_disk0 = None
        self.frm_disk1 = None
        self.frm_disk2 = None
        self.frm_disk3 = None
        self.btn_cancel = None
        self.btn_reset = None
        self.frm_idc = None
        self.btn_ok = None
        self.frm_btn = None
        ClsTopWin.__init__(self, title=self.lang['win_idc_name'])

        create_frm_btn()
        create_frm_idc()
