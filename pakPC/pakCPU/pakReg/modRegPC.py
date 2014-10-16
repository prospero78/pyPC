# -*- coding: utf8 -*-
'''
Класс программного счётчика.
'''

class clsRegPC:
    def __init__(self, val=0, max_adr=2**24):
        self.val=val
        self.max_adr=max_adr
