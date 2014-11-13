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
            
            
            # проверка пароля на базу данных
            if self.base.has_key('pass'):
                pas1 = self.base['pass']
                pas2 = ''
                i=0
                while pas1 != pas2:
                    pas2 = raw_input('Plis input password:')
                    i += 1
                    if i > 3:
                        print '  [ERROR] aborting load tank_base.db'
                        import sys
                        sys.exit()
            else:
                pas1 = ''
                pas2 = ' '
                while pas1 != pas2 and len(pas1) < 6:
                    print 'password mininmum 6 symbol!!!'
                    pas1 = raw_input('Plis input password:')
                    pas2 = raw_input('Plis confirm password:')
                self.base['pass'] = pas1
            
            if self.base.has_key('my_tank'):
                self.my_tank = self.base['my_tank']
            else:
                self.my_tank={}
                tank={'name':'my tank',
                      'atak': 0,
                      'bron': 0,
                      'toch': 0,
                      'proch': 0,}
            
                self.base['my_tank'] = {}
                self.base.sync()
        self.base = None
        base_read()
    
    def close_base(self):
        self.base.close()
        print '   [tank_data.db close]'
