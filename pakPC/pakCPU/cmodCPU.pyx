# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''

cdef struct Mem: # описание структуры памяти
    int adr[0xFFFF]
    int max_adr

cdef struct RegPC: # описание регистра программного счётчика
    int val     # текущее значение регистра программного счётчика
    int max_adr # макисмальное значение регистра
    
cdef struct Reg: # описание структуры регистра общего назначения
    int val     # текущее значение регистра
    int FlagZ   # флаг нуля
    int FlagO   # флаг переполнения
    int FlagC   # флаг переноса
    int FlagS   # флаг знака
    
# константы для регистров
if True:
    DEF REG_MASK=0b110000000 # маска для возможных регистров
    DEF REG_A=0x0
    DEF REG_B=0x1
    DEF REG_C=0x2
    DEF NOT_REG=0x03

# константы для кодов операций
if True:
    DEF A_set_A=0
    DEF A_add_A=1
    DEF A_sub_A=2
    DEF A_inc_A=3
    DEF A_dec_A=4
    DEF A_not_A=5
    DEF A_xor_A=6
    DEF A_or_A =7
    DEF A_and_A=8
    DEF A_shr_A=9
    DEF A_shl_A=10
    DEF A_set_n=11
    DEF A_add_n=12
    DEF A_sub_n=13
    DEF A_not_n=14
    DEF A_xor_n=15
    DEF A_or_n =16
    DEF A_and_n=17
    DEF A_set_nn=18
    DEF A_add_nn=19
    DEF A_sub_nn=20
    DEF A_inc_nn=21
    DEF A_dec_nn=22
    DEF A_not_nn=23
    DEF A_xor_nn=24
    DEF A_or_nn =25
    DEF A_and_nn=26
    DEF A_shr_nn=27
    DEF A_shl_nn=28
    

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
    cdef Reg RegA, RegB   # определение регистров общего назначения
    cdef int max_val # максимальное значение регистра или ячейки памяти
    cdef RegPC PC          # программный счётчик
    cdef Mem *Mem           # память виртуального компьютера
    cdef int nn         # служебная переменная для хранения адреса ячейки памяти
    
    def __init__(self, root=None):
        self.root=root
        
        self.max_val=self.root.Res.max_reg_val
       
        # инициализация памяти виртуального компьютера
        cdef int i=0
        for i in xrange(0,self.Mem.max_adr):
            self.Mem.adr[i]=0
        
        self.PC.val=0
        self.PC.max_adr=self.root.Res.max_adr
        
        self.RegA.val=0
        self.RegA.FlagZ=1
        self.RegA.FlagO=0
        self.RegA.FlagC=0
        self.RegA.FlagS=0
        
        self.RegB.val=0
        self.RegB.FlagZ=1
        self.RegB.FlagO=0
        self.RegB.FlagC=0
        self.RegB.FlagS=0
        
    cpdef run(self):
        pass
    
    cpdef step(self):
        self.detect()
        
    cdef detect(self):
        '''
        Процедурка занимается детектированием поступивших команд.
        '''
        cdef int cop=0 # текущий код операции
        cdef int reg=0 # текущий регистр
        cdef int nn=0
        
        cop=self.Mem.adr[self.PC.val]     # получить текущую команду из памяти
        # сначала вычислить регистр
        reg=(cop & REG_MASK)>>8
        if reg<REG_A or reg>=NOT_REG:
            print 'ERROR! In', self.PC.val, 'invalid reg! reg=', reg
            return 1
        # если это всё-таки регистр -- продолжить детектирование
        if cop==A_set_A:          # установка значения регистра А значением регистра А
            self.PC.val+=1           # выровнять укзатель команд на следующую команду
            # сбросить все флаги, кроме Zero и Signed
            self.RegA.FlagO=0
            self.RegA.FlagC=0
        elif cop==A_add_A:        # установка регистра А со сложением содержимого регистра А
            self.RegA.val+=self.RegA.val
            if self.RegA.val>=self.max_val: # если в регистре перебор
                self.RegA.FlagO=1   # установить флаг перебора
                self.RegA.val=self.max_val-self.RegA.val
            self.PC.val+=1
            # установка необходимых флагов
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
        elif cop==A_sub_A:        # установка регистра А с вычитанием содержимого регистра А
            self.RegA.val=0
            self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_inc_A:        # установка регистра А с инкрементом содержимого регистра А
            self.RegA.val+=1
            if self.RegA.val>=self.max_val: # если в регистре перебор
                self.RegA.FlagO=1   # установить флаг перебора
                self.RegA.val=self.max_val-self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_dec_A:        # установка регистра А с декрементом содержимого регистра А
            self.RegA.val-=1
            if self.RegA.val<0: # если в регистре недобор
                self.RegA.FlagC=1   # установить флаг заёма
                self.RegA.val=self.max_val+self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.PC.val+=1
        elif cop==A_not_A:      # инвертировать регистр А инверсным значением регистра А
            self.RegA.val=~self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_xor_A:      # поксорить регистр А значением регистра А
            self.RegA.val=0
            self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_or_A:      # OR регистра А со значением регистра А
            self.PC.val+=1
        elif cop==A_and_A:      # AND регистра А со значением регистра А
            self.PC.val+=1
        elif cop==A_shr_A:      # сдвиг вправо регистра А со значением регистра А
            self.RegA.val>>=1
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_shl_A:      # сдвиг влево регистра А со значением регистра А
            self.RegA.val<<=1
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            if self.RegA.val>self.max_val: # превышено ли максимальное значение?
                self.RegA.FlagO=1
                self.RegA.val=self.RegA.val-self.max_val
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_set_n:      # установить регистр А значением числа n
            self.PC.val+=1
            self.RegA.val=self.Mem.adr[self.PC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_add_n:        # установка регистра А со сложением содержимого числа n
            self.PC.val+=1
            self.RegA.val+=self.Mem.adr[self.PC.val]
            if self.RegA.val>=self.max_val: # если в регистре перебор
                self.RegA.FlagO=1   # установить флаг перебора
                self.RegA.val=self.max_val-self.RegA.val
            self.PC.val+=1
            # установка необходимых флагов
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
        elif cop==A_sub_n:        # установка регистра А с вычитанием числа n
            self.PC.val+=1
            self.RegA.val=self.RegA.val-self.Mem.adr[self.PC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            if self.RegA.val<0:
                self.RegA.val=self.max_val+self.RegA.val
                self.RegA.FlagS=1
            else:
                self.RegA.FlagS=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.PC.val+=1
        elif cop==A_not_n:      # инвертировать регистр А инверсным значением числа n
            self.PC.val+=1
            self.RegA.val=~self.Mem.adr[self.PC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_xor_n:      # поксорить регистр А значением n
            self.PC.val+=1
            self.RegA.val^=self.Mem.adr[self.PC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_or_n:      # OR регистра А со значением n
            self.PC.val+=1
            self.RegA.val|=self.Mem.adr[self.PC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_and_n:      # AND регистра А со значением n
            self.PC.val+=1
            self.RegA.val&=self.Mem.adr[self.PC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_set_nn:      # установка значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.Mem.adr[nn] # присовить
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=2
        elif cop==A_add_nn:      # сложение значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val+=self.Mem.adr[nn] # сложить
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            if self.RegA.val>=self.max_val:
                self.RegA.val=self.RegA.val-self.max_val
                self.RegA.FlagO=1
            else:
                self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=2
        elif cop==A_sub_nn:      # вычитание значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val-=self.Mem.adr[nn] # сложить
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            if self.RegA.val<0:
                self.RegA.val=self.RegA.val*(-1)
                self.RegA.FlagC=1
                self.RegA.FlagS=1
            else:
                self.RegA.FlagC=0
                self.RegA.FlagS=0
            self.RegA.FlagO=0
            self.PC.val+=2
        elif cop==A_inc_nn:      # увеличить на 1 значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.Mem.adr[nn]+1 # сложить
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            if self.RegA.val>=self.max_val:
                self.RegA.val=self.RegA.val-self.max_val
                self.RegA.FlagO=1
            else:
                self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_dec_nn:      # уменьшить на 1 значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.Mem.adr[nn]-1 # вычесть
            if self.RegA.val==0:
                self.RegA.FlagZ=1
                self.RegA.FlagC=0
            else:
                self.RegA.FlagZ=0
            if self.RegA.val<=0:
                self.RegA.val=self.max_val
                self.RegA.FlagC=1
            else:
                self.RegA.FlagC=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.PC.val+=2
        elif cop==A_not_nn:      # инвертировать значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=~self.Mem.adr[nn] # инвертировать
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_xor_nn:      # исключающее ИЛИ значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val^=self.Mem.adr[nn] # исключающее ИЛИ
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_or_nn:      # логическое И значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val|=self.Mem.adr[nn] # логическое ИЛИ
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_and_nn:      # логическое И значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val&=self.Mem.adr[nn] # логическое ИЛИ
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_shr_nn:      # правый сдвиг значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val>>self.Mem.adr[nn] # правый сдвиг
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_shl_nn:      # левый сдвиг значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val<<self.Mem.adr[nn] # левый сдвиг
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
