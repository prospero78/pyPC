# -*- coding: utf8 -*-
"""
Класс окна интерфейса дискового кластера.
"""

from Tkinter import Toplevel, Frame, Button

from pak_pc.pak_gui.pak_widgets.mod_frm_disk_select import ClsFrmDiskSelect


class ClsWinIDC(Toplevel):
    """
    Окно интерфейса дискового кластера.
    """
    def __init__(self, root=None):
        """
        Создаёт окно интерфейса дискового кластера.
        :param root:
        :return:
        """
        def create_self():
            """
            Создание окна самого себя.
            :return:
            """
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.lang['win_idc_name'])
            self.minsize(350, 200)

        def create_frm_btn():
            """
            Создание фрейма для кнопок.
            :return:
            """
            self.frm_btn = Frame(self, border=2, relief='sunken')
            self.frm_btn.pack(side='bottom', fill='x')

            self.btn_cancel = Button(self.frm_btn,
                                     text=self.lang['win_idc_cancel'],
                                     command=self.root.control.win_idc_cancel)
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
                                              root=self.root, text='Disk-0:')
            self.frm_disk1 = ClsFrmDiskSelect(master=self.frm_idc,
                                              root=self.root, text='Disk-1:',
                                              path='None')
            self.frm_disk2 = ClsFrmDiskSelect(master=self.frm_idc,
                                              root=self.root, text='Disk-2:',
                                              path='None')
            self.frm_disk3 = ClsFrmDiskSelect(master=self.frm_idc,
                                              root=self.root, text='Disk-3:',
                                              path='None')

        self.root = root
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

        create_self()
        create_frm_btn()
        create_frm_idc()

    def show(self):
        """
        Показ окна интерфейса дискового контролеера.
        :return:
        """
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()

    def destroy(self):
        """
        Скрытие окна интерфейса дискового контроллера.
        :return:
        """
        self.state('withdrawn')
        self.grab_release()

    def win_exit(self):
        """
        Уничтожение окна интерфейса дискового контроллера.
        при закрытии всей программы.
        :return:
        """
        self.destroy()
