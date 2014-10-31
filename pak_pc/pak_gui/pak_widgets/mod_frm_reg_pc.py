# -*- coding: utf8 -*-
'''
Модуль отображения регистра программного счётчика.
Будет показывать содержимое и флаги.
'''

from Tkinter import Frame, Label

class ClsFrmRegPC(Frame):
    def __init__(self, root=None):
        self.root=root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')
        
        self.lbl_name=Label(self, text='reg_pc', border=1, relief='ridge')
        self.lbl_name.pack(side='left', fill='x')
        
        self.lbl_val=Label(self, text='0000', border=1, relief='groove')
        self.lbl_val.pack(side='left')

        
if __name__=='__main__':
    from Tkinter import Tk
    root=Tk()
    root.title('test frmreg_pc')
    root.minsize(300,200)
    reg=ClsFrmRegPC(root=root)
    reg.lbl_name['text']='reg_pc'
    root.mainloop()
