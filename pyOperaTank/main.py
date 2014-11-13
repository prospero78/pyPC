# -*- coding: utf8 -*-
"""
Модуль запускает всю программу.
Продинутый вариант первого скрипта.
"""

from pakTank.modOperaTank import clsOperaTank

if True: # ведёт статистику по боям
    # статистика моего танка
    stat_my_tank = [ 312, 282, 291, 328]
    
    # статистика противников
    stat_tank1 = [0, 0, 0, 0]
    stat_tank2 = [0, 0, 0, 0]
    
    # статистика побед над мощностями
    stat_win_mosh = [517, 530, 528, 532, 522, 516, 532, 539, 518, 535]
    # статистика побед над вероятностями
    stat_win_ver =  [115, 114, 113, 112, 113, 115, 113, 112, 117, 113]

    # статистика проигрышей над мощностями
    stat_los_mosh = [535, 524, 520]
    # статистика проигрышей над вероятностями
    stat_los_ver = [113, 113, 114]

import sys
from Tkinter import LabelFrame, Entry, Label, Frame

class ClsKeyValue(Frame):
    """
    Класс обеспечивает пару "ключ:значение"
    """
    def __init__(self, root=None, key='key', value='None'):
        Frame.__init__(self, master=root, border=3, relief='groove')
        self.pack(side='top', fill='x')
        
        self.key=key
        self.value=value
        
        self.lblKey = Label(master=self, text=key)
        self.lblKey.pack(side='left', fill='x')
        
        self.entValue = Entry(master=self)
        self.entValue.pack(side='right')
        self.entValue.insert(0, value)

class ClsFrmRight(Frame):
    """
    Правый фрейм содержит всякие расчётные данные по чужим танкам.
    """
    def __init__(self, root=None, tank1=None, tank2=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='right', fill='y')
        self.lfrTank1 = ClsLfrTank(root=self, label = 'Противник 1', tank=tank1)
        self.lfrTank2 = ClsLfrTank(root=self, label = 'Противник 2', tank=tank2)

def main():
    """
    Главный запускающий скрипт.
    """
    app = clsOperaTank()
    my_tank = ClsTank()
    chuzak1 = ClsTank(atak=228,
                     bron=210,
                     toch=208,
                     proch=384,
                     name='Vrag 1')
    
    chuzak2 = ClsTank(atak=277,
                     bron=244,
                     toch=248,
                     proch=321,
                     name='Vrag 2')
    my_tank.get_result(chuzak1.mosh)
    print '#------------------------------#'
    my_tank.get_result(chuzak2.mosh)

def main_gui():
    """
    Запускается в работу по мере готовности gui.
    """
    winMain = ClsWinMain(my_tank=stat_my_tank,
                         tank1=stat_tank1,
                         tank2=stat_tank2)

if __name__ == '__main__':
    # готовность графического экрана к работе
    gui = 0

    if gui == 1:
        main_gui()
    else:
        main()
