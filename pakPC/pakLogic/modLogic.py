# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
        
    def run(self):
        pass
        
    def exit(self):
        '''
        Общесистемный выход из программы.
        Всякие финальные действия.
        '''
        print 'clsLogic.exit()'
        self.root.GUI.winAbout.destroy()
        self.root.GUI.winMain.destroy()
        sys.exit(0)
