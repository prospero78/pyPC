# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
        
    def create_disk(self):
        print 'clsLogic.create_disk()'
        self.root.GUI.winCreateDisk.show()
        
    def show_screen(self):
        self.root.GUI.winScreen.show()
        
    def run(self):
        self.GUI=self.root.GUI
        self.GUI.run()
        
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
    
    def show_winIDC(self):
        self.root.GUI.winIDC.show()
        
    def hide_winLicense(self):
        if 'lin' not in sys.platform:
            self.root.GUI.winAbout.grab_set()
