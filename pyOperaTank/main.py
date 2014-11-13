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
from Tkinter import Tk, LabelFrame, Entry, Label, Frame, Button

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
        

class ClsLfrTank(LabelFrame):
    """
    Класс создаёт фрейм для редактирования характеристик танка.
    """
    def __init__(self, root=None,
                 label='MyTank',
                 tank=None):
        LabelFrame.__init__(self,
                            master=root,
                            text = label,
                            border=3,
                            relief='raised',
                            font='Consolas 12 bold')
        self.pack(side='top', fill='y')
        
        self.kvAtak = ClsKeyValue(root=self, key='Атака', value=tank[0])
        self.kvBron = ClsKeyValue(root=self, key='Броня', value=tank[1])
        self.kvBron = ClsKeyValue(root=self, key='Точность', value=tank[2])
        self.kvBron = ClsKeyValue(root=self, key='Прочность', value=tank[3])
        self.kvMosh = ClsKeyValue(root=self, key='Мощность*', value='?')


class ClsFrmButton(Frame):
    """
    Класс добавляет фрейм с кнопками для пересчёта значений.
    """
    def __init__(self, root=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='bottom', fill='x')
        
        self.btnExit = Button(self, text='Выход', command=lambda:(sys.exit()))
        self.btnExit.pack(side='right')
        
        self.btnCalc = Button(self, text='Пересчёт')
        self.btnCalc.pack(side='right')

class ClsFrmLeft(Frame):
    """
    Левый фрейм содержит всякие расчётные данные по своему танку.
    """
    def __init__(self,
                 root=None,
                 my_tank=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='left', fill='y')
        self.lfrMyTank = ClsLfrTank(root=self,
                                    label = 'Мой танк',
                                    tank=my_tank)
        self.lfrMyTank.kvVer1 = ClsKeyValue(root=self.lfrMyTank,
                                            key='Вероятность 1*',
                                            value='?')
        self.lfrMyTank.kvVer2 = ClsKeyValue(root=self.lfrMyTank,
                                            key='Вероятность 2*',
                                            value='?')

class ClsFrmRight(Frame):
    """
    Правый фрейм содержит всякие расчётные данные по чужим танкам.
    """
    def __init__(self, root=None, tank1=None, tank2=None):
        Frame.__init__(self, master=root, border=3, relief='sunken')
        self.pack(side='right', fill='y')
        self.lfrTank1 = ClsLfrTank(root=self, label = 'Противник 1', tank=tank1)
        self.lfrTank2 = ClsLfrTank(root=self, label = 'Противник 2', tank=tank2)

class ClsWinMain(Tk):
    """
    Класс обеспечивает графику пользователя.
    """
    def __init__(self, my_tank=None, tank1=None, tank2=None):
        Tk.__init__(self)
        self.title('Калькулятор танков     ===build. 009===')
        self.minsize(320, 240)
        self.frmButton = ClsFrmButton(root=self)
        self.frmLeft = ClsFrmLeft(root=self, my_tank=my_tank)
        self.frmRight = ClsFrmRight(root=self, tank1=tank1, tank2=tank2)
        self.after(1000, self.update_sound)
        self.mainloop()
        
    def update_sound(self):
        print 'aaa'
        self.after(1000, self.update_sound)

class ClsTank(object):
    def __init__(self, atak=312, bron=282, toch=291, proch=328, name='My tank'):
        # сила атаки
        self.atak = atak * 1.0
        # броня
        self.bron = bron
        # точность стрельбы
        self.toch = toch
        # прочность танка
        self.proch = proch
        # общая характеристика
        self.mosh = (self.atak**2 + self.bron**2 + self.toch**2 + self.proch**2)**0.5
        print 'Name:', name, '\tmosh=', int(self.mosh)
        
    def get_result(self, mosh=0):
        """
        Процедурка высчитывает примерный результат боя.
        Вероятность в процентах.
        """
        res = self.mosh / mosh * 100
        
        print 'Isxod=', int(res), '%'
        if res < 112:
            print 'not recomended'
        else:
            print 'recomended! )))'
        
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
