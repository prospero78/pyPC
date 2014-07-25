# -*- coding: utf8 -*-
'''
Главный класс контроллера
'''

class clsController:
    def __init__(self, root=None):
        self.root=root
        self.GUI=self.root.GUI
    
    def run(self, event=None):
        print 'clsController.run()'
        self.GUI.run()
    
    def about(self, event=None):
        print 'about()'
        self.root.GUI.winAbout.show()
    
    def exit(self, event=None):
        print 'clsController.exit()'
        self.root.Logic.exit()
        
    def show_winLicense(self, event=None):
        self.root.Logic.show_winLicense()
        
    def hide_winLicense(self, event=None):
        self.root.Logic.hide_winLicense()
