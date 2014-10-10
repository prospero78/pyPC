# -*- coding: utf8 -*-
'''
Класс регистра общего назначения.
По умолчанию класс имеет 8 бит (0...255) -- MAX_REG_VAL
'''
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
    A_vin =41
    A_jmp = 42

class clsReg:
    def __init__(self, root=None, mem=None, pc=None):
        self.root=root
        
        # ссылка на память
        self.Mem=mem
        
        # сылка на программный счётчик
        self.RegPC=pc
        
        # сбросить регистр в ноль и установить флаг нуля
        self.val=0
        self.FlagZ=1
        self.FlagO=0
        self.FlagC=0
        
    def command(self, cop=0):
        '''
            Вычисляет что за команда поступила на вход и
            далее обрабатывает её, в зависимости от кода
            --------------------
            cop - "код операции"
            -------------------
        '''
        if cop==A_rset:          # установка значения регистра А значением регистра А
            self.RegPC.val+=1           # выровнять укзатель команд на следующую команду
            # сбросить все флаги, кроме Zero и Signed
            self.FlagO=0
            self.FlagC=0
        elif cop==A_radd:        # установка регистра А со сложением содержимого регистра А
            self.val+=self.val
            if self.val>=self.max_val: # если в регистре перебор
                self.FlagO=1   # установить флаг перебора
                self.val=self.max_val-self.val
            self.RegPC.val+=1
            # установка необходимых флагов
            if self.val==0:
                self.FlagZ=1
            self.FlagC=0
            self.FlagS=0
        elif cop==A_rsub:        # установка регистра А с вычитанием содержимого регистра А
            self.val=0
            self.FlagZ=1
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_rinc:        # установка регистра А с инкрементом содержимого регистра А
            self.val+=1
            if self.val>=self.max_val: # если в регистре перебор
                self.FlagO=1   # установить флаг перебора
                self.val=self.max_val-self.val
            if self.val==0:
                self.FlagZ=1
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_rdec:        # установка регистра А с декрементом содержимого регистра А
            self.val-=1
            if self.val<0: # если в регистре недобор
                self.FlagC=1   # установить флаг заёма
                self.val=self.max_val+self.val
            if self.val==0:
                self.FlagZ=1
            self.FlagO=0
            self.RegPC.val+=1
        elif cop==A_rnot:      # инвертировать регистр А инверсным значением регистра А
            self.val=~self.val
            if self.val==0:
                self.FlagZ=1
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_rxor:      # поксорить регистр А значением регистра А
            self.val=0
            self.FlagZ=1
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_ror:      # OR регистра А со значением регистра А
            self.RegPC.val+=1
        elif cop==A_rand:      # AND регистра А со значением регистра А
            self.RegPC.val+=1
        elif cop==A_rshr:      # сдвиг вправо регистра А со значением регистра А
            self.val>>=1
            if self.val==0:
                self.FlagZ=1
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_rshl:      # сдвиг влево регистра А со значением регистра А
            self.val<<=1
            if self.val==0:
                self.FlagZ=1
            if self.val>self.max_val: # превышено ли максимальное значение?
                self.FlagO=1
                self.val=self.val-self.max_val
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nset:      # установить регистр А значением числа n
            self.RegPC.val+=1
            self.val=self.Mem.adr[self.RegPC.val]
            if self.val==0:
                self.FlagZ=1
            self.FlagO=1
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nadd:        # установка регистра А со сложением содержимого числа n
            self.RegPC.val+=1
            self.val+=self.Mem.adr[self.RegPC.val]
            if self.val>=self.max_val: # если в регистре перебор
                self.FlagO=1   # установить флаг перебора
                self.val=self.max_val-self.val
            self.RegPC.val+=1
            # установка необходимых флагов
            if self.val==0:
                self.FlagZ=1
            self.FlagC=0
            self.FlagS=0
        elif cop==A_nsub:        # установка регистра А с вычитанием числа n
            self.RegPC.val+=1
            self.val=self.val-self.Mem.adr[self.RegPC.val]
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            if self.val<0:
                self.val=self.max_val+self.val
                self.FlagS=1
            else:
                self.FlagS=0
            self.FlagO=0
            self.FlagC=0
            self.RegPC.val+=1
        elif cop==A_nnot:      # инвертировать регистр А инверсным значением числа n
            self.RegPC.val+=1
            self.val=~self.Mem.adr[self.RegPC.val]
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nxor:      # поксорить регистр А значением n
            self.RegPC.val+=1
            self.val^=self.Mem.adr[self.RegPC.val]
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nor:      # OR регистра А со значением n
            self.RegPC.val+=1
            self.val|=self.Mem.adr[self.RegPC.val]
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nand:      # AND регистра А со значением n
            self.RegPC.val+=1
            self.val&=self.Mem.adr[self.RegPC.val]
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_mget:      # установка значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val=self.Mem.adr[nn] # присовить
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=2
        elif cop==A_madd:      # сложение значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val+=self.Mem.adr[nn] # сложить
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            if self.val>=self.max_val:
                self.val=self.val-self.max_val
                self.FlagO=1
            else:
                self.FlagO=0
            self.FlagC=0
            self.FlagS=0
            self.RegPC.val+=2
        elif cop==A_msub:      # вычитание значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val-=self.Mem.adr[nn] # сложить
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            if self.val<0:
                self.val=self.val*(-1)
                self.FlagC=1
                self.FlagS=1
            else:
                self.FlagC=0
                self.FlagS=0
            self.FlagO=0
            self.RegPC.val+=2
        elif cop==A_minc:      # увеличить на 1 значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val=self.Mem.adr[nn]+1 # сложить
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            if self.val>=self.max_val:
                self.val=self.val-self.max_val
                self.FlagO=1
            else:
                self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mdec:      # уменьшить на 1 значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val=self.Mem.adr[nn]-1 # вычесть
            if self.val==0:
                self.FlagZ=1
                self.FlagC=0
            else:
                self.FlagZ=0
            if self.val<=0:
                self.val=self.max_val
                self.FlagC=1
            else:
                self.FlagC=0
            self.FlagO=0
            self.FlagS=0
            self.RegPC.val+=2
        elif cop==A_mnot:      # инвертировать значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val=~self.Mem.adr[nn] # инвертировать
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mxor:      # исключающее ИЛИ значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val^=self.Mem.adr[nn] # исключающее ИЛИ
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mor:      # логическое И значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val|=self.Mem.adr[nn] # логическое ИЛИ
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mand:      # логическое И значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val&=self.Mem.adr[nn] # логическое ИЛИ
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mshr:      # правый сдвиг значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val=self.val>>(self.Mem.adr[nn]) # правый сдвиг
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mshl:      # получить флаги регистра А
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.val=self.val>>self.Mem.adr[nn] # левый сдвиг
            if self.val==0:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=2
        elif cop==A_getf:      # получить флаги регистра А в регистр А
            self.val=0
            if self.FlagZ==1:
                self.val+=1
                self.FlagZ=0
            
            if self.FlagC==1:
                self.val+=2
            
            if self.FlagO==1:
                self.val+=4
            
            if self.FlagS==1:
                self.val+=8
            
            self.FlagO=0
            self.FlagS=0
            self.FlagC=0
            self.RegPC.val+=1
        elif cop==A_setf:      # установить флаги регистра А из регистра А
            if self.val & 1:
                self.FlagZ=1
            else:
                self.FlagZ=0
            
            if self.val & 2:
                self.FlagC=1
            else:
                self.FlagC=0
            
            if self.val & 4:
                self.FlagO=1
            else:
                self.FlagO=0
            
            if self.val & 8:
                self.FlagS=1
            else:
                self.FlagS=0
            self.RegPC.val+=1
        elif cop==A_ifz:      # переход если "0"
            if self.FlagZ == 1:
                # переход, если регистр А равен нулю
                self.RegPC.val=self.Mem.adr[self.RegPC.val+1]
            else:
                self.RegPC.val+=2
        elif cop==A_ncmp:      # сравнить с числом
            self.RegPC.val+=1
            if self.val==self.Mem.adr[self.RegPC.val]:
                self.FlagZ=1
            else:
                self.FlagZ=0
            self.RegPC.val+=1
        elif cop==A_ifnz:      # переход если "0"
            if self.FlagZ <> 1:
                # переход, если регистр А равен нулю
                self.RegPC.val=self.Mem.adr[self.RegPC.val+1]
            else:
                self.RegPC.val+=2
        elif cop==A_mset:      # сохранить регистр А по адресу nn
            self.RegPC.val+=1
            # переход, если регистр А равен нулю
            self.Mem.adr[self.RegPC.val]=self.val
            self.RegPC.val+=1
        elif cop==A_push:      # сохранить регистр А в стеке
            self.Mem.adr[self.RegSP.val]=self.val
            self.RegSP.val-=1
            self.RegPC.val+=1
        elif cop==A_pop:      # восстановить регистр А из стека
            self.val=self.Mem.adr[self.RegSP.val]
            self.RegSP.val+=1
            self.RegPC.val+=1
        elif cop==A_call:      # вызвать процедуру по адресу в регистре А
            self.Mem.adr[self.RegSP.val]=self.val
            self.RegSP.val-=1
            self.RegPC.val=self.val
        elif cop==A_ret:      # возврат из процедуры
            self.RegPC.val=self.val
            self.RegSP.val+=1
        elif cop==A_in:      # чтение из порта
            self.RegPC.val+=1
            self.val=self.Port.adr[self.Mem.adr[self.RegPC.val]]
            self.RegPC.val+=1
        elif cop==A_out:      # запись в порт
            self.RegPC.val+=1
            self.Port.adr[self.Mem.adr[self.RegPC.val]]=self.val
            self.RegPC.val+=1
        #elif cop==A_vin:      # чтение из видеопорта
        #    self.RegPC.val+=1
        #    self.Port.adr[self.Mem.adr[self.RegPC.val]]=self.val
        #    self.RegPC.val+=1
        elif cop==A_jmp:      # запись в порт
            self.RegPC.val+=1
            self.RegPC.val=self.Mem.adr[self.RegPC.val]
