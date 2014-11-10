# -*- coding: utf8 -*-
"""
Модуль предоставляющий класс для универсальной работы с
множеством процессов по сетевому стеку. Это будет
универсальное и переносимое решение.
"""

from socket import socket
from threading import Thread
from time import sleep


class ClsIPC(Thread):
    """
    Класс обеспечивает взаимодействие различных частей python и снерщт кода через различные процессы.
    """
    def __init__ (self):
        """
        обеспечивает инициализацию класса сетевых межпроцессорных взаимодействий
        :return: возвращает ссылку на себя.
        """
        Thread.__init__(self)
        self.start()
        self.socket = None

    def run(self):
        i = 0
        while True:
            print self.getName(), i
            sleep(1)
            i += 1


