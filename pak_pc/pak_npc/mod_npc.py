# -*- coding: utf8 -*-
"""
Модуль предоставляющий класс для работы хост-процесса с
множеством процессов по сети. Это будет
универсальное и переносимое решение.
"""

import socket
from threading import Thread
from time import sleep
from mod_connect import ClsNetStor


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
        
        Thread.__init__(self)

    def run(self):
        """
        Метод исполняется при запуске отдельного потока.
        Метод зациклен.
        """
        
        def get_video_connect():
            """
            Устанавливает соединение видеокарты.
            """
            #--- определение сетевых подключений ---
            HOST = "" # localhost
            PORT = 58633 # порт, на который должно прийти подключение от видеокарты.
            
            # --- создание сервера для подключения
            srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #srv.settimeout(5)
            
            #--- запуск сервера ---
            srv.bind((HOST, PORT))
            srv.listen(1)  # сколько можно одновременно получить подключений на порт
            self.video_socket, self.video_addr = srv.accept() # ждём когда подкючится клиент видеокарты
            
                
        
        def get_cpu_connect():
            """
            Устанавливает соединение с ЦП.
            """
            pass
        
        def send_info():
            """
            Отправляет сообщения из очередей сообщений.
            """
            pass
            
        def get_info():
            """
            Получает сообщения по сети и ставит в очередь обработки.
            """
        
        
        # -- признак подключения видеокарты ---
        self.video_connect = False
        
        # -- признак подключения ЦП ---
        self.cpu_connect = False
        
        # --- данные по подключению видеокарты ---
        self.net_video = ClsNetStor()
        
        # --- данные по подключению ЦП ---
        self.net_cpu = ClsNetStor()
        
        #--- счётчик циклов и цикл
        count_loop = 0
        
            print 'Name = ', self.getName(), count_loop    # получить имя системы и счётчик циклов
            print "Слушаю порт".decode('utf8'), PORT
            
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

if __name__=='__main__':
    app=ClsNPC()
    app.start()
