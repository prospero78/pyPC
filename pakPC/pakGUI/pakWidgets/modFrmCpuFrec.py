# -*- coding: utf8 -*-
'''
Модуль отображения текущей частоты работы процессора.
Довольно важная вещь. )
'''

from modFrmKeyValue import clsFrmKeyValue

class clsFrmCpuFreq(clsFrmKeyValue):
    def __init__(self, root=None):
        clsFrmKeyValue.__init__(self, root=root, key='Frec', value='0 Hz')
