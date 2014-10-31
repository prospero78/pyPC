# -*- coding: utf8 -*-
'''
Модуль отображения регистра.
Будет показывать содержимое и флаги.
'''

from Tkinter import Frame, Label

class clsFrmReg(Frame):
    def __init__(self, root=None):
        self.root=root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')
        
        self.lblName=Label(self, text='RegXX', border=1, relief='ridge')
        self.lblName.pack(side='left', fill='x')
        
        self.lblVal=Label(self, text='00', border=1, relief='groove')
        self.lblVal.pack(side='left')
        
        self.lblFlagZ=Label(self, text='Z', border=1, relief='ridge')
        self.lblFlagZ.pack(side='left', fill='x')
        
        self.lblValZ=Label(self, text='0', border=1, relief='groove')
        self.lblValZ.pack(side='left', fill='x')
        
        self.lblFlagO=Label(self, text='O', border=1, relief='ridge')
        self.lblFlagO.pack(side='left', fill='x')
        
        self.lblValO=Label(self, text='0', border=1, relief='groove')
        self.lblValO.pack(side='left', fill='x')
        
        self.lblFlagC=Label(self, text='C', border=1, relief='ridge')
        self.lblFlagC.pack(side='left', fill='x')
        
        self.lblValC=Label(self, text='0', border=1, relief='groove')
        self.lblValC.pack(side='left', fill='x')
        
if __name__=='__main__':
    from Tkinter import Tk
    root=Tk()
    root.title('test frmReg')
    root.minsize(300,200)
    reg=clsFrmReg(root=root)
    reg.lblName['text']='123'
    root.mainloop()
