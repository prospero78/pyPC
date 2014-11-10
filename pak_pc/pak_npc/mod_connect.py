# -*- coding: utf8 -*-
"""
Модуль предоставляет класс для сохранения данных о подключении.
"""

class ClsStoreNetConnect:
    """
    Класс хранит данные о подключении.
    """
    def __init__(self, adr = None, port = None):
        self.adr = adr
        self.port = port
