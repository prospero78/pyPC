# -*- coding: utf8 -*-
"""
Класс памяти. Будем со временем дорабатывать.
"""
DEF MAX_ADR=2 ** 22
cdef struc Mem:
    int adr[MAX_ADR]

cdef class ClsMemory:
    """
    Описывает память в виде болчного устройства.
    """
    cdef public Mem *mem
    def __init__(self, int max_adr=2 ** 22):
        """
        Начальная инициализация памяти.
        :param max_adr:
        :return:
        """
        # максимально допустимое количество памяти
        self.max_adr = max_adr
        # текущее количество памяти
        self.act_mem = 1024
        # инициализация памяти виртуального компьютера
        self.adr = {}
        cdef int i = 0
        for i in xrange(0, self.act_mem):
            self.adr[i] = 0

    def get_adr(self, adr):
        """
        Возвращает значение ячейки памяти по адресу (для cython)
        :param adr:
        :return:
        """
        return self.adr[adr]

    def set_adr(self, adr, val):
        """
        Устанавливает ячейку памяти в значение. (для cython)
        :param adr:
        :param val:
        :return:
        """
        self.adr[adr] = val

    def get_max_adr(self):
        """
        Возвращает максимально-доступный адрес памяти.
        Выше его быть памяти в любом случае не может.
        :return:
        """
        return self.max_adr

    def add_memory(self):
        """
        Добавляет памяти блоками по 1024 ячейки (НЕ БАЙТА!!!)
        :return:
        """
        if self.act_mem < self.max_adr - 1024:
            for i in xrange(self.act_mem, self.act_mem + 1024):
                self.adr[i] = 0
            self.act_mem += 1024
