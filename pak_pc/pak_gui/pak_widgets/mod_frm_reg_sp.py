# -*- coding: utf8 -*-
'''
Модуль отображения регистра указателя стека.
'''

from Tkinter import Frame, Label

class ClsFrmRegSP(Frame):
    def __init__(self, root=None):
        self.root=root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')
        
        self.lbl_name=Label(self, text='reg_sp', border=1, relief='ridge')
        self.lbl_name.pack(side='left', fill='x')
        
        self.lblAdr=Label(self, text='adr', border=1, relief='groove', bg='gray')
        self.lblAdr.pack(side='left')
        
        self.lblAdrVal=Label(self, text='0000', border=1, relief='groove')
        self.lblAdrVal.pack(side='left')
        
        self.lbl_val=Label(self, text='val', border=1, relief='groove', bg='gray')
        self.lbl_val.pack(side='left')
        
        self.lblValVal=Label(self, text='0000', border=1, relief='groove')
        self.lblValVal.pack(side='left')
        
        

        
if __name__=='__main__':
    from Tkinter import Tk
    root=Tk()
    root.title('test frm_reg_sp')
    root.minsize(300,200)
    reg=ClsFrmRegPC(root=root)
    reg.lbl_name['text']='reg_sp'
    root.mainloop()
