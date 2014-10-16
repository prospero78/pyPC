# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
        
    def update_speed(self, dtime=0):
        '''
        При отладке обновляет периодически монитор состояния ЦП и скорость виртуальной машины.
        '''
        fr=1.0/dtime*self.CPU.time_code
        #print dtime, self.CPU.frec
        res=fr/self.CPU.frec
        if res>1.1 or res<0.9:
            if fr>self.CPU.frec:
                self.CPU.frec=self.CPU.frec+int(fr/100)
            elif fr<self.CPU.frec:
                self.CPU.frec=self.CPU.frec-int(fr/100)
            if fr>1000:
                fr=str(int(self.CPU.frec/1000))+' kHz'
            else:
                fr=str(int(self.CPU.frec))+' Hz'
            frec=self.GUI.winMain.frmCPU.frmCpuFrec
            frec.entVal.delete(0,'end')
            frec.entVal.insert(0, fr)
        self.GUI.winMain.update()
        
    def winEditBP_hide(self):
        print '  clsLogic.winEditBP_hide()'
        #------- обновить содержимое реального регистра программных прерываний --------
        self.CPU.RegBP.set_act(self.GUI.winEditBP.Act.get())
        self.CPU.RegBP.set_adr_break(int(self.GUI.winEditBP.entAdrBreakVal.get()))
        self.CPU.RegBP.set_adr_proc(int(self.GUI.winEditBP.entAdrProcVal.get()))
        print 'act=', self.CPU.RegBP.get_act()
        self.post_update_monitor()
        
    def show_winEditBP(self):
        #print 'clsLogic.show_winEditBP()'
        self.GUI.winEditBP.show()
       
    def debug_CPU(self):
        #print 'clsLogic.debug_CPU()'
        self.CPU.debug()
       
    def step_CPU(self):
        '''
        Метод исполняет шаг процессора с выводом результата.
        Команды отправляются в очередь между процессами.
        '''
        #print 'clsLogic.step_CPU()'
        self.pre_update_monitor()
        self.CPU.qcom.put('step()')
        #self.post_update_monitor()
    
    def pre_update_monitor(self):
        self.GUI.winMain.frmCPU.frmRegPC.lblVal['text']=self.CPU.RegPC.val
        
    def post_update_monitor(self):
        RegA=self.GUI.winMain.frmCPU.frmRegA
        while not self.CPU.qinfo.empty():
            info=self.CPU.qinfo.get()
            if info.has_key('RegA.val'):
                RegA.lblVal['text']=info['RegA.val']
        
        RegA.lblValZ['text']=self.CPU.RegA.FlagZ
        RegA.lblValO['text']=self.CPU.RegA.FlagO
        RegA.lblValC['text']=self.CPU.RegA.FlagC
        #-------------------------
        RegBP=self.GUI.winMain.frmCPU.frmRegBP
        RegBP.lblActVal['text']=self.CPU.RegBP.get_act()
        RegBP.lblProcVal['text']=self.CPU.RegBP.get_adr_proc()
        RegBP.lblBreakVal['text']=self.CPU.RegBP.get_adr_break()
   
    def load_bios(self):
        '''
        Загружает BIOS по умолчанию.
        BIOS содержится в py-файле, обычный хитрый словарь.
        '''
        Bios=self.Res.Bios
        for i in Bios.data:
            print i, Bios.data[i], '\n'
            self.CPU.Mem.set_adr(i, Bios.data[i])
        
    def generate_new_disk(self):
        #print 'generate_new_disk()'
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
        #print 'clsLogic.exit()'
        try:
            self.root.GUI.winEditBP.win_exit()
            self.root.GUI.winScreen.win_exit()
            self.root.GUI.winLicense.win_exit()
            self.root.GUI.winIDC.win_exit()
            self.root.GUI.winCreateDisk.win_exit()
            self.root.GUI.winAbout.win_exit()
            self.root.GUI.winMain.win_exit()
            del self.root.CPU
        finally:
            sys.exit(0)
        
    def show_winLicense(self):
        self.root.GUI.winLicense.show()
    
    def show_winIDC(self):
        self.root.GUI.winIDC.show()
        
    def hide_winLicense(self):
        if 'lin' not in sys.platform:
            self.root.GUI.winAbout.grab_set()
