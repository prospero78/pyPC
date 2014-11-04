# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''

#define max_adr 0xFFFF

cdef struct Mem:  # описание структуры памяти
    int adr[0xFFFF]
    int max_adr

cdef struct RegPC:  # описание регистра программного счётчика
    int val  # текущее значение регистра программного счётчика
    int max_adr  # макисмальное значение регистра
    int min_adr  # мимнимальный адрес регистра

cdef struct RegSP:  # описание регистра стека
    int val  # значение регистра стека
    int min_adr  # минмальный адрес стека

cdef struct Reg:  # описание структуры регистра общего назначения
    int val  # текущее значение регистра
    int flag_z  # флаг нуля
    int flag_o  # флаг переполнения
    int flag_c  # флаг переноса
    int flag_s  # флаг знака

cdef struct _port:  # описание структуры регистра общего назначения
    int adr[0xFFFF]  # массив портов ввода вывода
    int max_adr  # максимальный номер порта


# константы для регистров
if True:
    DEF REG_MASK=0b110000000  # маска для возможных регистров
    DEF REG_A=0x0
    DEF REG_B=0x1
    DEF REG_C=0x2
    DEF NOT_REG=0x03

# константы для кодов операций
if True:
    DEF A_rset=0
    DEF A_RADD=1
    DEF A_RSUB=2
    DEF A_RINC=3
    DEF A_RDEC=4
    DEF A_RNOT=5
    DEF A_RXOR=6
    DEF A_ROR =7
    DEF A_RAND=8
    DEF A_RSHR=9
    DEF A_RSHL=10
    #----------------------
    DEF A_NSET=11
    DEF A_NADD=12
    DEF A_NSUB=13
    DEF A_NNOT=14
    DEF A_NXOR=15
    DEF A_NOR =16
    DEF A_NAND=17
    #---------------------
    DEF A_MGET=18
    DEF A_MADD=19
    DEF A_MSUB=20
    DEF A_MINC=21
    DEF A_MDEC=22
    DEF A_MNOT=23
    DEF A_MXOR=24
    DEF A_MOR =25
    DEF A_MAND=26
    DEF A_MSHR=27
    DEF A_MSHL=28
    #-----------------
    DEF A_GETF =29
    DEF A_SETF =30
    #---------------
    DEF A_IFZ =31
    DEF A_NCMP=32
    DEF A_IFNZ=33
    DEF A_MSET=34
    DEF A_PUSH=35
    DEF A_POP =36
    DEF A_CALL=37
    DEF A_RET =38
    DEF A_IN  =39
    DEF A_OUT =40
    DEF A_VIN =40

cdef class clsCPU:
    '''
        Здесь надо хорошо подумать сколько элементарных операций будет выполнять процессор.
        Длина команды (без старшего бита) ограничена семью битами.
        Видимо, пока буду пилить один РОН, т. к. непонятно, сколько будет элементарных команд
        на один регистр. Теоретически, и одного регистра должно хватить с удовольствием. )
        ----------------------
        Класс центрального процессора обеспечивает выполнение кодов операций и 
        обработку данных.
        ----------------------
        FEDCBA98 7 6543210
                 |   |
                 |   код операции в регистре
                 два регистра общего назначения
           векторы прерываний
        расширенные команды процессора
        
        На каждый регистр отводится по 128 простых команд (7 бит)
    '''
    cdef Reg RegA, RegB  # определение регистров общего назначения
    cdef int max_val  # максимальное значение регистра или ячейки памяти
    cdef RegPC PC  # программный счётчик
    cdef Mem *Mem  # память виртуального компьютера
    cdef int nn  # служебная переменная для хранения адреса ячейки памяти
    cdef RegPC SP  # указатель стека с контролем дна
    cdef _port port  # ссылка на массив портов
    #cdef public root

    def __init__(self, root=None):
        self.root = root

        self.max_val = self.root.Res.max_reg_val

        # инициализация памяти виртуального компьютера
        cdef int i = 0
        for i in xrange(0, self.mem.max_adr):
            self.mem.adr[i] = 0

        self.SP.val = self.root.Res.max_adr
        self.SP.min_adr = self.SP.val - 100

        self.PC.val = 0
        self.PC.max_adr = self.SP.min_adr - 1  # максимальный адрес -- на 1 меньше, чем дно стека

        self.RegA.val = 0
        self.RegA.flag_z = 1
        self.RegA.flag_o = 0
        self.RegA.flag_c = 0
        self.RegA.flag_s = 0

        self.RegB.val = 0
        self.RegB.flag_z = 1
        self.RegB.flag_o = 0
        self.RegB.flag_c = 0
        self.RegB.flag_s = 0

    cpdef run(self):
        pass

    cpdef step(self):
        self.detect()

    cdef detect(self):
        '''
        Процедурка занимается детектированием поступивших команд.
        '''
        cdef int cop = 0  # текущий код операции
        cdef int reg = 0  # текущий регистр
        cdef int nn = 0

        cop = self.mem.adr[self.PC.val]  # получить текущую команду из памяти
        # сначала вычислить регистр
        reg = (cop & REG_MASK) >> 8
        #if reg<REG_A or reg>=NOT_REG:
        #    print 'ERROR! In', self.PC.val, 'invalid reg! reg=', reg
        #    return 1
        # если это всё-таки регистр -- продолжить детектирование
        if cop == A_rset:  # установка значения регистра А значением регистра А
            self.PC.val += 1  # выровнять укзатель команд на следующую команду
            # сбросить все флаги, кроме Zero и Signed
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
        elif cop == A_RADD:  # установка регистра А со сложением содержимого регистра А
            self.RegA.val += self.RegA.val
            if self.RegA.val >= self.max_val:  # если в регистре перебор
                self.RegA.flag_o = 1  # установить флаг перебора
                self.RegA.val = self.max_val - self.RegA.val
            self.PC.val += 1
            # установка необходимых флагов
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
        elif cop == A_RSUB:  # установка регистра А с вычитанием содержимого регистра А
            self.RegA.val = 0
            self.RegA.flag_z = 1
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_RINC:  # установка регистра А с инкрементом содержимого регистра А
            self.RegA.val += 1
            if self.RegA.val >= self.max_val:  # если в регистре перебор
                self.RegA.flag_o = 1  # установить флаг перебора
                self.RegA.val = self.max_val - self.RegA.val
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_RDEC:  # установка регистра А с декрементом содержимого регистра А
            self.RegA.val -= 1
            if self.RegA.val < 0:  # если в регистре недобор
                self.RegA.flag_c = 1  # установить флаг заёма
                self.RegA.val = self.max_val + self.RegA.val
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            self.RegA.flag_o = 0
            self.PC.val += 1
        elif cop == A_RNOT:  # инвертировать регистр А инверсным значением регистра А
            self.RegA.val = ~self.RegA.val
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_RXOR:  # поксорить регистр А значением регистра А
            self.RegA.val = 0
            self.RegA.flag_z = 1
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_ROR:  # OR регистра А со значением регистра А
            self.PC.val += 1
        elif cop == A_RAND:  # AND регистра А со значением регистра А
            self.PC.val += 1
        elif cop == A_RSHR:  # сдвиг вправо регистра А со значением регистра А
            self.RegA.val >>= 1
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_RSHL:  # сдвиг влево регистра А со значением регистра А
            self.RegA.val <<= 1
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            if self.RegA.val > self.max_val:  # превышено ли максимальное значение?
                self.RegA.flag_o = 1
                self.RegA.val = self.RegA.val - self.max_val
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_NSET:  # установить регистр А значением числа n
            self.PC.val += 1
            self.RegA.val = self.mem.adr[self.PC.val]
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            self.RegA.flag_o = 1
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_NADD:  # установка регистра А со сложением содержимого числа n
            self.PC.val += 1
            self.RegA.val += self.mem.adr[self.PC.val]
            if self.RegA.val >= self.max_val:  # если в регистре перебор
                self.RegA.flag_o = 1  # установить флаг перебора
                self.RegA.val = self.max_val - self.RegA.val
            self.PC.val += 1
            # установка необходимых флагов
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
        elif cop == A_NSUB:  # установка регистра А с вычитанием числа n
            self.PC.val += 1
            self.RegA.val = self.RegA.val - self.mem.adr[self.PC.val]
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            if self.RegA.val < 0:
                self.RegA.val = self.max_val + self.RegA.val
                self.RegA.flag_s = 1
            else:
                self.RegA.flag_s = 0
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.PC.val += 1
        elif cop == A_NNOT:  # инвертировать регистр А инверсным значением числа n
            self.PC.val += 1
            self.RegA.val = ~self.mem.adr[self.PC.val]
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_NXOR:  # поксорить регистр А значением n
            self.PC.val += 1
            self.RegA.val ^= self.mem.adr[self.PC.val]
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_NOR:  # OR регистра А со значением n
            self.PC.val += 1
            self.RegA.val |= self.mem.adr[self.PC.val]
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_NAND:  # AND регистра А со значением n
            self.PC.val += 1
            self.RegA.val &= self.mem.adr[self.PC.val]
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_MGET:  # установка значения регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val = self.mem.adr[nn]  # присовить
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 2
        elif cop == A_MADD:  # сложение значения регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val += self.mem.adr[nn]  # сложить
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            if self.RegA.val >= self.max_val:
                self.RegA.val = self.RegA.val - self.max_val
                self.RegA.flag_o = 1
            else:
                self.RegA.flag_o = 0
            self.RegA.flag_c = 0
            self.RegA.flag_s = 0
            self.PC.val += 2
        elif cop == A_MSUB:  # вычитание значения регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val -= self.mem.adr[nn]  # сложить
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            if self.RegA.val < 0:
                self.RegA.val = self.RegA.val * (-1)
                self.RegA.flag_c = 1
                self.RegA.flag_s = 1
            else:
                self.RegA.flag_c = 0
                self.RegA.flag_s = 0
            self.RegA.flag_o = 0
            self.PC.val += 2
        elif cop == A_MINC:  # увеличить на 1 значение регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val = self.mem.adr[nn] + 1  # сложить
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            if self.RegA.val >= self.max_val:
                self.RegA.val = self.RegA.val - self.max_val
                self.RegA.flag_o = 1
            else:
                self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 2
        elif cop == A_MDEC:  # уменьшить на 1 значение регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val = self.mem.adr[nn] - 1  # вычесть
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
                self.RegA.flag_c = 0
            else:
                self.RegA.flag_z = 0
            if self.RegA.val <= 0:
                self.RegA.val = self.max_val
                self.RegA.flag_c = 1
            else:
                self.RegA.flag_c = 0
            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.PC.val += 2
        elif cop == A_MNOT:  # инвертировать значение регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val = ~self.mem.adr[nn]  # инвертировать
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 2
        elif cop == A_MXOR:  # исключающее ИЛИ значение регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val ^= self.mem.adr[nn]  # исключающее ИЛИ
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 2
        elif cop == A_MOR:  # логическое И значение регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val |= self.mem.adr[nn]  # логическое ИЛИ
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 2
        elif cop == A_MAND:  # логическое И значение регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val &= self.mem.adr[nn]  # логическое ИЛИ
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 2
        elif cop == A_MSHR:  # правый сдвиг значения регистра А из ячейки с адресом nn
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val = self.RegA.val >> (self.mem.adr[nn])  # правый сдвиг
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 2
        elif cop == A_MSHL:  # получить флаги регистра А
            nn = self.mem.adr[
                self.PC.val + 1]  # получить адрес nn, в котором лежит число
            self.RegA.val = self.RegA.val >> self.mem.adr[nn]  # левый сдвиг
            if self.RegA.val == 0:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 2
        elif cop == A_GETF:  # получить флаги регистра А в регистр А
            self.RegA.val = 0
            if self.RegA.flag_z == 1:
                self.RegA.val += 1
                self.RegA.flag_z = 0

            if self.RegA.flag_c == 1:
                self.RegA.val += 2

            if self.RegA.flag_o == 1:
                self.RegA.val += 4

            if self.RegA.flag_s == 1:
                self.RegA.val += 8

            self.RegA.flag_o = 0
            self.RegA.flag_s = 0
            self.RegA.flag_c = 0
            self.PC.val += 1
        elif cop == A_SETF:  # установить флаги регистра А из регистра А
            if self.RegA.val & 1:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0

            if self.RegA.val & 2:
                self.RegA.flag_c = 1
            else:
                self.RegA.flag_c = 0

            if self.RegA.val & 4:
                self.RegA.flag_o = 1
            else:
                self.RegA.flag_o = 0

            if self.RegA.val & 8:
                self.RegA.flag_s = 1
            else:
                self.RegA.flag_s = 0
            self.PC.val += 1
        elif cop == A_IFZ:  # переход если "0"
            if self.RegA.flag_z == 1:
                # переход, если регистр А равен нулю
                self.PC.val = self.mem.adr[self.PC.val + 1]
            else:
                self.PC.val += 2
        elif cop == A_NCMP:  # сравнить с числом
            self.PC.val += 1
            if self.RegA.val == self.mem.adr[self.PC.val]:
                self.RegA.flag_z = 1
            else:
                self.RegA.flag_z = 0
            self.PC.val += 1
        elif cop == A_IFNZ:  # переход если "0"
            if self.RegA.flag_z <> 1:
                # переход, если регистр А равен нулю
                self.PC.val = self.mem.adr[self.PC.val + 1]
            else:
                self.PC.val += 2
        elif cop == A_MSET:  # сохранить регистр А по адресу nn
            self.PC.val += 1
            # переход, если регистр А равен нулю
            self.mem.adr[self.PC.val] = self.RegA.val
            self.PC.val += 1
        elif cop == A_PUSH:  # сохранить регистр А в стеке
            self.mem.adr[self.SP.val] = self.RegA.val
            self.SP.val -= 1
            self.PC.val += 1
        elif cop == A_POP:  # восстановить регистр А из стека
            self.RegA.val = self.mem.adr[self.SP.val]
            self.SP.val += 1
            self.PC.val += 1
        elif cop == A_CALL:  # вызвать процедуру по адресу в регистре А
            self.mem.adr[self.SP.val] = self.RegA.val
            self.SP.val -= 1
            self.PC.val = self.RegA.val
        elif cop == A_RET:  # возврат из процедуры
            self.PC.val = self.RegA.val
            self.SP.val += 1
        elif cop == A_IN:  # чтение из порта
            self.PC.val += 1
            self.RegA.val = self.port.adr[self.mem.adr[self.PC.val]]
            self.PC.val += 1
        elif cop == A_OUT:  # запись в порт
            self.PC.val += 1
            self.port.adr[self.mem.adr[self.PC.val]] = self.RegA.val
            self.PC.val += 1
            #elif cop==A_VIN:      # чтение из видеопорта
            #    self.PC.val+=1
            #    self.port.adr[self.mem.adr[self.PC.val]]=self.RegA.val
            #    self.PC.val+=1
