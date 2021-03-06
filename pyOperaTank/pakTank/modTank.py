# -*- coding: utf8 -*-
"""
Модуль описывающий свойства танка.
"""

class clsTank(object):
    """
    Описывает общий класс танка.
    """
    def __init__(self,
                 atak=0,
                 bron=0,
                 toch=0,
                 proch=0,
                 name='clsTank'):
        # сила атаки
        self.atak_ = atak
        # броня
        self.bron = bron
        # точность стрельбы
        self.toch = toch
        # прочность танка
        self.proch = proch
        # общая характеристика
        self.__mosh = 0
        # имя танка
        self.name = name
        self.__get_mosh()
    
    
    @property
    def atak(self):
        return self.atak_
    
    @atak.setter
    def atak(self, value=None):
        print 'value=', value, 'type=', type(value)
        value = int(value)
        self.atak_ = value
        print 'clsTank.atak=', self.atak_
        #except:
        #    print 'clsTank: invalid value for atak! value=', value, 'type=', type(value)
    def __get_mosh(self):
        """
        Спец метод для расчёта мощности танка
        """
        
        # расчёное значение мощности
        mosh_qw = 0
        mosh_qw += self.atak_**2
        mosh_qw += self.bron**2
        mosh_qw += self.toch**2
        mosh_qw += self.proch**2
        self.__mosh = mosh_qw**0.5
        print 'Name:', self.name, '\tmosh=', int(self.__mosh)
        
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
            
    @property
    def mosh(self):
        """
        Расчётное свойство. Доступно только для чтения.
        """
        self.__get_mosh()
        return self.__mosh 
