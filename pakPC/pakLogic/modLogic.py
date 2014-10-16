# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
        # локальная переменная для регистра программного счётчика
        self.RegPC_old=0
        self.RegPC_val=0
        
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
        self.RegBP_act=self.GUI.winEditBP.Act.get()
        self.RegBP_adr_break=int(self.GUI.winEditBP.entAdrBreakVal.get())
        self.RegBP_adr_proc=int(self.GUI.winEditBP.entAdrProcVal.get())
        
        info={'RegBP':{'act':self.RegBP_act, 'adr_break':self.RegBP_adr_break, 'adr_proc':self.RegBP_adr_proc}}
        self.CPU.qcom.put(info)
        
        #print 'act=', self.CPU.RegBP.get_act()
        self.update_monitor()
        
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
        #self.pre_update_monitor()
        info={'com':'step()'}
        self.CPU.qcom.put(info)
        #self.post_update_monitor()
        
    def update_monitor(self):
        while not self.CPU.qinfo.empty():
            RegA=self.GUI.winMain.frmCPU.frmRegA
            info=self.CPU.qinfo.get()
            #print 'have key "RegA.val"!', info['RegA.val']
            RegA.lblVal['text']=info['RegA.val']
            #print 'have key "RegA.FlagZ"!', info['RegA.FlagZ']
            RegA.lblValZ['text']=info['RegA.FlagZ']
            #print 'have key "RegA.FlagO"!', info['RegA.FlagO']
            RegA.lblValO['text']=info['RegA.FlagO']
            #print 'have key "RegA.FlagC"!', info['RegA.FlagC']
            RegA.lblValC['text']=info['RegA.FlagO']
            #-------------------------
            #print 'have key "RegPC.val"!', info['RegPC.val']
            self.RegPC_val=info['RegPC.val']
            self.GUI.winMain.frmCPU.frmRegPC.lblVal['text']=self.RegPC_old
            self.RegPC_old=self.RegPC_val
            #---------------------------
            RegBP=self.GUI.winMain.frmCPU.frmRegBP
            #print 'have key "RegBP.act"!', info['RegBP.act']
            RegBP.lblActVal['text']=info['RegBP.act']
            #print 'have key "RegBP.adr_proc"!', info['RegBP.adr_proc']
            RegBP.lblProcVal['text']=info['RegBP.adr_proc']
            #print 'have key "RegBP.adr_break"!', info['RegBP.adr_break']
            RegBP.lblBreakVal['text']=info['RegBP.adr_break']
    
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
        self.GUI.winCreateDisk.show()
        
    def show_screen(self):
        self.root.GUI.winScreen.show()
        
    def run(self):
        self.CPU=self.root.CPU
        self.GUI=self.root.GUI
        self.Res=self.root.Res
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
            self.root.CPU.terminate()
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
