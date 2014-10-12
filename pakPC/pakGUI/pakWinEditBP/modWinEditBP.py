# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Toplevel, Frame, Button, Label, Entry, Checkbutton

class clsWinEditBP(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.root.Res.winEditBP_title)
            self.minsize(380, 200)
        
        def create_frmUp():
            self.frmUp=Frame(self, border=3, relief='groove')
            self.frmUp.pack(fill='both', expand=1, side='top')
            
            self.lblRegBP=Label(self.frmUp, border=3, relief='raised', text=' RegBP ', bg='white', fg='red', font='Arial 24 bold')
            self.lblRegBP.pack(side='left', fill='y')
            #--------------------------------------------------------------
            self.frmAdrBreak=Frame(self.frmUp, border=3, relief='groove')
            self.frmAdrBreak.pack(fill='x', expand=1, side='top')
            
            self.lblAdrBreak=Label(self.frmAdrBreak, text='adr_break', relief='raised')
            self.lblAdrBreak.pack()
            
            self.entAdrBreakVal=Entry(self.frmAdrBreak, cursor='hand2')
            self.entAdrBreakVal.pack(side='top', fill='x')
            
            self.entAdrBreakVal.insert(0, self.root.CPU.RegBP.adr_break)
            #--------------------------------------------------------------
            self.lblAdrProc=Label(self.frmUp, text='adr_proc')
            self.lblAdrProc.pack(side='top', fill='x')
            
            self.entAdrProcVal=Entry(self.frmUp, cursor='hand2')
            self.entAdrProcVal.pack(side='top', fill='x')
            
            self.entAdrProcVal.insert(0, self.root.CPU.RegBP.adr_break)
            #--------------------------------------------------------------
            self.lblAct=Label(self.frmUp, text='act')
            self.lblAct.pack(side='top')
            
            self.cheActVal=Checkbutton(self.frmUp, cursor='hand2')
            self.cheActVal.pack(side='top', fill='x')
            
        
        def create_frmBtn():
            self.frmBtn=Frame(self, border=3, relief='raised')
            self.frmBtn.pack(side='bottom', fill='x')
            
            self.btnClose=Button(self.frmBtn, text=self.root.Res.winEditBP_btnClose, bg='gray', command=self.destroy)
            self.btnClose.pack(side='right')
            
        
        self.root=root
        create_self()
        create_frmUp()
        create_frmBtn()
        
        
        
    def show(self):
        self.state('normal')
        # показать поверх всех с фокусом
        self.focus_set()
        self.grab_set()
        self.wait_window()
        
    def destroy(self):
        self.state('withdrawn')
        self.grab_release()
