# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
        
    def show_winEditBP(self):
        print 'clsLogic.show_winEditBP()'
       
    def debug_CPU(self):
        print 'clsLogic.debug_CPU()'
       
    def step_CPU(self):
        '''
        Метод исполняет шаг процессора с выводом результата.
        '''
        print 'clsLogic.step_CPU()'
        self.CPU.step()
        self.update_monitor()
        
    def update_monitor(self):
        RegA=self.GUI.winMain.frmCPU.frmRegA
        RegA.lblVal['text']=self.CPU.RegA.val
        RegA.lblValZ['text']=self.CPU.RegA.FlagZ
        RegA.lblValO['text']=self.CPU.RegA.FlagO
        RegA.lblValC['text']=self.CPU.RegA.FlagC
        #-------------------------
        self.GUI.winMain.frmCPU.frmRegPC.lblVal['text']=self.CPU.RegPC.val
        #-------------------------
        RegBP=self.GUI.winMain.frmCPU.frmRegBP
        RegBP.lblActVal['text']=self.CPU.RegBP.act
        RegBP.lblProcVal['text']=self.CPU.RegBP.adr_proc
        RegBP.lblProcVal['text']=self.CPU.RegBP.adr_break
   
    def load_bios(self):
        '''
        Загружает BIOS по умолчанию.
        BIOS содержится в py-файле, обычный хитрый словарь.
        '''
        Bios=self.Res.Bios
        for i in Bios.data:
            print i, Bios.data[i], '\n'
            self.CPU.Mem.adr[i]=Bios.data[i]
        
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
        self.CPU=self.root.CPU
        self.GUI=self.root.GUI
        self.Res=self.root.Res
        self.load_bios()
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
