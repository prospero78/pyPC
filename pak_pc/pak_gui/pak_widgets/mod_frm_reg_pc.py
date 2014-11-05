# -*- coding: utf8 -*-
"""
Модуль отображения регистра программного счётчика.
Будет показывать содержимое и флаги.
"""

from Tkinter import Frame, Label


class ClsFrmRegPC(Frame):
    """
    Обеспечивает отображение состояия регистра программного счётчика.
    :param root: ссылка на корневой класс.
    """

    def __init__(self, root=None):
        """
        Создаёт фрейм отображения состояния регистра программного счётчика.
        :param root: ссылка на корневой элемент.
        """
        self.__root = root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')

        self.lbl_name = Label(self, text='reg_pc', border=1, relief='ridge')
        self.lbl_name.pack(side='left', fill='x')

        self.lbl_val = Label(self, text='0000', border=1, relief='groove')
        self.lbl_val.pack(side='left')


if __name__ == '__main__':
    from Tkinter import Tk

    win_test = Tk()
    win_test.title('test frmreg_pc')
    win_test.minsize(300, 200)
    reg = ClsFrmRegPC(root=win_test)
    reg.lbl_name['text'] = 'reg_pc'
    win_test.mainloop()
