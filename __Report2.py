# -*- coding: utf8 -*-
'''
Подборка всех файлов проекта.
1. Статистика по строкам
2. Статистика по файлам
'''

from os import getcwd, listdir, walk
from Tkinter import Tk, Button, Frame, PanedWindow, Menu, Menubutton, Text
vers='Version 1.70'

#
# thanks={koder{mail:mail, NumEdit:NumEdit, site:site}, koder:{...}}
#
thanks={'V.L.':{'mailto':'arnys@mail.ru',
                'NumEdit':'2+',
                'site':'www.aloys.narod.ru'}}

m='Special thanks: <a href="mailto:arnys@mail.ru">V.L. (2+)</a><br>'
# g - geometry
g={
    'winMain_minSizeX': 600,
    'winMain_minSizeY': 400,
    'winMain_maxSizeX': 800,
    'winMain_maxSizeY': 600
    }
ru={
    'winMain':  'Small Reporter for -=[fantom lab]=- '+vers,
    'mnuFile': 'Файл',
    'mnuFile_New':  'Новый',
    'mnuFile_Open': 'Новый',
    'mnuFile_Save': 'Сохранить',
    'mnuFile_SaveAs':   'Сохранить как...',
    'mnuFile_Print':    'Печать',
    'mnuFile_Exit':    'Выход',
    'mnuEdit':  'Правка',
    'mnuEdit_Undo':  'Отмена',
    'mnuEdit_Redo':  'Повтор',
    'mnuEdit_Copy':  'Копировать',
    'mnuEdit_Cut':  'Вырезать',
    'mnuEdit_Paste':    'Вставить',
    'mnuEdit_Find':    'Поиск',
    'mnuEdit_Replace': 'Замена',

    'btnSave':  'Сохранить <Ctrl-S>',
    'btnGenerate': 'Создать отчёт! <Ctrl-G>',
    'btnExit':  'Выход <Ctrl-Q>',
    }

class ClsGUI(Tk):
    '''
    Попытка создать ГУИ для репортера.
    '''
    def __init__(self):
        def bind_win():
            def quit_reporter(event=''):
                import sys
                sys.exit()

            def save_reporter(event=''):
                print '===report==='
                a=clsSmallReporter()
                self.txtReport.insert('1.0', a.HD)

            def generate_report(event=''):
                print '===report==='
                a=clsSmallReporter()
                self.txtReport.insert('1.0', a.HD)

            self.bind('<control-Q>', quit_reporter)
            self.bind('<control-q>', quit_reporter)

            self.bind('<control-S>', save_reporter)
            self.bind('<control-s>', save_reporter)

            self.bind('<control-G>', generate_report)
            self.bind('<control-g>', generate_report)

        Tk.__init__(self)
        self.title(ru['winMain'])
        self.minsize(g['winMain_minSizeX'], g['winMain_minSizeY'])
        self.maxsize(g['winMain_maxSizeX'], g['winMain_maxSizeY'])
        self.CreateUpFrame()
        self.create_frmMiddle()
        self.CreateDownFrame()
        bind_win()
        self.mainloop()

    def CreateUpFrame(self):
        self.frmUp=Frame(self)
        self.CreateMenuBar()
        self.frmUp.pack(side='top', fill='x')

    def create_frmMiddle(self):
        self.frmMiddle=Frame(self, border=2, relief='raised')
        self.frmMiddle.pack(side='top', expand=1, fill='both')
        self.txtReport=Text(self.frmMiddle, font='Consolas 9 normal')
        self.txtReport.pack(side='top', fill='both', expand=1)


    def CreateDownFrame(self):
        def btnGenerate_onClick(event=''):
            print '===report==='
            a=clsSmallReporter()
            self.txtReport.insert('1.0', a.HD)

        def CreateBtnExit():
            def report_exit(event=''):
                import sys
                sys.exit()
            self.btnExit=Button(self.frmDown,
                    text=ru['btnExit'],
                    command=report_exit,
                    bg='red')
            self.btnExit.pack(side='left', expand=1, fill='x')

        def CreateBtnSave():
            self.btnSave=Button(self.frmDown, text=ru['btnSave'])
            self.btnSave.pack(side='left', expand=1, fill='x')

        def CreateBtnGenerate():
            self.btnGenerate=Button(self.frmDown,
                        text=ru['btnGenerate'],
                        command=btnGenerate_onClick)
            self.btnGenerate.pack(side='left', expand=1, fill='x')


        self.frmDown=Frame(self)

        CreateBtnGenerate()
        CreateBtnSave()
        CreateBtnExit()

        self.frmDown.pack(side='bottom', fill='x')

    def CreateMenuBar(self):
        def CreateMnuFile():
            self.btnFile=Menubutton(self.pnlMenu, text=ru['mnuFile'], border=3, relief='groove')
            self.mnuFile=Menu(self.btnFile)
            self.btnFile.config(menu=self.mnuFile)
            self.mnuFile.add_command(label=ru['mnuFile_New'], accelerator='Ctrl+N')
            self.mnuFile.add_command(label=ru['mnuFile_Open'], accelerator='Ctrl+O')
            self.mnuFile.add_separator()
            self.mnuFile.add_command(label=ru['mnuFile_Save'], accelerator='Ctrl+S')
            self.mnuFile.add_command(label=ru['mnuFile_SaveAs'])
            self.mnuFile.add_separator()
            self.mnuFile.add_command(label=ru['mnuFile_Print'], accelerator='Ctrl+P')
            self.mnuFile.add_separator()
            self.mnuFile.add_command(label=ru['mnuFile_Exit'], accelerator='Ctrl+Q')
            self.btnFile.pack(side='left')

        def CreateMnuEdit():
            self.btnEdit=Menubutton(self.pnlMenu, text=ru['mnuEdit'], border=3, relief='groove')
            self.mnuEdit=Menu(self.btnEdit)
            self.btnEdit.config(menu=self.mnuEdit)
            self.mnuEdit.add_command(label=ru['mnuEdit_Undo'], accelerator='Ctrl+Z')
            self.mnuEdit.add_command(label=ru['mnuEdit_Redo'])
            self.mnuEdit.add_separator()
            self.mnuEdit.add_command(label=ru['mnuEdit_Copy'], accelerator='Ctrl+C')
            self.mnuEdit.add_command(label=ru['mnuEdit_Cut'], accelerator='Ctrl+X')
            self.mnuEdit.add_command(label=ru['mnuEdit_Paste'], accelerator='Ctrl+V')
            self.mnuEdit.add_separator()
            self.mnuEdit.add_command(label=ru['mnuEdit_Find'], accelerator='Ctrl+F')
            self.mnuEdit.add_command(label=ru['mnuEdit_Replace'], accelerator='Ctrl+R')
            self.btnEdit.pack(side='left')

        def CreateMnuCustom():
            self.btnCustom=Menubutton(self.pnlMenu, text='mnu_custom', border=3, relief='groove')
            self.mnu_custom=Menu(self.btnCustom)
            self.btnCustom.config(menu=self.mnu_custom)
            self.mnu_custom.add_command(label='Type files', accelerator='Ctrl+D')
            self.mnu_custom.add_command(label='--1')
            self.mnu_custom.add_separator()
            self.mnu_custom.add_command(label='--2', accelerator='---')
            self.mnu_custom.add_command(label='--3', accelerator='---')
            self.mnu_custom.add_command(label='--4', accelerator='---')
            self.mnu_custom.add_separator()
            self.btnCustom.pack(side='left')

        def CreateMnuHelp():
            self.btnHelp=Menubutton(self.pnlMenu, text='mnuHelp', border=3, relief='groove')
            self.mnuHelp=Menu(self.btnHelp)
            self.btnHelp.config(menu=self.mnuHelp)
            self.mnuHelp.add_command(label='Type files', accelerator='Ctrl+D')
            self.mnuHelp.add_command(label='--1')
            self.mnu_custom.add_separator()
            self.btnHelp.pack(side='left')

        self.pnlMenu=PanedWindow(self.frmUp, border=2, relief='raised')
        CreateMnuFile()
        CreateMnuEdit()
        CreateMnuCustom()
        CreateMnuHelp()

        self.pnlMenu.pack(side='left', expand=1, fill='x')

class clsSmallReporter:
    def GetDir(self, dir=''):
        '''
        Получение списка каталогов и файлов.
        '''
        a=listdir(dir)
        i=0
        # необходимо добавить полный путь к списку файлов
        while len(a)>i:
            b=a[i]
            b=dir + '\\'+ b
            a[i]=b
            i=i+1
        return a

    def GetAllFilesInPatch(self, ListElement, CurrentPatch):
        def ChekDir(fileProcess='1.py'):
            '''
            Проверка на то, является ли элемент списка каталогом или файлом.
            '''
            try:# ветка истинности файла
                fP=open(fileProcess, 'rb')
                fP.close()
            # если произошло исключение, то элемент - каталог, или занятый файл
            except:
                return 'not file'

        # пока число элементов не сравняется со счётчиком
        i=0
        while len(ListElement)>i:
            # получить текущий элемент
            CurrentElement=ListElement[i]
            # исключение самого файла репортера
            if CurrentElement==(CurrentPatch+'\\'+'__Report.py'):
                # если список не истощён - уменьшить его на один элемент
                if len(ListElement)<>i-1:
                    ListElement=ListElement[:i]+ListElement[i+1:]
                    # уменьшить список файлов-каталогов на один
                    CurrentElement=ListElement[i-1]
            # проверить на каталог и занятость
            result=ChekDir(fileProcess=CurrentElement)
            if result=='not file': # если не файл
                # то значит каталог, получить список файлов
                NewDir=self.GetDir(dir=CurrentElement)
                # вставить в основной список
                ListElement=ListElement[:i]+NewDir+ListElement[i+1:]
                # продлить итерацию на один проход
                i=i-1
            # продвинуться к следующему элементу списка
            i=i+1
        # все ветки перебраны - вернуть полный список файлов
        FullListFile=ListElement
        return FullListFile, i

    def TypeProect(self, Lines):
        '''
        Процедура по количеству строк кода определяет его крутость.
        Балл вычисляется по логарифмической шкале с десятичным основанием.
        '''
        from cmath import log10
        Lines=str(abs(log10(Lines)))
        Lines=Lines[:4]
        print 'Current ball: ',Lines
        if Lines[0]<='1':
            return 'Nano project (level '+Lines[0]+')<br>Total ball: '+Lines+'\n'
        elif Lines[0]>='1' and Lines[0]<='2':
            return 'Micro project (level '+Lines[0]+')<br>Total ball: '+Lines+'\n'
        elif Lines[0]>='2' and Lines[0]<='3':
            return 'Mini project (level '+Lines[0]+')<br>Total ball: '+Lines+'\n'
        elif Lines[0]>='3' and Lines[0]<='4':
            return 'Solid project (level '+Lines[0]+')<br>Total ball: '+Lines+'\n'
        elif Lines[0]>='4' and Lines[0]<='5':
            return 'Big project (level '+Lines[0]+')<br>Total ball: '+Lines+'\n'
        elif Lines[0]>='5' and Lines[0]<='6':
            return 'Whery big project (level '+Lines[0]+')<br>Total ball: '+Lines+'\n'
        elif Lines[0]>='6' and Lines[0]<='7':
            return 'Multi project (level '+Lines[0]+')<br>Total ball: '+Lines+'\n'
        elif Lines[0]>='7':
            return 'Global project (level'+Lines[0]+')<br>Total ball: '+Lines+'\n'

    def __init__(self):
        def save_report():
            a=open(self.NameReport +'.html','wb')
            a.write(self.HD)
            a.close

        def get_files_py():
            def SortPy(l=''):
                '''
                Проверка на то, является ли файл файлом с расширением .py
                '''
                i=0
                while len(l)>i:
                    f=l[i]
                    if f[-3:]<>'.py':
                        l=l[:i]+l[i+1:]
                        i=i-1
                    i=i+1
                return l
            # получить текущий путь
            CurrentPatch=getcwd()
            # получить список элементов каталогов/файлов
            ListElement=self.GetDir(CurrentPatch)
            # инициализация счётчика строк
            NumLines=0
            # вернуть полный список файлов
            FullListFile, self.i=self.GetAllFilesInPatch(ListElement, CurrentPatch)
            # отбросить все файлы не являющиеся .py
            self.ListFilePy=SortPy(FullListFile)

        def create_report():
            def GetTable(ListFilePy):
                def AnalisFile(f):
                    def docString(file=''):
                        '''
                        Процедура вычисляет количество строк документации.
                        '''
                        a=''# переменная строка
                        i=0 # счётчик порядкового номера строки
                        s=0 # количество строк документации
                        while i<len(file)-3: # искать символ начала комментария
                            a=file[i:i+3]

                            if (a=='"""' or a=="'''"):
                                s+=1
                            i+=1
                        return s

                    '''
                    Процедура анализирует .py файл на количество строк и
                    длинну кода.
                    '''
                    fa=open(f,'rb')# прочитать файл в переменную
                    t=fa.read()
                    fa.close()

                    NumberLine=1
                    ch=0
                    LenFile=len(t)     # получить длину файла
                    while LenFile>ch: #  проверка на количество символов ввода
                        sym=t[ch]
                        if sym=='\n': # если перевод строки увеличить счётчик строк
                            NumberLine=NumberLine+1
                        ch+=1
                    KolDocStr=docString(file=t)
                    return LenFile, NumberLine, KolDocStr

                # построение тела HTML таблицы
                Down='Plis, up<br>densyti code.'+'\n'
                Up='Plis, down<br>densyti code.'+'\n'
                body=''
                i=0
                TotalLines=0
                TotalBytes=0
                TotalDoc=0 # количество строк кода
                # пока не обнулится счётчик файлов
                col='<td bgcolor="#00FFFF" align="left">\n'
                while len(ListFilePy)>i:
                    file=ListFilePy[i]
                    LenFile, NumberLine, FileDoc=AnalisFile(file)
                    TotalDoc=TotalDoc+FileDoc
                    body=body+'<tr>'
                    body=body+col+'<h5>'+str(i+1)+'. '+'</td>'+col+'<h5>'+ str(file)+'</td>\n'
                    body=body+col+'<h5>'+ str(NumberLine)+'</td>'+col+'<h5>'+str(LenFile)+'</td>\n'
                    Densyti=Ratio(LenFile,NumberLine)
                    if Densyti=='Low':
                        Note=Down
                    elif Densyti=='Up':
                        Note=Up
                    else:
                        Note='-'
                    body=body+'<td><h5>'+Densyti+'</td><td><h5>'+Note+'</td></tr>'+'\n'
                    TotalLines=TotalLines+NumberLine
                    TotalBytes=TotalBytes+LenFile
                    i=i+1
                return body, TotalLines, TotalBytes, TotalDoc

            def Ratio(LenFile,NumberLine):
                '''
                Процедура проверяет плотность кода.
                '''
                a=LenFile/NumberLine
                if a<=14:
                    return 'Low'
                elif a>=15 and a<=59:
                    return 'Normal'
                elif a>=60:
                    return 'Hi'
                return

            def GetTime():
                '''
                    Надо получить форматированное время в виде 'гг-мм-дд_чч-мм-сс'.
                '''
                def NullTime(data):
                    '''
                    Проверка на наличие двух цифр во времени.
                    Если нет, то добавление нуля слева.
                    '''
                    if len(data)<2:
                        data='0'+data
                    return data

                from time import localtime
                # получение даты и времени
                t=localtime()
                #получить год
                god=str(t[0])
                god=NullTime(god)
                #получить месяц
                mon=str(t[1])
                mon=NullTime(mon)
                #получить день
                day=str(t[2])
                day=NullTime(day)
                # получить часы
                hour=str(t[3])
                # форматировать часы
                hour=NullTime(hour)
                # получить минуты
                minute=str(t[4])
                # форматировать минуты
                minute=NullTime(minute)
                # получить секунды
                second=str(t[5])
                # форматировать секунды
                second=NullTime(second)

                # составить общую строку времени
                result=god+'-'+mon+'-'+day+'_'+hour + '-' + minute + '-' + second
                return result


            def GetHeadHTML():
                def GetThanks():
                    '''
                    Процедурка формирует HTML-код с благодарностями и мылами.
                    '''
                    global thanks
                    # получить список кодеров
                    ListKoder=thanks.keys()
                    # проход по списку кодеров
                    out='-------------------------<br>Special thanks: <BR>'+'\n'
                    for i in xrange(len(ListKoder)):
                        # получить имя кодера
                        NameKoder=ListKoder[i]
                        # получить информацию по кодеру
                        InfoKoder=thanks[NameKoder]
                        # получить мыло кодера
                        Mail=InfoKoder['mailto']
                        # получить количество советов кодера
                        NumEdit=InfoKoder['NumEdit']
                        # получить сайт кодера
                        site=InfoKoder['site']
                        # сформировать строку
                        out+='Koder: <a href="mailto:'+Mail+'">'+NameKoder+' ('+NumEdit+')'+'\n'
                        out+='</a>'
                        out+=' Site: <a href=http://'+site+'>'+site+'</a><br>'+'\n'
                    out+='-------------------------<br>'
                    return out

                global vers, thanks
                txt='Small report for -=[fantom lab]=-<br>Desing in 2007\n\n'
                # correct charset for cyrillic path-names
                # модифицировано V.L. <arnys@mail.ru> (2+)
                HD = '<head><META HTTP-EQUIV="Content-Type" CONTENT="text/html;'+'\n'
                HD=HD+'charset=windows-1251"></head>'+'\n'
                body='<html>'+HD+'<title>Small reporter for Python</title><body bgcolor="#CCFFCC">'+'\n'
                body+='<b><center><h2>'+txt+'</center><hr></b>'+'\n'
                body+='<br><code><h5>REPORTER '+vers+'<br>'+'\n'
                body+='<a href=http://www.fantom-lab.narod.ru>www.fantom-lab.narod.ru</a><br>'+'\n'
                body+='Author: <a href="mailto:fantom-ab@mail.ru">-=[fantom]=-</a><br>'+'\n'
                body+=GetThanks()
                body+='<b>Summary info:<br>'+'\n'
                body+='<table border=3 width=100% bgcolor="#00FFFF">'+'\n'
                col='<td bgcolor="#C0C0C0" align="center">'+'\n'
                body+='<tr>'+col+'<b>Number<br>file</b></td>'+col+'<b>'+'\n'
                body+='Name File</b></td>'+col+'<b>Number<br>lines</b></td>'+'\n'
                body+=col+'<b>All<br>bytes</b></td>'+col+'<b><h5>Densyti<br>code</b>'+'\n'
                body+='</td>'+col+'<b>Note</b></td></tr>'+'\n'
                body=HD+body
                return body

            def GetEndHTML(TotalPyFiles,NameReport, TotalLines, TotalBytes, TotalDoc):
                def SpezInfo():
                    '''
                    Процедура выводит информацию о проекте и суммирует номер сборки
                    '''
                    try:
                        from _info import clsInfo
                        col='<td bgcolor="#C0C0C0" align="center">'+'\n'
                        string='<br><table border=3 width=60% bgcolor="#00FFFF">'+'\n'
                        string+='<tr>'+col+'<h5>Parametrs</td>'+col+'<h5>Variable</td></tr>'+'\n'
                        a=clsInfo()
                        string+='<tr><td><h5>Author</td><td><h5>'+a.author()+'</td></tr>'+'\n'
                        string+='<tr><td><h5>Project</td><td><h5>'+a.project()+'</td></tr>'+'\n'
                        string+='<tr><td><h5>About</td><td><h5>'+a.about()+'</td></tr>'+'\n'
                        string+='<tr><td><h5>Version</td><td><h5>'+a.version()+'</td></tr>'+'\n'
                        string+='<tr><td><h5>Build</td><td><h5>'+a.build()+'</td></tr></table>'+'\n'
                        return string
                    except:
                        return'''
</code><hr>
</b><h3>Plis, add Your project file <font color="#0808FF"><b>'_info.py'</font><br>
All variables defined programmers self.<br>
This file must content string:<br><code><h5>
<p style="margin-top: 0; margin-bottom: 0"><font color="#800080"><i><b># -*-
coding: cp1251 -*-</b></i></font></p>
<p style="margin-top: 0; margin-bottom: 0"><b>class</b> <font color="#0000FF">
clsInfo</font>:</p>
<p style="margin-top: 0; margin-bottom: 0">&nbsp;&nbsp; <b>def</b> __init__(<b><font color="#000080">self</font></b>):<br>
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
<p style="margin-top: 0; margin-bottom: 0"><span lang="ru">&nbsp; </span><b>def</b>
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

                def densytiDocString(KolString, KolLine):
                    '''
                    Процедура вычисляет плотность строк документации
                    KolString - количество строк документации
                    KolLine   - количество строк кода
                    '''
                    KolLine+=0.0
                    densyti=KolLine/KolString
                    a=str(densyti)
                    a=a[0:5]
                    if a<str(1.0/10):
                        m='<font color="#808000">Plis, up densyti DocString!</font>'
                    elif a>str(1.0/10) and a<str(1.0/5):
                        m='Normal densyti DocString.'
                    else:
                        m='<font color="#808000">Plis, down densyti DocString!</font>'
                    return m

                # получить конец таблицы
                body=''
                body+='</tr></table><br>'+'\n'
                body+='<b>Date: '+NameReport+'</b><br>'+'\n'
                body+=SpezInfo()
                body+='<br><table border=3 width=100% bgcolor="#00FFFF"><tr><td>'+'\n'
                body+='<b><h5>Total lines='+str(TotalLines)+'</td><td>'+'\n'
                body+='<b><h5>Total bytes='+str(TotalBytes)+'</td><td>'+'\n'
                body+='<b><h5>Total Files='+str(TotalPyFiles)+'</td><td><b><h5>'+'\n'
                body+='Densyti code='+Ratio(TotalBytes, TotalLines)
                body+='</td></tr><tr><td><h5>Total String docs:</td><td>'+'\n'
                body+='<h5>'+str(TotalDoc)+'</td>'+'\n'
                body+='<td><h5>Densyti docs</td><td><h5>'+\
                    str(densytiDocString(TotalLines,TotalDoc))+'</tr></table><br><br>'+'\n'
                body+='Size Project: '+ self.TypeProect(TotalLines)+ '</body></html>'+'\n'
                return body

            # модифицировано V.L. <arnys@mail.ru>(1+)
            if not self.ListFilePy:
                print 'Can not create report - files *.py not found!'
                return
            print 'Number All file=',self.i ,',\t*.py files=',len(self.ListFilePy)
            self.NameReport=GetTime()
            print 'Report file: '+ self.NameReport+'.html'
            self.HD=GetHeadHTML()
            body, TotalLines, TotalBytes, TotalDoc=GetTable(self.ListFilePy)
            self.HD+=body
            TotalPyFiles=len(self.ListFilePy)
            body=GetEndHTML(TotalPyFiles,
                        self.NameReport,
                        TotalLines,
                        TotalBytes,
                        TotalDoc)
            self.HD+=body

        get_files_py()
        create_report()
        save_report()

if __name__=='__main__':
    print '**********************************************'
    print 'Begin report....'
    # вызов репортера на исполнение
    #report=clsSmallReporter()
    #raw_input('Press <Enter> key...\n' )
    rep=ClsGUI()
    print'**********************************************'
