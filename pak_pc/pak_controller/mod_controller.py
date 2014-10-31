# -*- coding: utf8 -*-
'''
Главный класс контроллера
'''

class clsController:
    def __init__(self, root=None):
        self.root=root
        
    def reset_pc(self, event=''):
        print  'clsController.reset_pc()'
        self.Logic.reset_pc()
        
    def winEditBP_hide(self, event=''):
        #print  'clsController.winEditBP_hide()'
        self.Logic.winEditBP_hide()
        
    def show_winEditBP(self, event=''):
        #print  'clsController.show_winEditBP()'
        self.Logic.show_winEditBP()
        
    def winMain_debug(self, event=''):
        #print  'clsController.winMain_debug()'
        self.Logic.debug_CPU()
        
    def win_main_step_cpu(self, event=''):
        #print  'clsController.win_main_step_cpu()'
        self.Logic.step_CPU()
    
    def win_create_disk_ok(self, event=''):
        #print 'clsController.win_create_disk_ok()'
        self.Logic.generate_new_disk()
    
    def create_new_disk(self, event=None):
        #print 'clsController.create_new_disk()'
        self.Logic.create_new_disk()
    
    def winIDC_ok(self, event=None):
        #print 'clsController.winIDC_ok()'
        self.GUI.winIDC.destroy()
    
    def winIDC_cancel(self, event=None):
        #print 'clsController.winIDC_cancel()'
        self.GUI.winIDC.destroy()
    
    def create_disk(self, event=None):
        #print 'clsController.create_disk()'
        self.Logic.create_disk()
        
    def show_screen(self, event=None):
        #print 'clsController.show_screen()'
        self.Logic.show_screen()
    
    def run(self, event=None):
        self.GUI=self.root.GUI
        self.Logic=self.root.Logic
        self.CPU=self.root.CPU
        #print 'clsController.run()'
        self.Logic.run()
    
    def about(self, event=None):
        #print 'about()'
        self.root.GUI.winAbout.show()
    
    def exit(self, event=None):
        #print 'clsController.exit()'
        self.root.Logic.exit()
        
    def show_winLicense(self, event=None):
        self.root.Logic.show_winLicense()
        
    def hide_winLicense(self, event=None):
        self.root.Logic.hide_winLicense()
    
    def show_winIDC(self, event=None):
        self.root.Logic.show_winIDC()
