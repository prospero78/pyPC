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
    '''
    #TODO: доделать возможность передачи аргументов
    Кое что уже сделано, но надо бы добавить ещё ключей для солидняка )))
    '''
    sys.argv.append('--help')
    sys.argv.append('--about')
    main()
