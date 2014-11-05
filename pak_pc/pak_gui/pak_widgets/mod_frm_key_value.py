# -*- coding: utf8 -*-
"""
Модуль отображения регистра программного счётчика.
Будет показывать содержимое и флаги.
"""

from Tkinter import Frame, Label, Entry


class ClsFrmKeyValue(Frame):
    """
    Класс обеспечивает работу с парой ключ:значение.
    """
    def __init__(self, root=None, key='Key', value='None'):
        """
        Конструтирует пару ключ:значение.
        :param root:
        :param key:
        :param value:
        :return:
        """
        self.__root = root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')

        self.lbl_key = Label(self, text=key, border=1, relief='ridge', width=14)
        self.lbl_key.pack(side='left', fill='x', expand=1)

        self.ent_val = Entry(self, border=1, relief='groove')
        self.ent_val.pack(side='left', fill='x', expand=1)
        self.ent_val.delete(0, 'end')
        self.ent_val.insert(0, value)

    def get_val(self):
        """
        Возвращает значение ключа из пары ключ:значение.
        :return:
        """
        return self.ent_val.get()


if __name__ == '__main__':
    from Tkinter import Tk

    WIN_MAIN = Tk()
    WIN_MAIN.title('test frmreg_pc')
    WIN_MAIN.minsize(300, 200)
    REG = ClsFrmKeyValue(root=WIN_MAIN)
    REG.lbl_key['text'] = 'reg_pc'
    WIN_MAIN.mainloop()
