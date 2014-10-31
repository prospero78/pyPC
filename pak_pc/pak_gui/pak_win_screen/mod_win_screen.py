# -*- coding: utf8 -*-
'''
Класс окна экрана виртуального компьютера.
'''

from Tkinter import Toplevel, Frame, Button, Canvas, Label

class ClsWinScreen(Toplevel):
    def __init__(self, root=None):
        def create_self():
            Toplevel.__init__(self)
            self.state('withdrawn')
            self.title(self.lang['win_screen_title'])
            self.minsize(640, 480)
        
        def create_frmScreen():
            self.frmScreen=Frame(self, border=3, relief='groove')
            self.frmScreen.pack(fill='both', expand=1, side='top')
            
            #self.cnvScreen=Canvas(self.frmScreen, bg='white', width=640, height=480)
            #self.cnvScreen.pack(fill='both')
            
            self.lblScreen=Label(self.frmScreen, bg='black', fg='yellow', font='Consolas 10')
            self.lblScreen.pack(fill='both')
            
            a=''
            for i in xrange(0,40):
                for i1 in xrange(0,80):
                    a+=' '
                a+='\n'
            self.lblScreen['text']=a
        
        def create_frmBtn():
            self.frm_btn=Frame(self, border=3, relief='raised')
            self.frm_btn.pack(side='bottom', fill='x')
            
            self.btnScreenClose=Button(self.frm_btn, text=self.lang['win_screen_btn_close_text'], bg='gray', command=self.destroy)
            self.btnScreenClose.pack(side='right')
            
        self.root=root
        self.lang=root.res.lang_str.lang_dict
        create_self()
        create_frmBtn()
        create_frmScreen()
        # признак отображённости окна терминала
        self.winScreen_show=0
        
        
        
    def show(self):
        self.winScreen_show=1
        self.state('normal')
        # показать поверх всех с фокусом без удержания фокуса
        self.focus_set()
        #self.grab_set()
        #self.wait_window()
        self.root.gui.winMain.btnShowScreen['text']=self.root.res.winMain_btnShowScreen_hide
        
    def destroy(self):
        self.winScreen_show=0
        self.state('withdrawn')
        self.grab_release()
        self.root.gui.winMain.btnShowScreen['text']=self.root.res.winMain_btnShowScreen_show
    
    def win_exit(self):
        self.destroy()
