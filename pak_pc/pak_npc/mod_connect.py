# -*- coding: utf8 -*-
"""
Модуль предоставляет класс для сохранения данных о подключении.
"""

from Queue import Queue

class ClsNetStore(object):
    """
    Класс хранит данные о подключении.
    """
    def __init__(self, adr='localhost', port=None):
        """
        Создаёт объект сетевого подключения
        :param adr: ip-адрес соединения
        :param port: сетевой порт.
        """
        # сетевые адрес и порт
        self.conn = adr
        self.port = port

        # признак установленного подключения
        self.__connecting = False

        # создание очередей для приёма и отправки информации в дочерние
        # процессы
        self.out = Queue()
        self.in_ = Queue()

    def put (self, info=None):
        """
        Помещает информацию в исходящую очередь.
        """
        if (info is dict) and (len(info) > 1):
            self.out.append(info)

    @property
    def connecing(self):
        return self.__connecting
