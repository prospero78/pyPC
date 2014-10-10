# -*- coding: utf8 -*-
'''
Класс программного счётчика.
'''

class clsRegPC:
    def __init__(self, root=None, val=0, max_adr=2**24):
        self.root=root
        self.val=val
        self.max_adr=max_adr
