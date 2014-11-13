# -*- coding: utf8 -*-
"""
Инициализация пакета для танковой графики.
"""

from Tkinter import Tk

class clsWinMain(Tk):
    """
    Класс обеспечивает графику пользователя.
    """
    def __init__(self, my_tank=None, tank1=None, tank2=None):
        Tk.__init__(self)
        self.title('Калькулятор танков     ===build. 009===')
        self.minsize(320, 240)
        self.frmButton = clsFrmButton(root=self)
        self.frmLeft = ClsFrmLeft(root=self, my_tank=my_tank)
        self.frmRight = ClsFrmRight(root=self, tank1=tank1, tank2=tank2)
        self.after(1000, self.update_sound)
        self.mainloop()
        
    def update_sound(self):
        print 'aaa'
        self.after(1000, self.update_sound)
