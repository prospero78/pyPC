# -*- coding: utf8 -*-
"""
Модуль предоставляющий класс для работы хост-процесса с
множеством процессов по сети. Это будет
универсальное и переносимое решение.
"""

import socket
from threading import Thread
from Queue import Queue
from time import sleep


class ClsNPC(Thread):
    """
    Класс обеспечивает взаимодействие различных частей python и cython кода через различные процессы.
    Использование мультипроцессинга напрямую вызывает дикие проблемы.
    """
    def __init__ (self):
        """
        обеспечивает инициализацию класса сетевых межпроцессорных взаимодействий
        :return: возвращает ссылку на себя.
        """
        
        # создание очередей для приёма и отправки информации в дочерние процессы
        self.cpu_in = Queue()
        self.cpu_out = Queue()
        
        self.video_in = Queue()
        self.video_out = Queue()
        
        Thread.__init__(self)

    def run(self):
        """
        Метод исполняется при запуске отдельного потока.
        Метод зациклен.
        """
        
        #--- определение сетевых подключений ---
        HOST = "" # localhost
        PORT = 58633
        
        # --- создание сервера для подключения
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #srv.settimeout(5)
        
        while 1:
            try:
                #--- запуск сервера ---
                srv.bind((HOST, PORT))
                
                #--- счётчик циклов и цикл
                count_loop = 0
                while True:
                    print 'Name = ', self.getName(), count_loop    # получить имя системы и счётчик циклов
                    print "Слушаю порт".decode('utf8'), PORT
                    srv.listen(1)  # сколько можно одновременно получить подключений на порт
                    sock, addr = srv.accept() # ждём когда вылезит клиент
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
            finally:
                sleep(1)
                count_loop += 1

if __name__=='__main__':
    app=ClsNPC()
    app.start()
