# -*- coding: utf8 -*-
'''
Класс указателя стека.

val -- максимальное значение регистра. 
Устанавливается по количеству максимальной допустимой памяти.

min_adr -- дно стека.
'''

class clsRegSP:
    def __init__(self, val=None, min_adr=None):
        self.val=val
        self.min_adr=min_adr
