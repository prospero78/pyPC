# -*- coding: utf8 -*-
"""
Модуль описывающий свойства танка.
"""

class clsTank(object):
    def __init__(self,
                 atak=0,
                 bron=0,
                 toch=0,
                 proch=0,
                 name='clsTank'):
        # сила атаки
        self.atak = atak * 1.0
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
        
    def __get_mosh(self):
        """
        Спец метод для расчёта мощности танка
        """
        
        # расчёное значение мощности
        mosh_qw = 0
        mosh_qw += self.atak**2
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
