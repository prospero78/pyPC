# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
        
    def show_screen(self):
        self.root.GUI.winScreen.show()
        
    def run(self):
        pass
        
    def exit(self):
        '''
        Общесистемный выход из программы.
        Всякие финальные действия.
        '''
        print 'clsLogic.exit()'
        self.root.GUI.winLicense.destroy()
        self.root.GUI.winAbout.destroy()
        self.root.GUI.winMain.destroy()
        sys.exit(0)
        
    def show_winLicense(self):
        self.root.GUI.winLicense.show()
        
    def hide_winLicense(self):
        if 'lin' not in sys.platform:
            self.root.GUI.winAbout.grab_set()
