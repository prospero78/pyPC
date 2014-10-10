# -*- coding: utf8 -*-
'''
Класс центрального процессора.
'''
from pakReg.modReg import clsReg
from pakMem.modMemory import clsMemory

# константы для кодов операций
if True:
    A_rset=0
    A_radd=1
    A_rsub=2
    A_rinc=3
    A_rdec=4
    A_rnot=5
    A_rxor=6
    A_ror =7
    A_rand=8
    A_rshr=9
    A_rshl=10
    #----------------------
    A_nset=11
    A_nadd=12
    A_nsub=13
    A_nnot=14
    A_nxor=15
    A_nor =16
    A_nand=17
    #---------------------
    A_mget=18
    A_madd=19
    A_msub=20
    A_minc=21
    A_mdec=22
    A_mnot=23
    A_mxor=24
    A_mor =25
    A_mand=26
    A_mshr=27
    A_mshl=28
    #-----------------
    A_getf =29
    A_setf =30
    #---------------
    A_ifz =31
    A_ncmp=32
    A_ifnz=33
    A_mset=34
    A_push=35
    A_pop =36
    A_call=37
    A_ret =38
    A_in  =39
    A_out =40
    A_vin =40
    
class clsCPU:
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
    
    def __init__(self, root=None):
        self.root=root
        
        self.max_val=self.root.Res.max_reg_val
       
        self.Mem=clsMemory(root=self.root)
        
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
        
    def run(self):
        pass
    
    def step(self):
        self.detect()
        
    def detect(self):
        '''
        Процедурка занимается детектированием поступивших команд.
        '''
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
        elif cop==A_out:      # запись в порт
            self.PC.val+=1
            self.Port.adr[self.Mem.adr[self.PC.val]]=self.RegA.val
            self.PC.val+=1
        #elif cop==A_vin:      # чтение из видеопорта
        #    self.PC.val+=1
        #    self.Port.adr[self.Mem.adr[self.PC.val]]=self.RegA.val
        #    self.PC.val+=1
