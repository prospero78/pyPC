# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''

#define max_adr 0xFFFF

cdef struct Mem: # описание структуры памяти
    int adr[0xFFFF]
    int max_adr

cdef struct RegPC: # описание регистра программного счётчика
    int val     # текущее значение регистра программного счётчика
    int max_adr # макисмальное значение регистра
    int min_adr # мимнимальный адрес регистра
    
cdef struct RegSP: # описание регистра стека
    int val     # значение регистра стека
    int min_adr # минмальный адрес стека

cdef struct Reg: # описание структуры регистра общего назначения
    int val     # текущее значение регистра
    int FlagZ   # флаг нуля
    int FlagO   # флаг переполнения
    int FlagC   # флаг переноса
    int FlagS   # флаг знака

cdef struct _port: # описание структуры регистра общего назначения
    int adr[0xFFFF] # массив портов ввода вывода
    int max_adr     # максимальный номер порта

    
# константы для регистров
if True:
    DEF REG_MASK=0b110000000 # маска для возможных регистров
    DEF REG_A=0x0
    DEF REG_B=0x1
    DEF REG_C=0x2
    DEF NOT_REG=0x03

# константы для кодов операций
if True:
    DEF A_rset=0
    DEF A_radd=1
    DEF A_rsub=2
    DEF A_rinc=3
    DEF A_rdec=4
    DEF A_rnot=5
    DEF A_rxor=6
    DEF A_ror =7
    DEF A_rand=8
    DEF A_rshr=9
    DEF A_rshl=10
    #----------------------
    DEF A_nset=11
    DEF A_nadd=12
    DEF A_nsub=13
    DEF A_nnot=14
    DEF A_nxor=15
    DEF A_nor =16
    DEF A_nand=17
    #---------------------
    DEF A_mget=18
    DEF A_madd=19
    DEF A_msub=20
    DEF A_minc=21
    DEF A_mdec=22
    DEF A_mnot=23
    DEF A_mxor=24
    DEF A_mor =25
    DEF A_mand=26
    DEF A_mshr=27
    DEF A_mshl=28
    #-----------------
    DEF A_getf =29
    DEF A_setf =30
    #---------------
    DEF A_ifz =31
    DEF A_ncmp=32
    DEF A_ifnz=33
    DEF A_mset=34
    DEF A_push=35
    DEF A_pop =36
    DEF A_call=37
    DEF A_ret =38
    DEF A_in  =39
    
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
    cdef RegPC SP   # указатель стека с контролем дна
    cdef _port Port # ссылка на массив портов
    
    def __init__(self, root=None):
        self.root=root
        
        self.max_val=self.root.Res.max_reg_val
       
        # инициализация памяти виртуального компьютера
        cdef int i=0
        for i in xrange(0,self.Mem.max_adr):
            self.Mem.adr[i]=0
        
        self.SP.val=self.root.Res.max_adr
        self.SP.min_adr=self.SP.val-100
        
        self.PC.val=0
        self.PC.max_adr=self.SP.min_adr-1 # максимальный адрес -- на 1 меньше, чем дно стека
        
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
        #if reg<REG_A or reg>=NOT_REG:
        #    print 'ERROR! In', self.PC.val, 'invalid reg! reg=', reg
        #    return 1
        # если это всё-таки регистр -- продолжить детектирование
        if cop==A_rset:          # установка значения регистра А значением регистра А
            self.PC.val+=1           # выровнять укзатель команд на следующую команду
            # сбросить все флаги, кроме Zero и Signed
            self.RegA.FlagO=0
            self.RegA.FlagC=0
        elif cop==A_radd:        # установка регистра А со сложением содержимого регистра А
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
        elif cop==A_rsub:        # установка регистра А с вычитанием содержимого регистра А
            self.RegA.val=0
            self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_rinc:        # установка регистра А с инкрементом содержимого регистра А
            self.RegA.val+=1
            if self.RegA.val>=self.max_val: # если в регистре перебор
                self.RegA.FlagO=1   # установить флаг перебора
                self.RegA.val=self.max_val-self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_rdec:        # установка регистра А с декрементом содержимого регистра А
            self.RegA.val-=1
            if self.RegA.val<0: # если в регистре недобор
                self.RegA.FlagC=1   # установить флаг заёма
                self.RegA.val=self.max_val+self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.PC.val+=1
        elif cop==A_rnot:      # инвертировать регистр А инверсным значением регистра А
            self.RegA.val=~self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_rxor:      # поксорить регистр А значением регистра А
            self.RegA.val=0
            self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_ror:      # OR регистра А со значением регистра А
            self.PC.val+=1
        elif cop==A_rand:      # AND регистра А со значением регистра А
            self.PC.val+=1
        elif cop==A_rshr:      # сдвиг вправо регистра А со значением регистра А
            self.RegA.val>>=1
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_rshl:      # сдвиг влево регистра А со значением регистра А
            self.RegA.val<<=1
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            if self.RegA.val>self.max_val: # превышено ли максимальное значение?
                self.RegA.FlagO=1
                self.RegA.val=self.RegA.val-self.max_val
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_nset:      # установить регистр А значением числа n
            self.PC.val+=1
            self.RegA.val=self.Mem.adr[self.PC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_nadd:        # установка регистра А со сложением содержимого числа n
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
        elif cop==A_nsub:        # установка регистра А с вычитанием числа n
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
        elif cop==A_nnot:      # инвертировать регистр А инверсным значением числа n
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
        elif cop==A_nxor:      # поксорить регистр А значением n
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
        elif cop==A_nor:      # OR регистра А со значением n
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
        elif cop==A_nand:      # AND регистра А со значением n
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
        elif cop==A_mget:      # установка значения регистра А из ячейки с адресом nn
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
        elif cop==A_madd:      # сложение значения регистра А из ячейки с адресом nn
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
        elif cop==A_msub:      # вычитание значения регистра А из ячейки с адресом nn
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
        elif cop==A_minc:      # увеличить на 1 значение регистра А из ячейки с адресом nn
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
        elif cop==A_mdec:      # уменьшить на 1 значение регистра А из ячейки с адресом nn
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
        elif cop==A_mnot:      # инвертировать значение регистра А из ячейки с адресом nn
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
        elif cop==A_mxor:      # исключающее ИЛИ значение регистра А из ячейки с адресом nn
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
        elif cop==A_mor:      # логическое И значение регистра А из ячейки с адресом nn
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
        elif cop==A_mand:      # логическое И значение регистра А из ячейки с адресом nn
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
        elif cop==A_mshr:      # правый сдвиг значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.RegA.val>>(self.Mem.adr[nn]) # правый сдвиг
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_mshl:      # получить флаги регистра А
            nn=self.Mem.adr[self.PC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.RegA.val>>self.Mem.adr[nn] # левый сдвиг
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=2
        elif cop==A_getf:      # получить флаги регистра А в регистр А
            self.RegA.val=0
            if self.RegA.FlagZ==1:
                self.RegA.val+=1
                self.RegA.FlagZ=0
            
            if self.RegA.FlagC==1:
                self.RegA.val+=2
            
            if self.RegA.FlagO==1:
                self.RegA.val+=4
            
            if self.RegA.FlagS==1:
                self.RegA.val+=8
            
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.PC.val+=1
        elif cop==A_setf:      # установить флаги регистра А из регистра А
            if self.RegA.val & 1:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            
            if self.RegA.val & 2:
                self.RegA.FlagC=1
            else:
                self.RegA.FlagC=0
            
            if self.RegA.val & 4:
                self.RegA.FlagO=1
            else:
                self.RegA.FlagO=0
            
            if self.RegA.val & 8:
                self.RegA.FlagS=1
            else:
                self.RegA.FlagS=0
            self.PC.val+=1
        elif cop==A_ifz:      # переход если "0"
            if self.RegA.FlagZ == 1:
                # переход, если регистр А равен нулю
                self.PC.val=self.Mem.adr[self.PC.val+1]
            else:
                self.PC.val+=2
        elif cop==A_ncmp:      # сравнить с числом
            self.PC.val+=1
            if self.RegA.val==self.Mem.adr[self.PC.val]:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.PC.val+=1
        elif cop==A_ifnz:      # переход если "0"
            if self.RegA.FlagZ <> 1:
                # переход, если регистр А равен нулю
                self.PC.val=self.Mem.adr[self.PC.val+1]
            else:
                self.PC.val+=2
        elif cop==A_mset:      # сохранить регистр А по адресу nn
            self.PC.val+=1
            # переход, если регистр А равен нулю
            self.Mem.adr[self.PC.val]=self.RegA.val
            self.PC.val+=1
        elif cop==A_push:      # сохранить регистр А в стеке
            self.Mem.adr[self.SP.val]=self.RegA.val
            self.SP.val-=1
            self.PC.val+=1
        elif cop==A_pop:      # восстановить регистр А из стека
            self.RegA.val=self.Mem.adr[self.SP.val]
            self.SP.val+=1
            self.PC.val+=1
        elif cop==A_call:      # вызвать процедуру по адресу в регистре А
            self.Mem.adr[self.SP.val]=self.RegA.val
            self.SP.val-=1
            self.PC.val=self.RegA.val
        elif cop==A_ret:      # возврат из процедуры
            self.PC.val=self.RegA.val
            self.SP.val+=1
        elif cop==A_in:      # чтение из порта
            self.PC.val+=1
            self.RegA.val=self.Port.adr[self.Mem.adr[self.PC.val]]
            self.PC.val+=1
