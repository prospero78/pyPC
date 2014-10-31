# -*- coding: utf8 -*-
'''
Этот модуль заточен под отображение состояния центрального процессора.
Ввиду его отдельности -- его можно втыкать куда угодно. )
'''

from Tkinter import Frame

from pak_pc.pak_gui.pak_widgets.mod_frm_reg import ClsFrmReg
from pak_pc.pak_gui.pak_widgets.mod_frm_reg_pc import ClsFrmRegPC
from pak_pc.pak_gui.pak_widgets.mod_frm_reg_sp import ClsFrmRegSP
from pak_pc.pak_gui.pak_widgets.mod_frm_cpu_frec import clsFrmCpuFreq
from pak_pc.pak_gui.pak_widgets.modFrmRegSP import clsFrmRegSP

class ClsFrmCPU(Frame):
    def __init__(self, root=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='top', fill='x')
        
        # отображаем регистр программной отладки
        self.frmreg_pc=ClsFrmRegPC(root=self)
        
        # отображаем программный счётчик
        self.frmreg_pc=ClsFrmRegPC(root=self)
        #self.frmRegA.lblName['text']='RegA'
        
        # отображаем указатель стека
        self.frmRegSP=clsFrmRegSP(root=self)
        
        # отображение регистра А
        self.frmRegA=ClsFrmReg(root=self)
        self.frmRegA.lblName['text']='RegA'
        
        # отображение частоты виртуального процессора
        self.frmCpuFreq=clsFrmCpuFreq(root=self)
