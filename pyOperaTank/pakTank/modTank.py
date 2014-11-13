# -*- coding: utf8 -*-
"""
Модуль описывающий свойства танка.
"""

class ClsTank(object):
    def __init__(self, atak=0, bron=0, toch=0, proch=0, name='clsTank'):
        # сила атаки
        self.atak = atak * 1.0
        # броня
        self.bron = bron
        # точность стрельбы
        self.toch = toch
        # прочность танка
        self.proch = proch
        # общая характеристика
        mosh_qw = 0
        mosh_qw += self.atak**2
        mosh_qw += self.bron**2
        mosh_qw += self.toch**2
        mosh_qw += self.proch**2
        self.mosh = mosh_qw**0.5
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
