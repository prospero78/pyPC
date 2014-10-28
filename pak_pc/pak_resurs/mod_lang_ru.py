# -*- coding: utf8 -*-
'''
Модуль локализации русского языка.
'''

class ClsLangRU(object):
    def __init__(self):
        self.win_main_name = 'pyPC    верс. '+self.vers
        self.win_main_btn_exit_name = 'Выход'
        self.win_main_mbt_file_name = 'Файл'
        self.win_main_mbt_edit_name = 'Правка'
        self.win_main_mbt_edit_bp = 'Настройка регистра отладка'
        self.win_main_mbt_edit_disk = 'Настройка дисков'
        self.win_main_mbt_custom_name = 'Настройка'
        self.win_main_mbt_help_name = 'Справка'
        self.win_main_mbt_help_help = 'Справка по программе'
        self.win_main_mbt_help_about = 'О программе'
        self.win_main_btn_step = 'Шаг >'
        self.win_main_btn_debug_0 = 'Отладка  >>'
        self.win_main_btn_debug_1 = 'Отладка  [X]'

        self.win_main_btn_show_screen_show = 'Показать экран'
        self.win_main_btn_show_screen_hide = 'Скрыть экран'
        self.win_main_btn_reset = 'Сброс (Х)'
        self.win_main_frm_cpu_freq_lbl_key = 'Частота ЦП'

        self.win_about_name = 'О программе'
        self.win_about_close = 'Закрыть это окно'
        self.win_about_url = 'http://github.com/prospero78/pyPC'
        self.win_about_txt = '''Программа для виртуализации
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
        self.winAbout_license = 'Лицензионное требование'

        self.winLicense_title = 'Лицензионное требование'

        f = open('./pakPC/pakResurs/txt/GNU_GPL_v3_rus.txt', 'r')
        self.winLicense_locale = f.read()
        f.close()

        self.win_license_btn_local_license_text = 'Русский'

        self.win_screen_title = 'Экран pyPC'
        self.win_screen_btn_screen_close_text = 'Закрыть'

        self.win_idc_name = 'Интерфейс дискового кластера'
        self.win_idc_open = 'Открыть'
        self.win_idc_open_disk_image = 'Открыть дисковый образ...'
        self.win_idc_image_create = 'Cоздать'
        self.winIDC_ImageUnpath = 'Очистить'
        self.winIDC_cancel = 'Отменить'
        self.winIDC_reset = 'Сбросить'

        self.winCreateDisk_title = 'Создание нового диска...'

        self.winEditBP_title = 'Свойства регистра BP'
        self.winEditBP_btnClose = 'Закрыть'