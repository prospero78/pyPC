# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class clsLogic:
    def __init__(self, root=None):
        self.root=root
        # локальная переменная для регистра программного счётчика
        self.reg_pc_old=0
        self.reg_pc_val=0
        # признаки запущенности ЦП в debug mode
        self.debug=0
    
    def set_Res_str(self):
        '''
        Присваивает строковые ресурсы графическому интерфейсу.
        Процедура сделана с целью отвязки GUI от ресурсов
        (повышение атомарности класса).
        '''
        winMain=self.GUI.winMain
        winMain.btnStep['text']=self.Res.winMain_btnStep
        winMain.btnDebug['text']=self.Res.winMain_btnDebug_0
        winMain.btnExit['text']=self.Res.winMain_btnExit_name
        winMain.btnShowScreen['text']=self.Res.winMain_btnShowScreen_show
        winMain.btnReset['text']=self.root.Res.winMain_btnReset
        winMain.mbtFile['text']=self.Res.winMain_mbtFile_name
        winMain.mbtEdit['text']=self.Res.winMain_mbtEdit_name
        winMain.mbtCustom['text']=self.Res.winMain_mbtCustom_name
        winMain.frmCPU.frmCpuFreq.lblKey['text']=self.Res.winMain_frmCpuFreq_lblKey
        
    def reset_pc(self):
        '''
        Сброс состояния виртуального компьютера.
        '''
        info={'com':'reset'}
        self.CPU.qcom.put(info)
        
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
        #self.GUI.winMain.update()
        
    def winEditBP_hide(self):
        print '  clsLogic.winEditBP_hide()'
        #------- обновить содержимое реального регистра программных прерываний --------
        self.reg_pc_act=self.GUI.winEditBP.Act.get()
        self.reg_pc_adr_break=int(self.GUI.winEditBP.entAdrBreakVal.get())
        self.reg_pc_adr_proc=int(self.GUI.winEditBP.entAdrProcVal.get())
        
        info={'reg_pc':{'act':self.reg_pc_act, 'adr_break':self.reg_pc_adr_break, 'adr_proc':self.reg_pc_adr_proc}}
        self.CPU.qcom.put(info)
        
        #print 'act=', self.CPU.reg_pc.get_act()
        #self.update_monitor()
        
    def show_winEditBP(self):
        #print 'clsLogic.show_winEditBP()'
        self.GUI.winEditBP.show()
       
    def debug_CPU(self):
        #print 'clsLogic.debug_CPU()'
        if self.debug==0:
            self.debug=1
            self.GUI.winMain.btnDebug['text']=self.Res.winMain_btnDebug_1
            info={'com':'debug(on)'}
        else:
            self.debug=0
            self.GUI.winMain.btnDebug['text']=self.Res.winMain_btnDebug_0
            info={'com':'debug(off)'}
        self.CPU.qcom.put(info)
       
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
            info=self.CPU.qinfo.get()
            if info.has_key('RegA'):
                inf=info['RegA']
                #print 'detect RegA', inf
                RegA=self.GUI.winMain.frmCPU.frmRegA
                #print 'have key "RegA.val"!', info['RegA.val']
                RegA.lblVal['text']=inf['val']
                #print 'have key "RegA.FlagZ"!', info['RegA.FlagZ']
                RegA.lblValZ['text']=inf['FlagZ']
                #print 'have key "RegA.FlagO"!', info['RegA.FlagO']
                RegA.lblValO['text']=inf['FlagO']
                #print 'have key "RegA.FlagC"!', info['RegA.FlagC']
                RegA.lblValC['text']=inf['FlagO']
            if info.has_key('reg_pc'):
                inf=info['reg_pc']
                #print 'detect reg_pc', inf
                #print 'have key "reg_pc.val"!', info['reg_pc.val']
                self.reg_pc_val=inf['val']
                self.GUI.winMain.frmCPU.frmreg_pc.lblVal['text']=self.reg_pc_old
                self.reg_pc_old=self.reg_pc_val
            #---------------------------
            if info.has_key('reg_pc'):
                inf=info['reg_pc']
                reg_pc=self.GUI.winMain.frmCPU.frmreg_pc
                #print 'have key "reg_pc.act"!', info['reg_pc.act']
                reg_pc.lblActVal['text']=inf['act']
                #print 'have key "reg_pc.adr_proc"!', info['reg_pc.adr_proc']
                reg_pc.lblProcVal['text']=inf['adr_proc']
                #print 'have key "reg_pc.adr_break"!', info['reg_pc.adr_break']
                reg_pc.lblBreakVal['text']=inf['adr_break']
            #---------------------------
            if info.has_key('RegSP'):
                inf=info['RegSP']
                RegSP=self.GUI.winMain.frmCPU.frmRegSP
                RegSP.lblAdrVal['text']=inf['adr']
                RegSP.lblValVal['text']=inf['val']
            #---------------------------
            if info.has_key('debug'):
                inf=info['debug']
                #print 'detect DEBUG', inf
            #---------------------------
            if info.has_key('dtime'):
                inf=info['dtime']
                #print 'detect DTIME', inf
                self.update_speed(dtime=inf)
        while not self.Video.vout.empty():
            vout=self.Video.vout.get()
            self.winScreen.lblScreen['text']=vout
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
        if not self.GUI.winScreen.winScreen_show:
            self.GUI.winScreen.show()
        else:
            self.GUI.winScreen.destroy()
    def run(self):
        self.CPU=self.root.CPU
        self.GUI=self.root.GUI
        self.winScreen=self.GUI.winScreen
        self.Res=self.root.Res
        self.Video=self.root.Video
        self.Video.start()
        self.CPU.start()
        
        info={'com':'get_info()'}
        self.CPU.qcom.put(info)
        
        # присвоение строковых ресурсов
        self.set_Res_str()
        
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
            self.root.Video.terminate()
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
