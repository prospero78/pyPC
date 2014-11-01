# -*- coding: utf8 -*-
"""
Подборка всех файлов проекта.
1. Статистика по строкам
2. Статистика по файлам
"""

from os import getcwd, listdir
from Tkinter import Tk, Button, Frame, PanedWindow, Menu, Menubutton, Text

vers = 'Version 1.70'

#
# thanks={koder{mail:mail, num_edit:num_edit, site:site}, koder:{...}}
#
thanks = {'V.L.': {'mailto': 'arnys@mail.ru',
                   'num_edit': '2+',
                   'site': 'www.aloys.narod.ru'}}

m = 'Special thanks: <a href="mailto:arnys@mail.ru">V.L. (2+)</a><br>'
# g - geometry
g = {
    'winMain_minSizeX': 600,
    'winMain_minSizeY': 400,
    'winMain_maxSizeX': 800,
    'winMain_maxSizeY': 600
}
ru = {
    'win_main': 'Small Reporter for -=[fantom lab]=- ' + vers,
    'mnu_file': 'Файл',
    'mnuFile_New': 'Новый',
    'mnuFile_Open': 'Новый',
    'mnuFile_Save': 'Сохранить',
    'mnuFile_SaveAs': 'Сохранить как...',
    'mnuFile_Print': 'Печать',
    'mnuFile_Exit': 'Выход',
    'mnu_edit': 'Правка',
    'mnuEdit_Undo': 'Отмена',
    'mnuEdit_Redo': 'Повтор',
    'mnuEdit_Copy': 'Копировать',
    'mnuEdit_Cut': 'Вырезать',
    'mnuEdit_Paste': 'Вставить',
    'mnuEdit_Find': 'Поиск',
    'mnuEdit_Replace': 'Замена',

    'btn_save': 'Сохранить <Ctrl-S>',
    'btn_generate': 'Создать отчёт! <Ctrl-G>',
    'btn_exit': 'Выход <Ctrl-Q>',
}


class ClsGUI(Tk):
    """
    Попытка создать ГУИ для репортера.
    """

    def __init__(self):
        """
        Создаёт интерфейс пользователя для репортера.
        """
        self.frm_up = Frame(self)

        def bind_win():
            def quit_reporter(event=''):
                import sys

                sys.exit()

            def save_reporter(event=''):
                """
                Сохраняет отчёт.
                :param event:
                """
                print '===report==='
                a = ClsSmallReporter
                self.txt_report.insert('1.0', a.html_data)

            def generate_report(event=''):
                print '===report==='
                a = ClsSmallReporter
                self.txt_report.insert('1.0', a.html_data)

            self.bind('<Control-Q>', quit_reporter)
            self.bind('<Control-q>', quit_reporter)

            self.bind('<Control-S>', save_reporter)
            self.bind('<Control-s>', save_reporter)

            self.bind('<Control-G>', generate_report)
            self.bind('<Control-g>', generate_report)

        Tk.__init__(self)
        self.title(ru['win_main'])
        self.minsize(g['winMain_minSizeX'], g['winMain_minSizeY'])
        self.maxsize(g['winMain_maxSizeX'], g['winMain_maxSizeY'])
        self.create_up_frame()
        self.create_frm_middle()
        self.create_frm_down()
        bind_win()
        self.mainloop()

    def create_up_frame(self):
        """
        Создаёт верхний фрейм.
        :type self: object
        """
        self.create_menu_bar()
        self.frm_up.pack(side='top', fill='x')

    def create_frm_middle(self):
        self.frm_midle = Frame(self, border=2, relief='raised')
        self.frm_midle.pack(side='top', expand=1, fill='both')
        self.txt_report = Text(self.frm_midle, font='Consolas 9 normal')
        self.txt_report.pack(side='top', fill='both', expand=1)


    def create_frm_down(self):
        def btn_generate_click(event=''):
            print '===report==='
            a = ClsSmallReporter
            self.txt_report.insert('1.0', a.html_data)

        def create_btn_exit():
            def report_exit(event=''):
                import sys

                sys.exit()

            self.btn_exit = Button(self.frm_down,
                                   text=ru['btn_exit'],
                                   command=report_exit,
                                   bg='red')
            self.btn_exit.pack(side='left', expand=1, fill='x')

        def create_btn_save():
            self.btn_save = Button(self.frm_down, text=ru['btn_save'])
            self.btn_save.pack(side='left', expand=1, fill='x')

        def create_btn_generate():
            self.btn_generate = Button(self.frm_down,
                                       text=ru['btn_generate'],
                                       command=btn_generate_click)
            self.btn_generate.pack(side='left', expand=1, fill='x')


        self.frm_down = Frame(self)

        create_btn_generate()
        create_btn_save()
        create_btn_exit()

        self.frm_down.pack(side='bottom', fill='x')

    def create_menu_bar(self):
        def create_mnu_file():
            self.btn_file = Menubutton(self.pnl_menu, text=ru['mnu_file'],
                                       border=3, relief='groove')
            self.mnu_file = Menu(self.btn_file)
            self.btn_file.config(menu=self.mnu_file)
            self.mnu_file.add_command(label=ru['mnuFile_New'],
                                      accelerator='Ctrl+N')
            self.mnu_file.add_command(label=ru['mnuFile_Open'],
                                      accelerator='Ctrl+O')
            self.mnu_file.add_separator()
            self.mnu_file.add_command(label=ru['mnuFile_Save'],
                                      accelerator='Ctrl+S')
            self.mnu_file.add_command(label=ru['mnuFile_SaveAs'])
            self.mnu_file.add_separator()
            self.mnu_file.add_command(label=ru['mnuFile_Print'],
                                      accelerator='Ctrl+P')
            self.mnu_file.add_separator()
            self.mnu_file.add_command(label=ru['mnuFile_Exit'],
                                      accelerator='Ctrl+Q')
            self.btn_file.pack(side='left')

        def create_mnu_edit():
            self.btn_edit = Menubutton(self.pnl_menu,
                                       text=ru['mnu_edit'],
                                       border=3,
                                       relief='groove')
            self.mnu_edit = Menu(self.btn_edit)
            self.btn_edit.config(menu=self.mnu_edit)
            self.mnu_edit.add_command(label=ru['mnuEdit_Undo'],
                                      accelerator='Ctrl+Z')
            self.mnu_edit.add_command(label=ru['mnuEdit_Redo'])
            self.mnu_edit.add_separator()
            self.mnu_edit.add_command(label=ru['mnuEdit_Copy'],
                                      accelerator='Ctrl+C')
            self.mnu_edit.add_command(label=ru['mnuEdit_Cut'],
                                      accelerator='Ctrl+X')
            self.mnu_edit.add_command(label=ru['mnuEdit_Paste'],
                                      accelerator='Ctrl+V')
            self.mnu_edit.add_separator()
            self.mnu_edit.add_command(label=ru['mnuEdit_Find'],
                                      accelerator='Ctrl+F')
            self.mnu_edit.add_command(label=ru['mnuEdit_Replace'],
                                      accelerator='Ctrl+R')
            self.btn_edit.pack(side='left')

        def create_mnu_custom():
            self.btn_custom = Menubutton(self.pnl_menu, text='mnu_custom',
                                         border=3, relief='groove')
            self.mnu_custom = Menu(self.btn_custom)
            self.btn_custom.config(menu=self.mnu_custom)
            self.mnu_custom.add_command(label='Type files',
                                        accelerator='Ctrl+D')
            self.mnu_custom.add_command(label='--1')
            self.mnu_custom.add_separator()
            self.mnu_custom.add_command(label='--2', accelerator='---')
            self.mnu_custom.add_command(label='--3', accelerator='---')
            self.mnu_custom.add_command(label='--4', accelerator='---')
            self.mnu_custom.add_separator()
            self.btn_custom.pack(side='left')

        def create_mnu_help():
            self.btn_help = Menubutton(self.pnl_menu,
                                       text='mnu_help',
                                       border=3,
                                       relief='groove')
            self.mnu_help = Menu(self.btn_help)
            self.btn_help.config(menu=self.mnu_help)
            self.mnu_help.add_command(label='Type files', accelerator='Ctrl+D')
            self.mnu_help.add_command(label='--1')
            self.mnu_custom.add_separator()
            self.btn_help.pack(side='left')

        self.pnl_menu = PanedWindow(self.frm_up, border=2, relief='raised')
        create_mnu_file()
        create_mnu_edit()
        create_mnu_custom()
        create_mnu_help()

        self.pnl_menu.pack(side='left', expand=1, fill='x')


class ClsSmallReporter:
    def get_dir(self, dir=''):
        """
        Получение списка каталогов и файлов.
        """
        a = listdir(dir)
        i = 0
        # необходимо добавить полный путь к списку файлов
        while len(a) > i:
            b = a[i]
            b = dir + '\\' + b
            a[i] = b
            i = i + 1
        return a

    def get_all_files_in_patch(self, ListElement, current_patch):
        def chek_dir(fileProcess='1.py'):
            '''
            Проверка на то, является ли элемент списка каталогом или файлом.
            '''
            try:  # ветка истинности файла
                fP = open(fileProcess, 'rb')
                fP.close()
            # если произошло исключение, то элемент - каталог, или занятый файл
            except:
                return 'not file'

        # пока число элементов не сравняется со счётчиком
        i = 0
        while len(ListElement) > i:
            # получить текущий элемент
            current_element = ListElement[i]
            # исключение самого файла репортера
            if current_element == (current_patch + '\\' + '__Report.py'):
                # если список не истощён - уменьшить его на один элемент
                if len(ListElement) != i - 1:
                    ListElement = ListElement[:i] + ListElement[i + 1:]
                    # уменьшить список файлов-каталогов на один
                    current_element = ListElement[i - 1]
            # проверить на каталог и занятость
            result = chek_dir(fileProcess=current_element)
            if result == 'not file':  # если не файл
                # то значит каталог, получить список файлов
                new_dir = self.get_dir(dir=current_element)
                # вставить в основной список
                ListElement = ListElement[:i] + new_dir + ListElement[i + 1:]
                # продлить итерацию на один проход
                i = i - 1
            # продвинуться к следующему элементу списка
            i = i + 1
        # все ветки перебраны - вернуть полный список файлов
        full_list_file = ListElement
        return full_list_file, i

    def TypeProect(self, Lines):
        '''
        Процедура по количеству строк кода определяет его крутость.
        Балл вычисляется по логарифмической шкале с десятичным основанием.
        '''
        from cmath import log10

        Lines = str(abs(log10(Lines)))
        Lines = Lines[:4]
        print 'Current ball: ', Lines
        if Lines[0] <= '1':
            return 'Nano project (level ' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'
        elif Lines[0] >= '1' and Lines[0] <= '2':
            return 'Micro project (level ' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'
        elif Lines[0] >= '2' and Lines[0] <= '3':
            return 'Mini project (level ' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'
        elif Lines[0] >= '3' and Lines[0] <= '4':
            return 'Solid project (level ' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'
        elif Lines[0] >= '4' and Lines[0] <= '5':
            return 'Big project (level ' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'
        elif Lines[0] >= '5' and Lines[0] <= '6':
            return 'Whery big project (level ' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'
        elif Lines[0] >= '6' and Lines[0] <= '7':
            return 'Multi project (level ' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'
        elif Lines[0] >= '7':
            return 'Global project (level' + Lines[
                0] + ')<br>Total ball: ' + Lines + '\n'

    @property
    def __init__(self):
        """
        Создаёт класс репортера.
        :rtype : object
        """
        self.name_report = None
        self.html_data = None
        self.i = None
        self.list_file_py = None
        self.html_data = ""

        def save_report():
            """
            Сохраняет отчёт.
            """
            a = open(self.name_report + '.html', 'wb')
            a.write(self.html_data)
            a.close()

        def get_files_py():
            """
            Возвращает список python-файлов.
            :return:
            """

            def filter_file_py(l=''):
                '''
                Проверка на то, является ли файл файлом с расширением .py
                '''
                i = 0
                while len(l) > i:
                    f = l[i]
                    if f[-3:] != '.py':
                        l = l[:i] + l[i + 1:]
                        i = i - 1
                    i = i + 1
                return l

            # получить текущий путь
            current_patch = getcwd()
            # получить список элементов каталогов/файлов
            ListElement = self.get_dir(current_patch)
            # инициализация счётчика строк
            NumLines = 0
            # вернуть полный список файлов
            full_list_file, self.i = self.get_all_files_in_patch(ListElement,
                                                                 current_patch)
            # отбросить все файлы не являющиеся .py
            self.list_file_py = filter_file_py(full_list_file)

        def create_report():
            """
            СЗапускает создание отчёта.
            :return:
            """

            def get_table(list_file_py):
                """
                Возвращает таблицу файлов.
                :param list_file_py:
                :return:
                """

                def get_analis_file(f):
                    def doc_string(file=''):
                        '''
                        Процедура вычисляет количество строк документации.
                        '''
                        a = ''  # переменная строка
                        i = 0  # счётчик порядкового номера строки
                        s = 0  # количество строк документации
                        while i < len(
                                file) - 3:  # искать символ начала комментария
                            a = file[i:i + 3]

                            if (a == '"""' or a == "'''"):
                                s += 1
                            i += 1
                        return s

                    '''
                    Процедура анализирует .py файл на количество строк и
                    длинну кода.
                    '''
                    fa = open(f, 'rb')  # прочитать файл в переменную
                    t = fa.read()
                    fa.close()

                    number_line = 1
                    ch = 0
                    len_file = len(t)  # получить длину файла
                    # проверка на количество символов ввода
                    while len_file > ch:
                        sym = t[ch]
                        # если перевод строки увеличить счётчик строк
                        if sym == '\n':
                            number_line = number_line + 1
                        ch += 1
                    kol_doc_str = doc_string(file=t)
                    return len_file, number_line, kol_doc_str

                # построение тела HTML таблицы
                down = 'Plis, up<br>densyti code.' + '\n'
                up = 'Plis, down<br>densyti code.' + '\n'
                body_html = ''
                i = 0
                total_lines = 0
                total_bytes = 0
                total_doc = 0  # количество строк кода
                # пока не обнулится счётчик файлов
                col = '<td bgcolor="#00FFFF" align="left">\n'
                while len(list_file_py) > i:
                    file = list_file_py[i]
                    len_file, number_line, FileDoc = get_analis_file(file)
                    total_doc = total_doc + FileDoc
                    body_html = body_html + '<tr>'
                    body_html = body_html + col + '<h5>' + str(i + 1) + \
                           '. ' + '</td>' + col + '<h5>' + str(file) + \
                           '</td>\n'
                    body_html = body_html + col + '<h5>' + str(number_line) + \
                           '</td>' + col + '<h5>' + \
                           str(len_file) + '</td>\n'
                    densyti = Ratio(len_file, number_line)
                    if densyti == 'Low':
                        Note = down
                    elif densyti == 'up':
                        Note = up
                    else:
                        Note = '-'
                    body_html = body_html + '<td><h5>' + densyti + \
                                '</td><td><h5>' + Note + '</td></tr>' + '\n'
                    total_lines = total_lines + number_line
                    total_bytes = total_bytes + len_file
                    i = i + 1
                return body_html, total_lines, total_bytes, total_doc

            def Ratio(len_file, number_line):
                '''
                Процедура проверяет плотность кода.
                '''
                a = len_file / number_line
                if a <= 14:
                    return 'Low'
                elif a >= 15 and a <= 59:
                    return 'Normal'
                elif a >= 60:
                    return 'Hi'
                return

            def GetTime():
                '''
                    Надо получить форматированное время в виде
                    'гг-мм-дд_чч-мм-сс'.
                '''

                def NullTime(data):
                    '''
                    Проверка на наличие двух цифр во времени.
                    Если нет, то добавление нуля слева.
                    '''
                    if len(data) < 2:
                        data = '0' + data
                    return data

                from time import localtime
                # получение даты и времени
                t = localtime()
                # получить год
                god = str(t[0])
                god = NullTime(god)
                # получить месяц
                mon = str(t[1])
                mon = NullTime(mon)
                # получить день
                day = str(t[2])
                day = NullTime(day)
                # получить часы
                hour = str(t[3])
                # форматировать часы
                hour = NullTime(hour)
                # получить минуты
                minute = str(t[4])
                # форматировать минуты
                minute = NullTime(minute)
                # получить секунды
                second = str(t[5])
                # форматировать секунды
                second = NullTime(second)

                # составить общую строку времени
                result = god + '-' + mon + '-' + day + '_' + hour + '-' + \
                         minute + '-' + second
                return result


            def get_head_html():
                def get_thanks():
                    '''
                    Процедурка формирует HTML-код с благодарностями и мылами.
                    '''
                    global thanks
                    # получить список кодеров
                    list_coder = thanks.keys()
                    # проход по списку кодеров
                    out = '-------------------------<br>Special thanks: <BR>\n'
                    for i in xrange(len(list_coder)):
                        # получить имя кодера
                        name_coder = list_coder[i]
                        # получить информацию по кодеру
                        info_coder = thanks[name_coder]
                        # получить мыло кодера
                        mail = info_coder['mailto']
                        # получить количество советов кодера
                        num_edit = info_coder['num_edit']
                        # получить сайт кодера
                        site = info_coder['site']
                        # сформировать строку
                        out += 'Koder: <a href="mailto:' + mail + '">' + \
                               name_coder + ' (' + num_edit + ')' + '\n'
                        out += '</a>'
                        out += ' Site: <a href=http://' + site + '>' + site + \
                               '</a><br>\n'
                    out += '-------------------------<br>'
                    return out

                global vers, thanks
                txt = 'Small report for -=[fantom lab]=-<br>Desing in 2007\n\n'
                # correct charset for cyrillic path-names
                # модифицировано V.L. <arnys@mail.ru> (2+)
                html_data = '<head><META HTTP-EQUIV="Content-Type" CONTENT=' + \
                            '"text/html;' + '\n'
                html_data = html_data + 'charset=windows-1251"></head>' + '\n'
                body_html = '<html>' + html_data + '<title>Small ' + \
                            'reporter for Python</title>' + \
                            '<body bgcolor="#CCFFCC">' + '\n'
                body_html += '<b><center><h2>' + txt + \
                             '</center><hr></b>' + '\n'
                body_html += '<br><code><h5>REPORTER ' + vers + '<br>' + '\n'
                body_html += '<a href=http://www.fantom-lab.narod.ru>' + \
                             'www.fantom-lab.narod.ru</a><br>\n'
                body_html += 'Author: <a href="mailto:fantom-ab@mai' + \
                             'l.ru">-=[fantom]=-</a><br>\n'
                body_html += get_thanks()
                body_html += '<b>Summary info:<br>' + '\n'
                body_html += '<table border=3 width=100% bgcol' + \
                             'or="#00FFFF">' + '\n'
                col = '<td bgcolor="#C0C0C0" align="center">' + '\n'
                body_html += '<tr>' + col + '<b>Number<br>file</b>' + \
                             '</td>' + col + '<b>\n'
                body_html += 'Name File</b></td>' + col + \
                             '<b>Number<br>lines' + \
                             '</b></td>' + '\n'
                body_html += col + '<b>All<br>bytes</b></td>' + col + \
                            '<b><h5>densyti<br>code</b>\n'
                body_html += '</td>' + col + '<b>Note</b></td></tr>\n'
                body_html = html_data + body_html
                return body_html

            def get_end_html(total_py_files,
                             name_report,
                             total_lines,
                             total_bytes,
                             total_doc):
                """
                Получает концовку html текста отчёта
                :rtype : object
                :param total_py_files: всего python файлов
                :param name_report: имя отчёта
                :param total_lines: всего строк
                :param total_bytes: всего байт
                :param total_doc: всего строк документации
                :return: строку отчёта в формате html
                """

                def get_spez_info():
                    '''
                    Процедура выводит информацию о проекте и суммирует
                    номер сборки
                    '''
                    try:
                        from _info import ClsInfo

                        col = '<td bgcolor="#C0C0C0" align="center">' + '\n'
                        string = '<br><table border=3 width=60% bgcolor' + \
                            '="#00FFFF">' + '\n'
                        string += '<tr>' + col + '<h5>Parametrs</td>' + col + \
                                  '<h5>Variable</td></tr>' + '\n'
                        _inf = clsInfo()
                        string += '<tr><td><h5>Author</td><td><h5>' + \
                                  _inf.author() + '</td></tr>' + '\n'
                        string += '<tr><td><h5>Project</td><td><h5>' + \
                                  _inf.project() + '</td></tr>' + '\n'
                        string += '<tr><td><h5>About</td><td><h5>' + \
                                  _inf.about() + '</td></tr>' + '\n'
                        string += '<tr><td><h5>Version</td><td><h5>' + \
                                  _inf.version() + '</td></tr>' + '\n'
                        string += '<tr><td><h5>Build</td><td><h5>' + \
                                  _inf.build() + '</td></tr></table>' + '\n'
                        return string
                    except:
                        return '''
</code><hr>
</b>
<h3>Plis, add Your project file <font color="#0808FF"><b>'_info.py'</font><br>
All variables defined programmers self.<br>
This file must content string:<br><code><h5>
<p style="margin-top: 0; margin-bottom: 0"><font color="#800080"><i><b># -*-
coding: cp1251 -*-</b></i></font></p>
<p style="margin-top: 0; margin-bottom: 0"><b>class</b> <font color="#0000FF">
clsInfo</font>:</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;&nbsp; <b>def</b> __init__(<b>
<font color="#000080">self</font></b>):<br>
&nbsp;&nbsp;&nbsp; self.authorInfo=''<br>
&nbsp;&nbsp;&nbsp; self.projectInfo=''<br>
&nbsp;&nbsp;&nbsp; self.aboutInfo=''<br>
&nbsp;&nbsp;&nbsp; self.buildInfo=''</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp; <b>def</b> author
(<b><font color="#000080">self</font></b>):</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;&nbsp;&nbsp;
<font color="#FF0000"><b>return</b></font> self.authorInfo</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp; <b>def</b> project
(<font color="#000080"><b>self</b></font>):</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;&nbsp;&nbsp;
<font color="#FF0000"><b>return</b></font> self.projectInfo</p>
<p style="margin-top: 0; margin-bottom: 0"><span lang="ru">&nbsp; </span>
<b>def</b>
about(self):</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;&nbsp;&nbsp;
<font color="#FF0000">return</font> self.aboutInfo</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp; <b>def</b> version
(<b><font color="#000080">self</font></b>):</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;&nbsp;&nbsp; <b>
<font color="#FF0000">return</font></b> self.projectInfo</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp; <b>def</b> build(self):</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;&nbsp;&nbsp; <b>
<font color="#FF0000">return</font></b> self.buildInfo</p>

<hr>
'''

                def get_densyti_doc_string(KolString, KolLine):
                    '''
                    Процедура вычисляет плотность строк документации
                    KolString - количество строк документации
                    KolLine   - количество строк кода
                    '''
                    KolLine += 0.0
                    densyti = KolLine / KolString
                    a = str(densyti)
                    a = a[0:5]
                    if a < str(1.0 / 10):
                        _msg = '<font color="#808000">Plis, up densyti ' + \
                            'doc_string!</font>'
                    elif a > str(1.0 / 10) and a < str(1.0 / 5):
                        _msg = 'Normal densyti doc_string.'
                    else:
                        _msg = '<font color="#808000">Plis, down densyti ' + \
                            'doc_string!</font>'
                    return _msg

                # получить конец таблицы
                body_html = ''
                body_html += '</tr></table><br>' + '\n'
                body_html += '<b>Date: ' + name_report + '</b><br>' + '\n'
                body_html += get_spez_info()
                body_html += '<br><table border=3 width=100% ' + \
                             'bgcolor="#00FFFF">' + \
                        '<tr><td>' + '\n'
                body_html += '<b><h5>Total lines=' + str(
                    total_lines) + '</td><td>' + '\n'
                body_html += '<b><h5>Total bytes=' + str(
                    total_bytes) + '</td><td>' + '\n'
                body_html += '<b><h5>Total Files=' + str(
                    total_py_files) + '</td><td><b><h5>' + '\n'
                body_html += 'densyti code=' + Ratio(total_bytes, total_lines)
                body_html += '</td></tr><tr><td><h5>Total ' + \
                             'String docs:</td><td>\n'
                body_html += '<h5>' + str(total_doc) + '</td>' + '\n'
                body_html += '<td><h5>densyti docs</td><td><h5>' + \
                        str(get_densyti_doc_string(total_lines,  total_doc)) + \
                        '</tr></table><br><br>\n'
                body_html += 'Size Project: ' + self.TypeProect(
                    total_lines) + '</body></html>\n'
                return body_html

            # модифицировано V.L. <arnys@mail.ru>(1+)
            if not self.list_file_py:
                print 'Can not create report - files *.py not found!'
                return
            print 'Number All file=', self.i, ',\t*.py files=', len(
                self.list_file_py)
            self.name_report = GetTime()
            print 'Report file: ' + self.name_report + '.html'
            self.html_data = get_head_html()
            body_html, total_lines, total_bytes, total_doc = get_table(
                self.list_file_py)
            self.html_data += body_html
            total_py_files = len(self.list_file_py)
            body_html = get_end_html(total_py_files,
                                self.name_report,
                                total_lines,
                                total_bytes,
                                total_doc)
            self.html_data += body_html

        get_files_py()
        create_report()
        save_report()


if __name__ == '__main__':
    print '**********************************************'
    print 'Begin report....'
    # вызов репортера на исполнение
    # report=СlsSmallReporter()
    # raw_input('Press <Enter> key...\n' )
    rep = ClsGUI()
    print'**********************************************'
