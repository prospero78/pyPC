# -*- coding: utf8 -*-
'''
    Главный запускающий файл для всего pyPC.
'''

import sys

def main():
    '''
    Импортирует главный класс, и запускает приложение.
    '''
    arg=sys.argv
    from pakPC import clsPC
    app=clsPC(arg=arg)
    app.run()

if __name__=='__main__':
    #TODO: сделать возможность передачи аргументов
    sys.argv.append('--help')
    sys.argv.append('--about')
    main()
