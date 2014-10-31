# -*- coding: utf8 -*-
'''
Класс программного счётчика.
'''

class ClsRegPC:
    '''
    Класс программного счётчика обеспечивает учёт текущей инструкции системы.
    '''
    def __init__(self, val=0, max_adr=2**24):
        self.val = val
        self.max_adr = max_adr
