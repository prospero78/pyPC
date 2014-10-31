# -*- coding: utf8 -*-
'''
Главный класс общей логики
'''
import sys
class ClsLogic:
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
        winMain=self.gui.winMain
        winMain.btnStep['text']=self.res.winMain_btnStep
        winMain.btnDebug['text']=self.res.winMain_btnDebug_0
        winMain.btnExit['text']=self.res.winMain_btnExit_name
        winMain.btnShowScreen['text']=self.res.winMain_btnShowScreen_show
        winMain.btnReset['text']=self.root.res.winMain_btnReset
        winMain.mbtFile['text']=self.res.winMain_mbtFile_name
        winMain.mbtEdit['text']=self.res.winMain_mbtEdit_name
        winMain.mbtCustom['text']=self.res.winMain_mbtCustom_name
        winMain.frmCPU.frmCpuFreq.lblKey['text']=self.res.winMain_frmCpuFreq_lblKey
        
    def reset_pc(self):
        '''
        Сброс состояния виртуального компьютера.
        '''
        info={'com':'reset'}
        self.cpu.qcom.put(info)
        
    def update_speed(self, dtime=0):
        '''
        При отладке обновляет периодически монитор состояния ЦП и скорость виртуальной машины.
        '''
        fr=1.0/dtime*self.cpu.time_code
        #print dtime, self.cpu.frec
        res=fr/self.cpu.frec
        if res>1.1 or res<0.9:
            if fr>self.cpu.frec:
                self.cpu.frec=self.cpu.frec+int(fr/100)
            elif fr<self.cpu.frec:
                self.cpu.frec=self.cpu.frec-int(fr/100)
            if fr>1000:
                fr=str(int(self.cpu.frec/1000))+' kHz'
            else:
                fr=str(int(self.cpu.frec))+' Hz'
            frec=self.gui.winMain.frmCPU.frmCpuFrec
            frec.entVal.delete(0,'end')
            frec.entVal.insert(0, fr)
        #self.gui.winMain.update()
        
    def winEditBP_hide(self):
        print '  ClsLogic.winEditBP_hide()'
        #------- обновить содержимое реального регистра программных прерываний --------
        self.reg_pc_act=self.gui.winEditBP.Act.get()
        self.reg_pc_adr_break=int(self.gui.winEditBP.entAdrBreakVal.get())
        self.reg_pc_adr_proc=int(self.gui.winEditBP.entAdrProcVal.get())
        
        info={'reg_pc':{'act':self.reg_pc_act, 'adr_break':self.reg_pc_adr_break, 'adr_proc':self.reg_pc_adr_proc}}
        self.cpu.qcom.put(info)
        
        #print 'act=', self.cpu.reg_pc.get_act()
        #self.update_monitor()
        
    def show_winEditBP(self):
        #print 'ClsLogic.show_winEditBP()'
        self.gui.winEditBP.show()
       
    def debug_CPU(self):
        #print 'ClsLogic.debug_CPU()'
        if self.debug==0:
            self.debug=1
            self.gui.winMain.btnDebug['text']=self.res.winMain_btnDebug_1
            info={'com':'debug(on)'}
        else:
            self.debug=0
            self.gui.winMain.btnDebug['text']=self.res.winMain_btnDebug_0
            info={'com':'debug(off)'}
        self.cpu.qcom.put(info)
       
    def step_CPU(self):
        '''
        Метод исполняет шаг процессора с выводом результата.
        Команды отправляются в очередь между процессами.
        '''
        #print 'ClsLogic.step_CPU()'
        #self.pre_update_monitor()
        info={'com':'step()'}
        self.cpu.qcom.put(info)
        #self.post_update_monitor()
        
    def update_monitor(self):
        while not self.cpu.qinfo.empty():
            info=self.cpu.qinfo.get()
            if info.has_key('RegA'):
                inf=info['RegA']
                #print 'detect RegA', inf
                RegA=self.gui.winMain.frmCPU.frmRegA
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
                self.gui.winMain.frmCPU.frmreg_pc.lblVal['text']=self.reg_pc_old
                self.reg_pc_old=self.reg_pc_val
            #---------------------------
            if info.has_key('reg_pc'):
                inf=info['reg_pc']
                reg_pc=self.gui.winMain.frmCPU.frmreg_pc
                #print 'have key "reg_pc.act"!', info['reg_pc.act']
                reg_pc.lblActVal['text']=inf['act']
                #print 'have key "reg_pc.adr_proc"!', info['reg_pc.adr_proc']
                reg_pc.lblProcVal['text']=inf['adr_proc']
                #print 'have key "reg_pc.adr_break"!', info['reg_pc.adr_break']
                reg_pc.lblBreakVal['text']=inf['adr_break']
            #---------------------------
            if info.has_key('RegSP'):
                inf=info['RegSP']
                RegSP=self.gui.winMain.frmCPU.frmRegSP
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
        self.gui.winCreateDisk.destroy()
        disk_size=int(self.gui.winCreateDisk.fkvSize.get_val())
        disk_name=self.gui.winCreateDisk.fkvName.get_val()
        str_='\0'*(2**10)
        f=open('./data/'+disk_name+'.dsk','wb')
        for i in xrange(0, disk_size):
            f.write(str_)
        f.close()
        
    def create_new_disk(self):
        #TODO: дописать процедуру создания нового диска
        pass
    
    def create_disk(self):
        print 'ClsLogic.create_disk()'
        self.gui.winCreateDisk.show()
        
    def show_screen(self):
        if not self.gui.winScreen.winScreen_show:
            self.gui.winScreen.show()
        else:
            self.gui.winScreen.destroy()
    def run(self):
        self.cpu=self.root.cpu
        self.gui=self.root.gui
        self.winScreen=self.gui.winScreen
        self.res=self.root.res
        self.Video=self.root.Video
        self.Video.start()
        self.cpu.start()
        
        info={'com':'get_info()'}
        self.cpu.qcom.put(info)
        
        # присвоение строковых ресурсов
        self.set_Res_str()
        
        self.gui.run()
        
    def exit(self):
        '''
        Общесистемный выход из программы.
        Всякие финальные действия.
        '''
        #print 'ClsLogic.exit()'
        try:
            self.root.gui.winEditBP.win_exit()
            self.root.gui.winScreen.win_exit()
            self.root.gui.winLicense.win_exit()
            self.root.gui.winIDC.win_exit()
            self.root.gui.winCreateDisk.win_exit()
            self.root.gui.winAbout.win_exit()
            self.root.gui.winMain.win_exit()
            self.root.cpu.terminate()
            self.root.Video.terminate()
            del self.root.cpu
        finally:
            sys.exit(0)
        
    def show_winLicense(self):
        self.root.gui.winLicense.show()
    
    def show_winIDC(self):
        self.root.gui.winIDC.show()
        
    def hide_winLicense(self):
        if 'lin' not in sys.platform:
            self.root.gui.winAbout.grab_set()
