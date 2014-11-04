# -*- coding: utf8 -*-
"""
Модуль отображения текущей частоты работы процессора.
Довольно важная вещь. )
"""

from pak_pc.pak_gui.pak_widgets.mod_frm_key_value import ClsFrmKeyValue


class ClsFrmCpuFreq(ClsFrmKeyValue):
    """
    Фрейм отображения частоты ЦП.
    """
    def __init__(self, root=None):
        """
        Создание фрейма для отображения частоты ЦП.
        :param root:
        :return:
        """
        ClsFrmKeyValue.__init__(self, root=root, key='Frec', value='0 Hz')
