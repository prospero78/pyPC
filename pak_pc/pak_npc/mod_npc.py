# -*- coding: utf8 -*-
"""
Модуль предоставляющий класс для работы хост-процесса с
множеством процессов по сети. Это будет
универсальное и переносимое решение.
"""

import socket
from threading import Thread
from time import sleep
from pak_pc.pak_npc.mod_connect import ClsNetStore

#--- определение сетевых подключений ---
HOST_VIDEO = "" # localhost

# порт, на который должно прийти подключение от видеокарты.
PORT_VIDEO = 58633

class ClsNPC(Thread):
    """
    Класс обеспечивает взаимодействие различных частей python и cython
    кода через различные процессы.
    Использование мультипроцессинга напрямую вызывает дикие проблемы.
    """
    def __init__(self):
        """
        обеспечивает инициализацию класса сетевых межпроцессорных
        взаимодействий
        :return: возвращает ссылку на себя.
        """

        def get_video_connect():
            """
            Устанавливает соединение видеокарты.
            """

            # --- создание сервера для подключения
            srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #srv.settimeout(5)

            #--- запуск сервера ---
            srv.bind((HOST_VIDEO, PORT_VIDEO))
            # сколько можно одновременно получить подключений на порт
            srv.listen(1)
            # ждём когда подкючится клиент видеокарты
            self.video.port, self.video.adr = srv.accept()

        def get_cpu_connect():
            """
            Устанавливает соединение с ЦП.
            """
            pass

        Thread.__init__(self)
        self.video = ClsNetStore()
        self.cpu = ClsNetStore()

        # -- признак подключения видеокарты ---
        self.video_connect = False

        # -- признак подключения ЦП ---
        self.cpu_connect = False

        # --- получить подключение от видеокарты ---
        get_video_connect()
        get_cpu_connect()

    def run(self):
        """
        Метод исполняется при запуске отдельного потока.
        Метод зациклен.
        """

        def send_info():
            """
            Отправляет сообщения из очередей сообщений.
            """
            pass

        def get_info():
            """
            Получает сообщения по сети и ставит в очередь обработки.
            """

        #--- счётчик циклов и цикл
        count_loop = 0

        # получить имя системы и счётчик циклов
        print 'Name = ', self.getName(), count_loop
        print "Слушаю порт".decode('utf8'), PORT_VIDEO

        while 1:
            pal = sock.recv(1024) # получить данные
            if not pal: # если данных нет -- не продолжать
                print 'Not reada net data'
            else:
                print "Получено от %s:%s:" % addr, pal
                lap = do_something(pal)
                print "Отправлено %s:%s:" % addr, lap
                sock.send(lap)
                sock.close()
                sleep(1)
                count_loop += 1

if __name__ == '__main__':
    APP = ClsNPC()
    APP.start()
