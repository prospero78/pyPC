# -*- coding: utf8 -*-
'''
Модуль отображения регистра указателя стека.
'''

from Tkinter import Frame, Label

class clsFrmRegSP(Frame):
    def __init__(self, root=None):
        self.root=root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')
        
        self.lblName=Label(self, text='RegSP', border=1, relief='ridge')
        self.lblName.pack(side='left', fill='x')
        
        self.lblVal=Label(self, text='0000', border=1, relief='groove')
        self.lblVal.pack(side='left')

        
if __name__=='__main__':
    from Tkinter import Tk
    root=Tk()
    root.title('test frmRegSP')
    root.minsize(300,200)
    reg=clsFrmRegPC(root=root)
    reg.lblName['text']='RegSP'
    root.mainloop()