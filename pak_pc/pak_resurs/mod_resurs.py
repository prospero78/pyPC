# -*- coding: utf8 -*-
'''
Класс ресурсов. Содержит всякие полезные штуки для интернационализации,
графики и т. д.
'''
from pak_pc.pak_resurs.mod_lang import ClsLang
class ClsRes(ClsLang):
    '''
    Класс создаёт все необходимые ресурсы в программе.
    '''
    def __init__(self, root=None, lang='ru', arg=None):
        self.root = root
        self.lang = lang
        self.arg = arg

        self.create_res()
        self.pars_arg()
        if self.lang == 'ru':
            from pak_pc.pak_resurs.mod_lang_ru import ClsLangRu
            ClsLangRu.__init__(self, lang=self.lang)

    def pars_arg(self):
        if len(self.arg) > 1:
            for i in self.arg:
                if ('--help' in i) or ('-h' in i) or ('/h' in i):
                    print '''
Пример запуска: "python main.py --help"
Помощь по ключам командной строки:
    --help (-h)      показать эту справку
    --about (-a)     о программе
                    '''.decode('utf8')
                elif ('--about' in i) or ('-a' in i):
                    print '''pyPC vers. ''' + self.vers + '''
О программе:
    Эта программа представляет собой вымышленный
    (но вполне рабочий) виртуальный компьютер.
    Конечная цель:
        -создать (на сколько это возможно) платформонезависимый компьютер
        -с понятной и простой системой команд, архитектурой
        -дать людям бесплатный инструмент для безопасной работы в этих
            ваших тырнетах
        -наконец-то покончить с дикими вирусами (хотя, хотя.... хотелось бы)
    ------------------
    (A) Valeriy Shipkov, 2014
    (L) GNU GPL v.3
                    '''.decode('utf8')

    def create_res(self):
        '''
        vers -- версия сборки проекта, xxx -- версия сборки
        0.xxx -- черновая версия
        1.ххх -- зарелизенная версия
        И других вариантов не будет.
        '''
        self.vers = '0.870' # текущая версия сборки
        self.max_adr = 2**16 # максимальный адрес памяти
        self.max_reg_val = 2**16 # максимальное значение регистра
