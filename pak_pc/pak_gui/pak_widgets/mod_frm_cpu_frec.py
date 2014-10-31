# -*- coding: utf8 -*-
'''
Модуль отображения текущей частоты работы процессора.
Довольно важная вещь. )
'''

from mod_frm_key_value import ClsFrmKeyValue

class ClsFrmCpuFreq(ClsFrmKeyValue):
    def __init__(self, root=None):
        ClsFrmKeyValue.__init__(self, root=root, key='Frec', value='0 Hz')
