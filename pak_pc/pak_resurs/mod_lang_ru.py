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
        self.__vers = self._ClsLang__vers + 1
        self.win_main_name = 'pyPC    верс. ' + self.__vers
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
        self.win_about_license = 'Лицензионное требование'

        self.win_license_title = 'Лицензионное требование'

        fread = open('./pakPC/pakResurs/txt/GNU_GPL_v3_rus.txt', 'r')
        self.win_license_locale = fread.read()
        fread.close()

        self.win_license_btn_local_text = 'Русский'

        self.win_screen_title = 'Экран pyPC'
        self.win_screen_btn_close_text = 'Закрыть'

        self.win_idc_name = 'Интерфейс дискового кластера'
        self.win_idc_open = 'Открыть'
        self.win_idc_open_disk_image = 'Открыть дисковый образ...'
        self.win_idc_image_create = 'Cоздать'
        self.win_idc_image_unpath = 'Очистить'
        self.win_idc_cancel = 'Отменить'
        self.win_idc_reset = 'Сбросить'

        self.win_create_disk_title = 'Создание нового диска...'

        self.win_edit_bp_title = 'Свойства регистра BP'
        self.win_edit_bp_btn_close = 'Закрыть'

    @property
    def vers(self):
        '''
        Возвращает свойство версии для текущего класса, с учётом
        версии родительских классов.
        '''
        return self.__vers

    @vers.setter
    def vers(self, val=None):
        ''''
        Устанавливает текущую версию класса.
        Если значение неприемлимое -- ничего не делает.
        '''
        if val == None or val == '':
            print 'ClsLangRu.vers_setter(): invalid val version!'
        else:
            self.__vers = val
