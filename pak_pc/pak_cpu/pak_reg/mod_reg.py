# -*- coding: utf8 -*-
'''
Класс регистра общего назначения.
По умолчанию класс имеет 8 бит (0...255) -- MAX_REG_VAL
'''
# константы для кодов операций
if True:
    A_NOP = 0
    A_RADD = 1
    A_RSUB = 2
    A_RINC = 3
    A_RDEC = 4
    A_RNOT = 5
    A_RXOR = 6
    A_ROR = 7
    A_RAND = 8
    A_RSHR = 9
    A_RSHL = 10
    # ----------------------
    A_NSET = 11
    A_NADD = 12
    A_NSUB = 13
    A_NNOT = 14
    A_NXOR = 15
    A_NOR = 16
    A_NAND = 17
    #---------------------
    A_MGET = 18
    A_MADD = 19
    A_MSUB = 20
    A_MINC = 21
    A_MDEC = 22
    A_MNOT = 23
    A_mxor = 24
    A_mor = 25
    A_mand = 26
    A_mshr = 27
    A_mshl = 28
    #-----------------
    A_getf = 29
    A_setf = 30
    #---------------
    A_ifz = 31
    A_ncmp = 32
    A_ifnz = 33
    A_mset = 34
    A_push = 35
    A_pop = 36
    A_call = 37
    A_ret = 38
    A_in = 39
    A_out = 40
    A_jmp = 41
    A_jmpr = 42


class ClsReg:
    def __init__(self, root=None,
                 mem=None,
                 pc=None,
                 sp=None,
                 port=None,
                 vcom=None,
                 vinfo=None):
        self.root = root

        # максимальное значение в регистре
        self.max_val = 2 ** 16

        # ссылка на память
        self.Mem = mem

        # ссылка на порты
        self.Port = port

        # сылка на программный счётчик
        self.reg_pc = pc

        # ссылка на указатель стека
        self.reg_sp = sp

        # ссылка на регистр программного прерывания
        self.reg_bp = self.root.reg_bp

        # сбросить регистр в ноль и установить флаг нуля
        self.val = 0
        self.FlagZ = 1
        self.FlagO = 0
        self.FlagC = 0

    def command(self):
        '''
            Вычисляет что за команда поступила на вход и
            далее обрабатывает её, в зависимости от кода
            --------------------
            cop - "код операции"
            -------------------
        '''
        # признак "нельзя перебивать флаг Z" -- для команды сравнения с числом
        not_Z = 0

        # проверить на достижение программного бряка -- регистр ВР
        if self.reg_bp.act == 1:
            if self.reg_bp.adr_break == self.reg_pc.val:
                print '    reg_pc BREAK!!!'
                self.reg_bp.adr_old = self.reg_pc.val
                self.reg_pc.val = self.reg_bp.adr_proc

        cop = self.Mem.adr[self.reg_pc.val]
        # print 'PC=', self.reg_pc.val, 'cop=', cop
        if cop == A_NOP:  # тупой пропуск команды
            # выровнять укзатель команд на следующую команду
            self.reg_pc.val += 1
        # установка регистра А со сложением содержимого регистра А
        elif cop == A_RADD:
            self.val += self.val
            if self.val >= self.max_val:  # если в регистре перебор
                self.FlagO = 1  # установить флаг перебора
                self.val = self.max_val - self.val
            self.reg_pc.val += 1
            # установка необходимых флагов
            self.FlagC = 0
            self.FlagS = 0
        # установка регистра А с вычитанием содержимого регистра А
        elif cop == A_RSUB:
            self.val = 0
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        # установка регистра А с инкрементом содержимого регистра А
        elif cop == A_RINC:
            self.val += 1
            if self.val >= self.max_val:  # если в регистре перебор
                self.FlagO = 1  # установить флаг перебора
                self.val = self.max_val - self.val
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        # установка регистра А с декрементом содержимого регистра А
        elif cop == A_RDEC:
            self.val -= 1
            if self.val < 0:  # если в регистре недобор
                self.FlagC = 1  # установить флаг заёма
                self.val = self.max_val + self.val
            self.FlagO = 0
            self.reg_pc.val += 1
        # инвертировать регистр А инверсным значением регистра А
        elif cop == A_RNOT:
            self.val = ~self.val
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_RXOR:  # поксорить регистр А значением регистра А
            self.val = 0
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_ROR:  # OR регистра А со значением регистра А
            self.reg_pc.val += 1
        elif cop == A_RAND:  # AND регистра А со значением регистра А
            self.reg_pc.val += 1
        elif cop == A_RSHR:  # сдвиг вправо регистра А со значением регистра А
            self.val >>= 1
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_RSHL:  # сдвиг влево регистра А со значением регистра А
            self.val <<= 1
            if self.val > self.max_val:  # превышено ли максимальное значение?
                self.FlagO = 1
                self.val = self.val - self.max_val
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_NSET:  # установить регистр А значением числа n
            self.reg_pc.val += 1
            self.val = self.Mem.adr[self.reg_pc.val]
            #self.FlagO=1
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        # установка регистра А со сложением содержимого числа n
        elif cop == A_NADD:
            self.reg_pc.val += 1
            self.val += self.Mem.adr[self.reg_pc.val]
            if self.val >= self.max_val:  # если в регистре перебор
                self.FlagO = 1  # установить флаг перебора
                self.val = self.max_val - self.val
            self.reg_pc.val += 1
            # установка необходимых флагов
            self.FlagC = 0
            self.FlagS = 0
        elif cop == A_NSUB:  # установка регистра А с вычитанием числа n
            self.reg_pc.val += 1
            self.val = self.val - self.Mem.adr[self.reg_pc.val]
            if self.val < 0:
                self.val = self.max_val + self.val
                self.FlagS = 1
            else:
                self.FlagS = 0
            self.FlagO = 0
            self.FlagC = 0
            self.reg_pc.val += 1
        # инвертировать регистр А инверсным значением числа n
        elif cop == A_NNOT:
            self.reg_pc.val += 1
            self.val = ~self.Mem.adr[self.reg_pc.val]
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_NXOR:  # поксорить регистр А значением n
            self.reg_pc.val += 1
            self.val ^= self.Mem.adr[self.reg_pc.val]
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_NOR:  # OR регистра А со значением n
            self.reg_pc.val += 1
            self.val |= self.Mem.adr[self.reg_pc.val]
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_NAND:  # AND регистра А со значением n
            self.reg_pc.val += 1
            self.val &= self.Mem.adr[self.reg_pc.val]
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 1
        # установка значения регистра А из ячейки с адресом nn
        elif cop == A_MGET:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.Mem.get_adr(m)  # присовить
            self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 2
        # сложение значения регистра А из ячейки с адресом nn
        elif cop == A_MADD:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val += self.Mem.get_adr(m)  # сложить
            if self.val >= self.max_val:
                self.val = self.val - self.max_val
                self.FlagO = 1
            else:
                self.FlagO = 0
            self.FlagC = 0
            self.FlagS = 0
            self.reg_pc.val += 2
        # вычитание значения регистра А из ячейки с адресом nn
        elif cop == A_MSUB:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val -= self.Mem.get_adr(m)  # сложить
            if self.val < 0:
                self.val = self.val * (-1)
                self.FlagC = 1
                self.FlagS = 1
            else:
                self.FlagC = 0
                self.FlagS = 0
            self.FlagO = 0
            self.reg_pc.val += 2
        # увеличить на 1 значение регистра А из ячейки с адресом nn
        elif cop == A_MINC:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.Mem.adr[m] + 1  # сложить
            if self.val >= self.max_val:
                self.val = self.val - self.max_val
                self.FlagO = 1
            else:
                self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 2
        # уменьшить на 1 значение регистра А из ячейки с адресом nn
        elif cop == A_MDEC:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.Mem.get_adr(m) - 1  # вычесть
            if self.val == 0:
                self.FlagC = 0
            if self.val <= 0:
                self.val = self.max_val
                self.FlagC = 1
            else:
                self.FlagC = 0
            self.FlagO = 0
            self.FlagS = 0
            self.reg_pc.val += 2
        # инвертировать значение регистра А из ячейки с адресом nn
        elif cop == A_MNOT:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = ~self.Mem.adr[m]  # инвертировать
            self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 2
        # исключающее ИЛИ значение регистра А из ячейки с адресом nn
        elif cop == A_mxor:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val ^= self.Mem.adr[m]  # исключающее ИЛИ
            self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 2
        # логическое И значение регистра А из ячейки с адресом nn
        elif cop == A_mor:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val |= self.Mem.adr[m]  # логическое ИЛИ
            self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 2
        # логическое И значение регистра А из ячейки с адресом nn
        elif cop == A_mand:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val &= self.Mem.adr[m]  # логическое ИЛИ
            self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 2
        # правый сдвиг значения регистра А из ячейки с адресом nn
        elif cop == A_mshr:
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.val >> self.Mem.adr[m]  # правый сдвиг
            self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 2
        elif cop == A_mshl:  # получить флаги регистра А
            m = self.Mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.val >> self.Mem.adr[m]  # левый сдвиг
            self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 2
        elif cop == A_getf:  # получить флаги регистра А в регистр А
            self.val = 0
            if self.FlagZ == 1:
                self.val += 1
                self.FlagZ = 0

            if self.FlagC == 1:
                self.val += 2

            if self.FlagO == 1:
                self.val += 4

            if self.FlagS == 1:
                self.val += 8

            self.FlagO = 0
            self.FlagS = 0
            self.FlagC = 0
            self.reg_pc.val += 1
        elif cop == A_setf:  # установить флаги регистра А из регистра А
            if self.val & 1:
                self.FlagZ = 1
            else:
                self.FlagZ = 0

            if self.val & 2:
                self.FlagC = 1
            else:
                self.FlagC = 0

            if self.val & 4:
                self.FlagO = 1
            else:
                self.FlagO = 0

            if self.val & 8:
                self.FlagS = 1
            else:
                self.FlagS = 0
            self.reg_pc.val += 1
        elif cop == A_ifz:  # переход если Z==1
            if self.FlagZ == 1:
                # переход, если регистр А равен нулю
                self.reg_pc.val = self.Mem.adr[self.reg_pc.val + 1]
            else:
                self.reg_pc.val += 2
        elif cop == A_ncmp:  # сравнить с числом
            self.reg_pc.val += 1
            if self.val == self.Mem.adr[self.reg_pc.val]:
                self.FlagZ = 1
            else:
                self.FlagZ = 0
            self.reg_pc.val += 1
            not_Z = 1
        elif cop == A_ifnz:  # переход если Z==0
            if self.FlagZ == 0:
                # переход, если регистр А равен нулю
                self.reg_pc.val = self.Mem.adr[self.reg_pc.val + 1]
            else:
                self.reg_pc.val += 2
        elif cop == A_mset:  # сохранить регистр А по адресу nn
            self.reg_pc.val += 1
            # переход, если регистр А равен нулю
            self.Mem.adr[self.reg_pc.val] = self.val
            self.reg_pc.val += 1
        elif cop == A_push:  # сохранить регистр А в стеке
            self.reg_sp.val -= 1
            self.Mem.adr[self.reg_sp.val] = self.val
            self.reg_pc.val += 1
        elif cop == A_pop:  # восстановить регистр А из стека
            self.val = self.Mem.adr[self.reg_sp.val]
            self.reg_sp.val += 1
            self.reg_pc.val += 1
        elif cop == A_call:  # вызвать процедуру по адресу в m
            self.reg_sp.val -= 1
            self.Mem.adr[self.reg_sp.val] = self.reg_pc.val + 2
            self.reg_pc.val = self.Mem.adr[self.reg_pc.val + 1]
        elif cop == A_ret:  # возврат из процедуры
            self.reg_pc.val = self.Mem.adr[self.reg_sp.val]
            self.reg_sp.val += 1
        elif cop == A_in:  # чтение из порта в регистр А
            port = self.Port.adr[self.Mem.adr[self.reg_pc.val + 1]]
            print 'clsReg: port=', port
            # вызов процедуры детектирования используемого порта
            # если порт висит в воздухе, то просто возврат хранимого
            # значения.
            self.val = self.Port.detect_port(port=port)
            self.reg_pc.val += 2
        elif cop == A_out:  # запись в порт
            self.Port.adr[self.Mem.adr[self.reg_pc.val + 1]] = self.val
            print 'clsReg: port=', self.Mem.adr[self.reg_pc.val + 1]
            self.Port.detect_port(port=self.Mem.adr[self.reg_pc.val + 1],
                                  com=self.val)
            self.reg_pc.val += 2
        elif cop == A_jmp:  # прыжок по абсолютному адресу
            self.reg_pc.val += 1
            self.reg_pc.val = self.Mem.adr[self.reg_pc.val]
        elif cop == A_jmpr:  # прыжок по относительному адресу
            #self.reg_pc.val+=1
            self.reg_pc.val = self.reg_pc.val + self.Mem.adr[
                self.reg_pc.val + 1]


        #-------control FlagZ--------------
        if not_Z == 0 and self.val == 0:
            self.FlagZ = 1
        else:
            self.FlagZ = 0
