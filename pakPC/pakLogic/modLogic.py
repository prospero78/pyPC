# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
       
    def load_bios(self):
        '''
        Загружает BIOS по умолчанию.
        BIOS находится в файле './data/bios.csv'
        Имеет формат реального csv файла для облегчения чтения и парсинга
        '''
        print 'clsLogic.load_bios()'
        f=open('./data/bios.csv', 'r')
        biso_csv=f.read()
        f.close()
        
    
    def generate_new_disk(self):
        print 'generate_new_disk()'
        self.GUI.winCreateDisk.destroy()
        disk_size=int(self.GUI.winCreateDisk.fkvSize.get_val())
        disk_name=self.GUI.winCreateDisk.fkvName.get_val()
        str_='\0'*(2**10)
        f=open('./data/'+disk_name+'.dsk','wb')
        for i in xrange(0, disk_size):
            f.write(str_)
        f.close()
        
    def create_new_disk(self):
        #TODO: дописать процедуру создания нового диска
        pass
    
    def create_disk(self):
        print 'clsLogic.create_disk()'
        self.root.GUI.winCreateDisk.show()
        
    def show_screen(self):
        self.root.GUI.winScreen.show()
        
    def run(self):
        self.load_bios()
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
