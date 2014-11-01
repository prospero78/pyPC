# -*- coding: utf8 -*-
'''
Модуль отображения регистра программного прерывания.
Будет показывать содержимое и его флаг активности.
'''

from Tkinter import Frame, Label

class ClsFrmRegBP(Frame):
    def __init__(self, root=None):
        self.root=root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')
        
        self.lbl_name=Label(self, text='reg_pc', border=1, relief='ridge')
        self.lbl_name.pack(side='left', fill='x')
        
        self.lblBreak=Label(self, text='adr_break', border=1, relief='groove', bg='gray')
        self.lblBreak.pack(side='left')
        
        self.lblBreakVal=Label(self, text='0', border=1, relief='groove')
        self.lblBreakVal.pack(side='left')
        
        self.lblProc=Label(self, text='adr_proc', border=1, relief='groove', bg='gray')
        self.lblProc.pack(side='left')
        
        self.lblProcVal=Label(self, text='0', border=1, relief='groove')
        self.lblProcVal.pack(side='left')
        
        self.lbl_act=Label(self, text='act', border=1, relief='groove', bg='gray')
        self.lbl_act.pack(side='left')
        
        self.lbl_act_val=Label(self, text='0', border=1, relief='groove')
        self.lbl_act_val.pack(side='left')
        
if __name__=='__main__':
    from Tkinter import Tk
    root=Tk()
    root.title('test frmreg_pc')
    root.minsize(300,200)
    reg=ClsFrmRegPC(root=root)
    reg.lbl_name['text']='reg_pc'
    root.mainloop()
