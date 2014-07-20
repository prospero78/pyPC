# -*- coding: utf8 -*-
'''
Инициализация класса главного окна.
'''
from Tkinter import Tk, Frame, Button, Menubutton, Menu
from pakPC.pakGUI.pakWidgets.modFrmCPU import clsFrmCPU

class clsWinMain(Tk):
    def __init__(self, root=None):
        def create_self():
            def create_frmBtn():
                 # нижний фрейм главного окна
                self.frmBtn=Frame(self, border=3, relief='sunken')
                self.frmBtn.pack(side='bottom', fil='x')
                
                # кнопка "шаг" главного окна
                self.btnStep=Button(self.frmBtn, text='Step')
                self.btnStep.pack(side='left')
                
                # кнопка "выход" главного окна
                self.btnExit=Button(self.frmBtn, text=self.root.Res.winMain_btnExit_name)
                self.btnExit.pack(side='right')
                
            def create_menu():
                def create_mnuFile():
                    # добавление менюхи файл
                    self.mbtFile=Menubutton(self.frmMenu, text=self.root.Res.winMain_mbtFile_name, relief='raised', border=3)
                    self.mbtFile.pack(side='left')
                    
                def create_mnuEdit():
                    # добавление менюхи правка
                    self.mbtEdit=Menubutton(self.frmMenu, text=self.root.Res.winMain_mbtEdit_name, relief='raised', border=3)
                    self.mbtEdit.pack(side='left')
                    
                def create_mnuCustom():
                    # добавление менюхи настройка
                    self.mbtCustom=Menubutton(self.frmMenu, text=self.root.Res.winMain_mbtCustom_name, relief='raised', border=3)
                    self.mbtCustom.pack(side='left')
                    
                def create_mnuHelp():
                    # добавление менюхи справка
                    self.btmHelp=Menubutton(self.frmMenu, text=self.root.Res.winMain_mbtHelp_name, relief='raised', border=3)
                    self.btmHelp.pack(side='right')
                    
                    self.mnuHelp=Menu(self.btmHelp)
                    self.mnuHelp.add_command(label=self.root.Res.winMain_mbtHelp_help, accelerator='F1')
                    self.mnuHelp.add_separator()
                    self.mnuHelp.add_command(label=self.root.Res.winMain_mbtHelp_about, accelerator='Ctrl-F1', command=self.root.Control.about)
                    
                    self.btmHelp.config(menu=self.mnuHelp)
                    
                # фрейм меню (в верхней части)
                self.frmMenu=Frame(self, border=3, relief='sunken')
                self.frmMenu.pack(side='top', fil='x')
                
                create_mnuFile()
                create_mnuEdit()
                create_mnuCustom()
                create_mnuHelp()
            
            def create_frmCPU():
                self.frmCPU=clsFrmCPU(root=self)
                
            Tk.__init__(self)
            self.minsize(320,400)
            self.title(self.root.Res.winMain_name)
            
            create_frmBtn()
            create_menu()
            create_frmCPU()
        
        self.root=root
        create_self()
    
    def begin(self):
        '''
        В целях ухода от конфликтов имён пришлось назвать вот так ))).
        '''
        self.mainloop()
