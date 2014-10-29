# -*- coding: utf8 -*-
'''
Модуль локализации русского языка.
'''
from pak_pc.pak_resurs.mod_lang import ClsLang

class ClsLangRu(ClsLang):
    '''
    Класс обеспечивает строковыми ресурсами для русского языка.
    '''
    def __init__(self, lang='ru'):
        ClsLang.__init__(self, lang='ru')
        self.vers = self.vers + 3
        fread = open('./pak_pc/pak_resurs/txt/GNU_GPL_v3_rus.txt', 'r')
        lic_ru = fread.read()
        fread.close()

        self.lang_dict = {'win_main_name': 'pyPC    верс. ' + str(self.vers),
                          'win_main_btn_exit_name': 'Выход',
                          'win_main_mbt_file_name': 'Файл',
                          'win_main_mbt_edit_name': 'Правка',
                          'win_main_mbt_edit_bp': 'Настройка регистра отладка',
                          'win_main_mbt_edit_disk': 'Настройка дисков',
                          'win_main_mbt_custom_name': 'Настройка',
                          'win_main_mbt_help_name': 'Справка',
                          'win_main_mbt_help_help': 'Справка по программе',
                          'win_main_mbt_help_about': 'О программе',
                          'win_main_btn_step': 'Шаг >',
                          'win_main_btn_debug_0': 'Отладка  >>',
                          'win_main_btn_debug_1': 'Отладка  [X]',

                          'win_main_btn_show_screen_show': 'Показать экран',
                          'win_main_btn_show_screen_hide': 'Скрыть экран',
                          'win_main_btn_reset': 'Сброс (Х)',
                          'win_main_frm_cpu_freq_lbl_key': 'Частота ЦП',

                          'win_about_name': 'О программе',
                          'win_about_close': 'Закрыть это окно',
                          'win_about_url': 'http://github.com/prospero78/pyPC',
                          'win_about_txt': '''Программа для виртуализации
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
Сделано в России с любовью. )''',
                          'win_about_license': 'Лицензионное требование',

                          'win_license_title': 'Лицензионное требование',

                          'win_license_locale': lic_ru,

                          'win_license_btn_local_text': 'Русский',

                          'win_screen_title': 'Экран pyPC',
                          'win_screen_btn_close_text': 'Закрыть',

                          'win_idc_name': 'Интерфейс дискового кластера',
                          'win_idc_open': 'Открыть',
                          'win_idc_open_disk_image': \
                          'Открыть дисковый образ...',
                          'win_idc_image_create': 'Cоздать',
                          'win_idc_image_unpath': 'Очистить',
                          'win_idc_cancel': 'Отменить',
                          'win_idc_reset': 'Сбросить',

                          'win_create_disk_title': \
                          'Создание нового диска...',

                          'win_edit_bp_title': 'Свойства регистра BP',
                          'win_edit_bp_btn_close': 'Закрыть',}
