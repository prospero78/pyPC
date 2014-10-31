# -*- coding: utf8 -*-
'''
Главный класс контроллера
'''

class ClsController:
    def __init__(self, root=None):
        self.root=root
        
    def reset_pc(self, event=''):
        print  '.ClsController.reset_pc()'
        self.logic.reset_pc()
        
    def winEditBP_hide(self, event=''):
        #print  '.ClsController.winEditBP_hide()'
        self.logic.winEditBP_hide()
        
    def show_winEditBP(self, event=''):
        #print  '.ClsController.show_winEditBP()'
        self.logic.show_winEditBP()
        
    def winMain_debug(self, event=''):
        #print  '.ClsController.winMain_debug()'
        self.logic.debug_CPU()
        
    def win_main_step_cpu(self, event=''):
        #print  '.ClsController.win_main_step_cpu()'
        self.logic.step_CPU()
    
    def win_create_disk_ok(self, event=''):
        #print '.ClsController.win_create_disk_ok()'
        self.logic.generate_new_disk()
    
    def create_new_disk(self, event=None):
        #print '.ClsController.create_new_disk()'
        self.logic.create_new_disk()
    
    def winIDC_ok(self, event=None):
        #print '.ClsController.winIDC_ok()'
        self.gui.winIDC.destroy()
    
    def winIDC_cancel(self, event=None):
        #print '.ClsController.winIDC_cancel()'
        self.gui.winIDC.destroy()
    
    def create_disk(self, event=None):
        #print '.ClsController.create_disk()'
        self.logic.create_disk()
        
    def show_screen(self, event=None):
        #print '.ClsController.show_screen()'
        self.logic.show_screen()
    
    def run(self, event=None):
        self.gui=self.root.gui
        self.logic=self.root.logic
        self.cpu=self.root.cpu
        #print '.ClsController.run()'
        self.logic.run()
    
    def about(self, event=None):
        #print 'about()'
        self.root.gui.winAbout.show()
    
    def exit(self, event=None):
        #print '.ClsController.exit()'
        self.root.logic.exit()
        
    def show_winLicense(self, event=None):
        self.root.logic.show_winLicense()
        
    def hide_winLicense(self, event=None):
        self.root.logic.hide_winLicense()
    
    def show_winIDC(self, event=None):
        self.root.logic.show_winIDC()
