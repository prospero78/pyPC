# -*- coding: utf8 -*-
'''
Этот модуль заточен под отображение состояния центрального процессора.
Ввиду его отдельности -- его можно втыкать куда угодно. )
'''

from Tkinter import Frame

from pakPC.pakGUI.pakWidgets.modFrmReg import clsFrmReg
from pakPC.pakGUI.pakWidgets.modFrmreg_pc import clsFrmreg_pc
from pakPC.pakGUI.pakWidgets.modFrmreg_pc import clsFrmreg_pc
from pakPC.pakGUI.pakWidgets.modFrmCpuFrec import clsFrmCpuFreq
from pakPC.pakGUI.pakWidgets.modFrmRegSP import clsFrmRegSP

class clsFrmCPU(Frame):
    def __init__(self, root=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='top', fill='x')
        
        # отображаем регистр программной отладки
        self.frmreg_pc=clsFrmreg_pc(root=self)
        
        # отображаем программный счётчик
        self.frmreg_pc=clsFrmreg_pc(root=self)
        #self.frmRegA.lblName['text']='RegA'
        
        # отображаем указатель стека
        self.frmRegSP=clsFrmRegSP(root=self)
        
        # отображение регистра А
        self.frmRegA=clsFrmReg(root=self)
        self.frmRegA.lblName['text']='RegA'
        
        # отображение частоты виртуального процессора
        self.frmCpuFreq=clsFrmCpuFreq(root=self)
