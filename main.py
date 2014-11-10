# -*- coding: utf8 -*-
"""
    Главный запускающий файл для всего pyPC.
"""

import sys
from time import sleep

__version__ = 5


def main():
    """
    Импортирует главные классы, и запускает приложение.
    1. ClsPC
    3. ClsCPU
    2. ClsVideo
    """
    arg = sys.argv
    from pak_pc import ClsPC

    app = ClsPC(arg=arg)
    os.system('start main_video.py')
    sleep(0.3)
    os.system('start main_cpu.py')
    sleep(0.3)
    app.run()


if __name__ == '__main__':
    __doc_app__ = \
    """
        #TODO: доделать возможность передачи аргументов
        Кое что уже сделано, но надо бы добавить ещё ключей для
        солидняка )))
        #TODO: в меню "Файл" давно пора доделать возможность выхода
        из машины.
    """
    sys.argv.append('--help')
    sys.argv.append('--about')
    main()
