# -*- coding: utf8 -*-
"""
Инициализация пакета виджета выбора диска.
"""

from Tkinter import Frame, Label, Button
from tkFileDialog import askopenfilename


class ClsFrmDiskSelect(Frame):
    """
    Фрейм выбора диска.
    """
    def __init__(self,
                 master=None,
                 root=None,
                 text='Disk-0:',
                 path='./data/default.dsk'):
        """
        Создаёт фрейм для выбора диска.
        :param master:
        :param root:
        :param text:
        :param path:
        :return:
        """
        def create_self():
            """
            Создание самого фрейма.
            :return:
            """
            def open_disk(event=''):
                """
                Запрос на отрытие файла-диска.
                :param event:
                :return:
                """
                d = askopenfilename(defaultextension='.dsk',
                                    initialfile='./data/default.dsk',
                                    filetypes=[('Disk images', '.dsk'), ],
                                    title=self.root.res.winIDC_OpenDiskImage)
                self.root.gui.win_idc.lift()
                self.root.gui.win_idc.focus_get()

            Frame.__init__(self, master=self.master)
            self.pack(side='top', fill='x')

            self.lbl_path = Label(self, text=self.text, border=2,
                                  relief='raised')
            self.lbl_path.pack(side='left')

            self.lbl_disk_path = Label(self, text=self.path, anchor='w', border=2,
                                       relief='groove')
            self.lbl_disk_path.pack(side='left', fill='both', expand=1)

            self.btn_create = Button(self,
                                     text=self.lang['win_idc_image_create'],
                                     command=self.root.control.create_disk)
            self.btn_create.pack(side='left')

            self.btn_open = Button(self, text=self.lang['win_idc_open'],
                                   command=open_disk)
            self.btn_open.pack(side='left')

            self.btn_clear = Button(self, text=self.lang['win_idc_image_unpath'])
            self.btn_clear.pack(side='left')


        self.root = root
        self.lang = root.res.lang_str.lang_dict
        self.master = master
        self.path = path
        self.text = text
        create_self()
