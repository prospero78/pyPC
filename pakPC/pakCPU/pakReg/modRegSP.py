# -*- coding: utf8 -*-
'''
Класс указателя стека.
'''

class clsRegSP:
    def __init__(self, root=None, val=2**24, min_adr=0):
        self.root=root
        self.val=val
        self.min_adr=min_adr
