# -*- coding: utf8 -*-
'''
Модуль отображения регистра программного счётчика.
Будет показывать содержимое и флаги.
'''

from Tkinter import Frame, Label, Entry

class clsFrmKeyValue(Frame):
    def __init__(self, root=None, key='Key', value='None'):
        self.root=root
        Frame.__init__(self, master=root, border=2, relief='ridge')
        self.pack(fill='x', side='top')
        
        self.lblKey=Label(self, text=key, border=1, relief='ridge', width=14)
        self.lblKey.pack(side='left', fill='x', expand=1)
        
        self.entVal=Entry(self, border=1, relief='groove')
        self.entVal.pack(side='left', fill='x', expand=1)
        self.entVal.delete(0,'end')
        self.entVal.insert(0,value)
    
    def get_val(self):
        return self.entVal.get()

        
if __name__=='__main__':
    from Tkinter import Tk
    root=Tk()
    root.title('test frmreg_pc')
    root.minsize(300,200)
    reg=clsFrmreg_pc(root=root)
    reg.lblName['text']='reg_pc'
    root.mainloop()
