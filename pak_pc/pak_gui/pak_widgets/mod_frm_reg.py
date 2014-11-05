# -*- coding: utf8 -*-
"""
Модуль отображения регистра.
Будет показывать содержимое и флаги.
"""

from Tkinter import Frame, Label


class ClsFrmReg(Frame):
    """
    Фрейм регистро
    """
    def __init__(self, root=None):
        """
        Создаёт фрейм регистра.
        :param root:
        :return:
        """
        self.__root = root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')

        self.lbl_name = Label(self, text='RegXX', border=1, relief='ridge')
        self.lbl_name.pack(side='left', fill='x')

        self.lbl_val = Label(self, text='00', border=1, relief='groove')
        self.lbl_val.pack(side='left')

        self.lbl_flag_z = Label(self, text='Z', border=1, relief='ridge')
        self.lbl_flag_z.pack(side='left', fill='x')

        self.lbl_val_z = Label(self, text='0', border=1, relief='groove')
        self.lbl_val_z.pack(side='left', fill='x')

        self.lbl_flag_o = Label(self, text='O', border=1, relief='ridge')
        self.lbl_flag_o.pack(side='left', fill='x')

        self.lbl_val_o = Label(self, text='0', border=1, relief='groove')
        self.lbl_val_o.pack(side='left', fill='x')

        self.lbl_flag_c = Label(self, text='C', border=1, relief='ridge')
        self.lbl_flag_c.pack(side='left', fill='x')

        self.lbl_val_c = Label(self, text='0', border=1, relief='groove')
        self.lbl_val_c.pack(side='left', fill='x')


if __name__ == '__main__':
    from Tkinter import Tk

    WIN_TEST = Tk()
    WIN_TEST.title('test frm_reg')
    WIN_TEST.minsize(300, 200)
    REG = ClsFrmReg(root=WIN_TEST)
    REG.lbl_name['text'] = '123'
    WIN_TEST.mainloop()
