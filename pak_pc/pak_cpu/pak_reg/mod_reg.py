# -*- coding: utf8 -*-
"""
Класс регистра общего назначения.
По умолчанию класс имеет 8 бит (0...255) -- MAX_REG_VAL
"""
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
    A_MXOR = 24
    A_MOR = 25
    A_MAND = 26
    A_MSHR = 27
    A_MSHL = 28
    #-----------------
    A_GETF = 29
    A_SETF = 30
    #---------------
    A_IFZ = 31
    A_NCMP = 32
    A_IFNZ = 33
    A_MSET = 34
    A_PUSH = 35
    A_POP = 36
    A_CALL = 37
    A_RET = 38
    A_IN = 39
    A_OUT = 40
    A_JMP = 41
    A_JMPR = 42


class ClsReg(object):
    """
    Класс описывает регистр общего назначения.
    :param root:
    :param mem:
    :param pc:
    :param sp:
    :param port:
    """

    def __init__(self, root=None,
                 mem=None,
                 pc=None,
                 sp=None,
                 port=None):
        self.__root = root

        # максимальное значение в регистре
        self.max_val = 2 ** 16

        # ссылка на память
        self.mem = mem

        # ссылка на порты
        self.port = port

        # сылка на программный счётчик
        self.reg_pc = pc

        # ссылка на указатель стека
        self.reg_sp = sp

        # ссылка на регистр программного прерывания
        self.reg_bp = self.__root.reg_bp

        # сбросить регистр в ноль и установить флаг нуля
        self.val = 0
        self.flag_z = 1
        self.flag_o = 0
        self.flag_c = 0
        self.flag_s = 0

    def command(self):
        """
            Вычисляет что за команда поступила на вход и
            далее обрабатывает её, в зависимости от кода
            --------------------
            cop - "код операции"
            -------------------
        """
        # признак "нельзя перебивать флаг Z" -- для команды сравнения с числом
        NOT_SET_Z = 0

        # проверить на достижение программного бряка -- регистр ВР
        if self.reg_bp.flag_act == 1:
            if self.reg_bp.adr_break == self.reg_pc.val:
                print '    reg_pc BREAK!!!'
                self.reg_bp.adr_old = self.reg_pc.val
                self.reg_pc.val = self.reg_bp.adr_proc

        cop = self.mem.adr[self.reg_pc.val]
        # print 'PC=', self.reg_pc.val, 'cop=', cop
        if cop == A_NOP:  # тупой пропуск команды
            # выровнять укзатель команд на следующую команду
            self.reg_pc.val += 1
        # установка регистра А со сложением содержимого регистра А
        elif cop == A_RADD:
            self.val += self.val
            if self.val >= self.max_val:  # если в регистре перебор
                self.flag_o = 1  # установить флаг перебора
                self.val = self.max_val - self.val
            self.reg_pc.val += 1
            # установка необходимых флагов
            self.flag_c = 0
            self.flag_s = 0
        # установка регистра А с вычитанием содержимого регистра А
        elif cop == A_RSUB:
            self.val = 0
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        # установка регистра А с инкрементом содержимого регистра А
        elif cop == A_RINC:
            self.val += 1
            if self.val >= self.max_val:  # если в регистре перебор
                self.flag_o = 1  # установить флаг перебора
                self.val = self.max_val - self.val
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        # установка регистра А с декрементом содержимого регистра А
        elif cop == A_RDEC:
            self.val -= 1
            if self.val < 0:  # если в регистре недобор
                self.flag_c = 1  # установить флаг заёма
                self.val = self.max_val + self.val
            self.flag_o = 0
            self.reg_pc.val += 1
        # инвертировать регистр А инверсным значением регистра А
        elif cop == A_RNOT:
            self.val = ~self.val
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_RXOR:  # поксорить регистр А значением регистра А
            self.val = 0
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_ROR:  # OR регистра А со значением регистра А
            self.reg_pc.val += 1
        elif cop == A_RAND:  # AND регистра А со значением регистра А
            self.reg_pc.val += 1
        elif cop == A_RSHR:  # сдвиг вправо регистра А со значением регистра А
            self.val >>= 1
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_RSHL:  # сдвиг влево регистра А со значением регистра А
            self.val <<= 1
            if self.val > self.max_val:  # превышено ли максимальное значение?
                self.flag_o = 1
                self.val = self.val - self.max_val
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_NSET:  # установить регистр А значением числа n
            self.reg_pc.val += 1
            self.val = self.mem.adr[self.reg_pc.val]
            #self.flag_o=1
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        # установка регистра А со сложением содержимого числа n
        elif cop == A_NADD:
            self.reg_pc.val += 1
            self.val += self.mem.adr[self.reg_pc.val]
            if self.val >= self.max_val:  # если в регистре перебор
                self.flag_o = 1  # установить флаг перебора
                self.val = self.max_val - self.val
            self.reg_pc.val += 1
            # установка необходимых флагов
            self.flag_c = 0
            self.flag_s = 0
        elif cop == A_NSUB:  # установка регистра А с вычитанием числа n
            self.reg_pc.val += 1
            self.val = self.val - self.mem.adr[self.reg_pc.val]
            if self.val < 0:
                self.val = self.max_val + self.val
                self.flag_s = 1
            else:
                self.flag_s = 0
            self.flag_o = 0
            self.flag_c = 0
            self.reg_pc.val += 1
        # инвертировать регистр А инверсным значением числа n
        elif cop == A_NNOT:
            self.reg_pc.val += 1
            self.val = ~self.mem.adr[self.reg_pc.val]
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_NXOR:  # поксорить регистр А значением n
            self.reg_pc.val += 1
            self.val ^= self.mem.adr[self.reg_pc.val]
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_NOR:  # OR регистра А со значением n
            self.reg_pc.val += 1
            self.val |= self.mem.adr[self.reg_pc.val]
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_NAND:  # AND регистра А со значением n
            self.reg_pc.val += 1
            self.val &= self.mem.adr[self.reg_pc.val]
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 1
        # установка значения регистра А из ячейки с адресом nn
        elif cop == A_MGET:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.mem.get_adr(mem)  # присовить
            self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 2
        # сложение значения регистра А из ячейки с адресом nn
        elif cop == A_MADD:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val += self.mem.get_adr(mem)  # сложить
            if self.val >= self.max_val:
                self.val = self.val - self.max_val
                self.flag_o = 1
            else:
                self.flag_o = 0
            self.flag_c = 0
            self.flag_s = 0
            self.reg_pc.val += 2
        # вычитание значения регистра А из ячейки с адресом nn
        elif cop == A_MSUB:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val -= self.mem.get_adr(mem)  # сложить
            if self.val < 0:
                self.val = self.val * (-1)
                self.flag_c = 1
                self.flag_s = 1
            else:
                self.flag_c = 0
                self.flag_s = 0
            self.flag_o = 0
            self.reg_pc.val += 2
        # увеличить на 1 значение регистра А из ячейки с адресом nn
        elif cop == A_MINC:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.mem.adr[mem] + 1  # сложить
            if self.val >= self.max_val:
                self.val = self.val - self.max_val
                self.flag_o = 1
            else:
                self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 2
        # уменьшить на 1 значение регистра А из ячейки с адресом nn
        elif cop == A_MDEC:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.mem.get_adr(mem) - 1  # вычесть
            if self.val == 0:
                self.flag_c = 0
            if self.val <= 0:
                self.val = self.max_val
                self.flag_c = 1
            else:
                self.flag_c = 0
            self.flag_o = 0
            self.flag_s = 0
            self.reg_pc.val += 2
        # инвертировать значение регистра А из ячейки с адресом nn
        elif cop == A_MNOT:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = ~self.mem.adr[mem]  # инвертировать
            self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 2
        # исключающее ИЛИ значение регистра А из ячейки с адресом nn
        elif cop == A_MXOR:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val ^= self.mem.adr[mem]  # исключающее ИЛИ
            self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 2
        # логическое И значение регистра А из ячейки с адресом nn
        elif cop == A_MOR:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val |= self.mem.adr[mem]  # логическое ИЛИ
            self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 2
        # логическое И значение регистра А из ячейки с адресом nn
        elif cop == A_MAND:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val &= self.mem.adr[mem]  # логическое ИЛИ
            self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 2
        # правый сдвиг значения регистра А из ячейки с адресом nn
        elif cop == A_MSHR:
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.val >> self.mem.adr[mem]  # правый сдвиг
            self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 2
        elif cop == A_MSHL:  # получить флаги регистра А
            mem = self.mem.adr[
                self.reg_pc.val + 1]  # получить адрес nn, в котором лежит число
            self.val = self.val >> self.mem.adr[mem]  # левый сдвиг
            self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 2
        elif cop == A_GETF:  # получить флаги регистра А в регистр А
            self.val = 0
            if self.flag_z == 1:
                self.val += 1
                self.flag_z = 0

            if self.flag_c == 1:
                self.val += 2

            if self.flag_o == 1:
                self.val += 4

            if self.flag_s == 1:
                self.val += 8

            self.flag_o = 0
            self.flag_s = 0
            self.flag_c = 0
            self.reg_pc.val += 1
        elif cop == A_SETF:  # установить флаги регистра А из регистра А
            if self.val & 1:
                self.flag_z = 1
            else:
                self.flag_z = 0

            if self.val & 2:
                self.flag_c = 1
            else:
                self.flag_c = 0

            if self.val & 4:
                self.flag_o = 1
            else:
                self.flag_o = 0

            if self.val & 8:
                self.flag_s = 1
            else:
                self.flag_s = 0
            self.reg_pc.val += 1
        elif cop == A_IFZ:  # переход если Z==1
            if self.flag_z == 1:
                # переход, если регистр А равен нулю
                self.reg_pc.val = self.mem.adr[self.reg_pc.val + 1]
            else:
                self.reg_pc.val += 2
        elif cop == A_NCMP:  # сравнить с числом
            self.reg_pc.val += 1
            if self.val == self.mem.adr[self.reg_pc.val]:
                self.flag_z = 1
            else:
                self.flag_z = 0
            self.reg_pc.val += 1
            NOT_SET_Z = 1
        elif cop == A_IFNZ:  # переход если Z==0
            if self.flag_z == 0:
                # переход, если регистр А равен нулю
                self.reg_pc.val = self.mem.adr[self.reg_pc.val + 1]
            else:
                self.reg_pc.val += 2
        elif cop == A_MSET:  # сохранить регистр А по адресу nn
            self.reg_pc.val += 1
            # переход, если регистр А равен нулю
            self.mem.adr[self.reg_pc.val] = self.val
            self.reg_pc.val += 1
        elif cop == A_PUSH:  # сохранить регистр А в стеке
            self.reg_sp.val -= 1
            self.mem.adr[self.reg_sp.val] = self.val
            self.reg_pc.val += 1
        elif cop == A_POP:  # восстановить регистр А из стека
            self.val = self.mem.adr[self.reg_sp.val]
            self.reg_sp.val += 1
            self.reg_pc.val += 1
        elif cop == A_CALL:  # вызвать процедуру по адресу в mem
            self.reg_sp.val -= 1
            self.mem.adr[self.reg_sp.val] = self.reg_pc.val + 2
            self.reg_pc.val = self.mem.adr[self.reg_pc.val + 1]
        elif cop == A_RET:  # возврат из процедуры
            self.reg_pc.val = self.mem.adr[self.reg_sp.val]
            self.reg_sp.val += 1
        elif cop == A_IN:  # чтение из порта в регистр А
            port = self.port.adr[self.mem.adr[self.reg_pc.val + 1]]
            print 'clsReg: port=', port
            # вызов процедуры детектирования используемого порта
            # если порт висит в воздухе, то просто возврат хранимого
            # значения.
            self.val = self.port.detect_port(port=port)
            self.reg_pc.val += 2
        elif cop == A_OUT:  # запись в порт
            self.port.adr[self.mem.adr[self.reg_pc.val + 1]] = self.val
            print 'clsReg: port=', self.mem.adr[self.reg_pc.val + 1]
            self.port.detect_port(port=self.mem.adr[self.reg_pc.val + 1],
                                  com=self.val)
            self.reg_pc.val += 2
        elif cop == A_JMP:  # прыжок по абсолютному адресу
            self.reg_pc.val += 1
            self.reg_pc.val = self.mem.adr[self.reg_pc.val]
        elif cop == A_JMPR:  # прыжок по относительному адресу
            #self.reg_pc.val+=1
            self.reg_pc.val = self.reg_pc.val + self.mem.adr[
                self.reg_pc.val + 1]


        #-------control flag_z--------------
        if NOT_SET_Z == 0 and self.val == 0:
            self.flag_z = 1
        else:
            self.flag_z = 0
