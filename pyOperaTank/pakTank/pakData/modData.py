# -*- coding: utf8 -*-
"""
Модуль хранения танковых данных.
"""

import shelve

class clsData(object):
    """
    Класс обеспечивает хранение, чтение, запись всех данных
    по танковым боям.
    """
    def __init__(self):
        """
        Считывает в память все данные по боям.
        """
        def base_read():
            """
            Читает данные из базы.
            Если её нет -- создаёт.
            """
            self.base = shelve.open('./pakTank/pakData/tank_data.db')
            
            if self.base.has_key('my_tank'):
                self.my_tank = self.base['my_tank']
            else:
                self.my_tank={}
                self.base['my_tank'] = {}
                self.base.sync()
        self.base = None
        base_read()
    
    def close_base(self):
        self.base.close()
        print '   [tank_data.db close]'
