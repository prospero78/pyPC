# -*- coding: utf8 -*-
'''
Инициализация класса главного окна.
'''
from Tkinter import Tk, Frame, Button, Menubutton, Menu
from pak_pc.pak_gui.pak_widgets.mod_frm_cpu import ClsFrmCPU

class ClsWinMain(Tk):
    def __init__(self, root=None):
        def create_self():
            def create_frmBtn():
                 # нижний фрейм главного окна
                self.frm_btn=Frame(self, border=3, relief='sunken')
                self.frm_btn.pack(side='bottom', fil='x')
                
                # кнопка "шаг" главного окна
                self.btnStep=Button(self.frm_btn, text='Step >', command=self.root.control.win_main_step_cpu)
                self.btnStep.pack(side='left')
                
                # кнопка "Отлдака" главного окна
                self.btnDebug=Button(self.frm_btn, text='Debug >>', command=self.root.control.winMain_debug)
                self.btnDebug.pack(side='left')
                
                # кнопка "выход" главного окна
                self.btnExit=Button(self.frm_btn,
                            text='Exit [X]',
                            command=self.root.control.exit)
                self.btnExit.pack(side='right')
                
                # кнопка для показа экрана виртуального компьютера
                self.btnShowScreen=Button(self.frm_btn,
                            text='PC Screen',
                            command=self.root.control.show_screen)
                self.btnShowScreen.pack(side='left')
                
                # кнопка для сброса виртуального компьютера
                self.btnReset=Button(self.frm_btn,
                            text='Reset (x)',
                            command=self.root.control.reset_pc)
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
                    
                    self.mnu_custom=Menu(self.mbtCustom)
                    self.mnu_custom.add_command(label=self.lang['win_main_mbt_edit_bp'], accelerator='F11', command=self.root.control.show_winEditBP)
                    self.mnu_custom.add_separator()
                    self.mnu_custom.add_command(label=self.lang['win_main_mbt_edit_disk'], accelerator='F12', command=self.root.control.show_winIDC)
                    
                    self.mbtCustom.config(menu=self.mnu_custom)
                    
                def create_mnuHelp():
                    # добавление менюхи справка
                    self.btmHelp=Menubutton(self.frmMenu, text=self.lang['win_main_mbt_help_name'], relief='raised', border=3)
                    self.btmHelp.pack(side='right')
                    
                    self.mnuHelp=Menu(self.btmHelp)
                    self.mnuHelp.add_command(label=self.lang['win_main_mbt_help_help'], accelerator='F1')
                    self.mnuHelp.add_separator()
                    self.mnuHelp.add_command(label=self.lang['win_main_mbt_help_about'], accelerator='Ctrl-F1', command=self.root.control.about)
                    
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
            self.title(self.lang['win_main_name'])
            self.after(100, self.win_update)
            
            create_frmBtn()
            create_menu()
            create_frmCPU()
        
        self.root=root
        self.lang=root.res.lang_str.lang_dict
        create_self()
    
    def win_update(self):
        self.root.logic.update_monitor()
        self.after(100, self.win_update)
    
    def begin(self):
        '''
        В целях ухода от конфликтов имён пришлось назвать вот так ))).
        '''
        self.mainloop()
    
    def win_exit(self):
        self.destroy()
