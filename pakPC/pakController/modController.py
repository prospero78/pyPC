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
    
    def exit(self, event=None):
        self.root.Logic.exit()
