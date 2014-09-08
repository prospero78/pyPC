# -*- coding: utf8 -*-
'''
Класс ресурсов. Содержит всякие полезные штуки для интернационализации, графики и т. д.
'''
class clsRes:
    def __init__(self, root=None, lang='ru', arg=[]):
        self.root=root
        self.lang=lang
        self.arg=arg

        self.create_res()
        self.pars_arg()
        if self.lang=='ru':
            self.create_ru()

    def pars_arg(self):
        if len(self.arg)>1:
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
        self.vers='0.461' # текущая версия сборки
        self.max_adr=2**16 # максимальный адрес памяти
        self.max_reg_val=2**16 # максимальное значение регистра

        # инициализация биоса
        from modBios import bios
        self.bios=bios
        
        # чтение файла лицензии
        self.winLicense_title='Лицензионное требование'
        f=open('./pakPC/pakResurs/txt/GNU_GPL_v3_eng.txt','r')
        self.winLicense_eng=f.read()
        f.close()
        
    def create_ru(self):
        self.winMain_name='pyPC    Vers. '+self.vers
        self.winMain_btnExit_name='Выход'
        self.winMain_mbtFile_name='Файл'
        self.winMain_mbtEdit_name='Правка'
        self.winMain_mbtEdit_disk='Настройка дисков'
        self.winMain_mbtCustom_name='Настройка'
        self.winMain_mbtHelp_name='Справка'
        self.winMain_mbtHelp_help='Справка по программе'
        self.winMain_mbtHelp_about='О программе'
        
        self.winAbout_name='О программе'
        self.winAbout_close='Закрыть это окно'
        self.winAbout_url='http://github.com/prospero78/pyPC'
        self.winAbout_txt='''Программа для виртуализации
несуществующего компьютера. Всё что в нём есть:
  -процессор
  -память
  -видеокарта
  -сетевая карта
  -жесткий диск
всё это наглым образом эмулируется.
Цель проекта: создать заведомо несовместимую с IBM PC 
архитектуру, заведомо безопасную и легко настраиваемую
для своих нужд. Суперькомпьютера из этого не сделать,
но и свои секреты, в целом -- доверить можно.
Сделано в России с любовью. )'''
        self.winAbout_license='Лицензионное требование'
        
        self.winLicense_title='Лицензионное требование'
        f=open('./pakPC/pakResurs/txt/GNU_GPL_v3_rus.txt','r')
        self.winLicense_locale=f.read()
        self.winLicense_btnLocalLicense_text='Русский'
        self.winLicense_btnStep_text='Шаг >>'
        self.winLicense_btnShowScreen_text='Показать экран'
        
        self.winScreen_title='Экран pyPC'
        self.winScreen_btnScreenClose_text='Закрыть'
        
        self.winIDC_name='Интерфейс дискового кластера'
        self.winIDC_open='Открыть'
        self.winIDC_OpenDiskImage='Открыть дисковый образ...'
        self.winIDC_ImageCreate='Cоздать'
        self.winIDC_ImageUnpath='Очистить'
        self.winIDC_cancel='Отменить'
        self.winIDC_reset='Сбросить'
        
        self.winCreateDisk_title='Создание нового диска...'
        
        f.close()
