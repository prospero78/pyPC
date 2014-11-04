# -*- coding: utf8 -*-
"""
Модуль отображения регистра программного прерывания.
Будет показывать содержимое и его флаг активности.
"""

from Tkinter import Frame, Label


class ClsFrmRegBP(Frame):
    """
    Фрейм выводит состояние регистра программного прерывания.
    :param root:
    """

    def __init__(self, root=None):
        """
        Создаёт экземпляр класса.
        :param root: ссылка на корневой класс приложения.
        """
        self.root = root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')

        self.lbl_name = Label(self, text='reg_pc', border=1, relief='ridge')
        self.lbl_name.pack(side='left', fill='x')

        self.lbl_break = Label(self,
                               text='adr_break',
                               border=1,
                               relief='groove',
                               bg='gray')
        self.lbl_break.pack(side='left')

        self.lbl_break_val = Label(self, text='0', border=1, relief='groove')
        self.lbl_break_val.pack(side='left')

        self.lbl_proc = Label(self,
                              text='adr_proc',
                              border=1,
                              relief='groove',
                              bg='gray')
        self.lbl_proc.pack(side='left')

        self.lbl_proc_val = Label(self, text='0', border=1, relief='groove')
        self.lbl_proc_val.pack(side='left')

        self.lbl_act = Label(self, text='flag_act', border=1, relief='groove',
                             bg='gray')
        self.lbl_act.pack(side='left')

        self.lbl_act_val = Label(self, text='0', border=1, relief='groove')
        self.lbl_act_val.pack(side='left')


if __name__ == '__main__':
    from Tkinter import Tk

    win_test = Tk()
    win_test.title('test frmreg_pc')
    win_test.minsize(300, 200)
    reg = ClsFrmRegBP(root=win_test)
    reg.lbl_name['text'] = 'reg_pc'
    win_test.mainloop()
