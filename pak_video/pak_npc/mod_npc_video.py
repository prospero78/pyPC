# -*- coding: utf8 -*-
"""
Модуль предоставляющий класс для работы видеокарты с
хост-процессом. Позволяет передавать данные в направлении терминала.
"""

from threading import Thread

class ClsVideoIpc(Thread):
    """
    Класс для сетевого обмена видеокарты
    """
    def __init__(self):
        Thread.__init__(self)
        self.start()
        
    def run(self):
        print 'ClsVideoIpc.run()'
    
    
if __name__=='__main__':
    app=ClsVideoIpc()
