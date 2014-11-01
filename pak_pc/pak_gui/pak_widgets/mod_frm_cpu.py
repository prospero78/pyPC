# -*- coding: utf8 -*-
'''
Этот модуль заточен под отображение состояния центрального процессора.
Ввиду его отдельности -- его можно втыкать куда угодно. )
'''

from Tkinter import Frame

from pak_pc.pak_gui.pak_widgets.mod_frm_reg import ClsFrmReg
from pak_pc.pak_gui.pak_widgets.mod_frm_reg_pc import ClsFrmRegPC
from pak_pc.pak_gui.pak_widgets.mod_frm_reg_bp import ClsFrmRegBP
from pak_pc.pak_gui.pak_widgets.mod_frm_cpu_frec import ClsFrmCpuFreq
from pak_pc.pak_gui.pak_widgets.mod_frm_reg_sp import ClsFrmRegSP

class ClsFrmCPU(Frame):
    def __init__(self, root=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='top', fill='x')
        
        # отображаем регистр программной отладки
        self.frm_reg_bp=ClsFrmRegBP(root=self)
        
        # отображаем программный счётчик
        self.frm_reg_pc=ClsFrmRegPC(root=self)
        #self.frm_reg_a.lbl_name['text']='reg_a'
        
        # отображаем указатель стека
        self.frm_reg_sp=ClsFrmRegSP(root=self)
        
        # отображение регистра А
        self.frm_reg_a=ClsFrmReg(root=self)
        self.frm_reg_a.lbl_name['text']='reg_a'
        
        # отображение частоты виртуального процессора
        self.frm_cpu_freq=ClsFrmCpuFreq(root=self)
