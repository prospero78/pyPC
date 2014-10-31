# -*- coding: utf8 -*-
'''
Класс окна "О программе".
'''

from Tkinter import Toplevel, Frame, Button, Label, Entry, Checkbutton, IntVar

class clsWinEditBP(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.root.res.winEditBP_title)
            self.minsize(380, 200)
        
        def create_frmUp():
            self.frmUp=Frame(self, border=3, relief='groove')
            self.frmUp.pack(fill='both', expand=1, side='top')
            
            self.lblreg_pc=Label(self.frmUp, border=3, relief='raised', text=' reg_pc ', bg='white', fg='red', font='Arial 24 bold')
            self.lblreg_pc.pack(side='left', fill='y')
            #--------------------------------------------------------------
            self.frmAdrBreak=Frame(self.frmUp, border=3, relief='groove')
            self.frmAdrBreak.pack(fill='x', side='top')
            
            self.lblAdrBreak=Label(self.frmAdrBreak, text='adr_break', relief='raised')
            self.lblAdrBreak.pack(side='top', fill='x')
            
            self.entAdrBreakVal=Entry(self.frmAdrBreak, cursor='hand2')
            self.entAdrBreakVal.pack(side='top', fill='x')
            
            self.entAdrBreakVal.insert(0, '0')
            #--------------------------------------------------------------
            self.frmAdrProc=Frame(self.frmUp, border=3, relief='groove')
            self.frmAdrProc.pack(fill='x', side='top')
            
            self.lblAdrProc=Label(self.frmAdrProc, text='adr_proc', relief='raised')
            self.lblAdrProc.pack(side='top', fill='x')
            
            self.entAdrProcVal=Entry(self.frmAdrProc, cursor='hand2')
            self.entAdrProcVal.pack(side='top', fill='x')
            
            self.entAdrProcVal.insert(0, '0')
            #--------------------------------------------------------------
            self.frmAct=Frame(self.frmUp, border=3, relief='groove')
            self.frmAct.pack(fill='both', expand=1, side='top')
            
            self.lblAct=Label(self.frmAct, text='act', relief='raised')
            self.lblAct.pack(side='top', fill='x')
            
            self.Act=IntVar()
            self.cheActVal=Checkbutton(self.frmAct, cursor='hand2', state='active', text='active register', variable=self.Act)
            self.cheActVal.select()
            self.cheActVal.pack(side='top', fill='x')
            
        
        def create_frmBtn():
            self.frm_btn=Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')
            
            self.btnClose=Button(self.frm_btn, text=self.root.res.winEditBP_btnClose, bg='gray', command=self.destroy)
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
        self.root.control.winEditBP_hide()
    
    def win_exit(self):
        self.destroy()
