# -*- coding: utf8 -*-
'''
Инициализация класса главного окна.
'''
from Tkinter import Tk, Frame, Button, Menubutton, Menu
from pak_pc.pak_gui.pak_widgets.mod_frm_cpu import ClsFrmCPU

class clsWinMain(Tk):
    def __init__(self, root=None):
        def create_self():
            def create_frmBtn():
                 # нижний фрейм главного окна
                self.frmBtn=Frame(self, border=3, relief='sunken')
                self.frmBtn.pack(side='bottom', fil='x')
                
                # кнопка "шаг" главного окна
                self.btnStep=Button(self.frmBtn, text='Step >', command=self.root.Control.winMain_stepCPU)
                self.btnStep.pack(side='left')
                
                # кнопка "Отлдака" главного окна
                self.btnDebug=Button(self.frmBtn, text='Debug >>', command=self.root.Control.winMain_debug)
                self.btnDebug.pack(side='left')
                
                # кнопка "выход" главного окна
                self.btnExit=Button(self.frmBtn,
                            text='Exit [X]',
                            command=self.root.Control.exit)
                self.btnExit.pack(side='right')
                
                # кнопка для показа экрана виртуального компьютера
                self.btnShowScreen=Button(self.frmBtn,
                            text='PC Screen',
                            command=self.root.Control.show_screen)
                self.btnShowScreen.pack(side='left')
                
                # кнопка для сброса виртуального компьютера
                self.btnReset=Button(self.frmBtn,
                            text='Reset (x)',
                            command=self.root.Control.reset_pc)
                self.btnReset.pack(side='left')
                
            def create_menu():
                def create_mnuFile():
                    # добавление менюхи файл
                    self.mbtFile=Menubutton(self.frmMenu, text='File', relief='raised', border=3)
                    self.mbtFile.pack(side='left')
                    
                def create_mnuEdit():
                    # добавление менюхи правка
                    self.mbtEdit=Menubutton(self.frmMenu, text='Edit', relief='raised', border=3)
                    self.mbtEdit.pack(side='left')
                    
                def create_mnuCustom():
                    # добавление менюхи настройка
                    self.mbtCustom=Menubutton(self.frmMenu, text='Custom', relief='raised', border=3)
                    self.mbtCustom.pack(side='left')
                    
                    self.mnuCustom=Menu(self.mbtCustom)
                    self.mnuCustom.add_command(label=self.root.Res.winMain_mbtEditBP, accelerator='F11', command=self.root.Control.show_winEditBP)
                    self.mnuCustom.add_separator()
                    self.mnuCustom.add_command(label=self.root.Res.winMain_mbtEdit_disk, accelerator='F12', command=self.root.Control.show_winIDC)
                    
                    self.mbtCustom.config(menu=self.mnuCustom)
                    
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
                self.frmCPU=ClsFrmCPU(root=self)
                
            Tk.__init__(self)
            self.minsize(320,400)
            self.title(self.root.Res.winMain_name)
            self.after(100, self.win_update)
            
            create_frmBtn()
            create_menu()
            create_frmCPU()
        
        self.root=root
        create_self()
    
    def win_update(self):
        self.root.Logic.update_monitor()
        self.after(100, self.win_update)
    
    def begin(self):
        '''
        В целях ухода от конфликтов имён пришлось назвать вот так ))).
        '''
        self.mainloop()
    
    def win_exit(self):
        self.destroy()
