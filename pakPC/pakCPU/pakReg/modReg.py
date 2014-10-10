# -*- coding: utf8 -*-
'''
Класс регистра общего назначения.
По умолчанию класс имеет 8 бит (0...255) -- MAX_REG_VAL
'''

class clsReg:
    def __init__(self, root=None, mem=None, pc=None):
        self.root=root
        
        # ссылка на память
        self.Mem=mem
        
        # сылка на программный счётчик
        self.PC=pc
        
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
        cop=self.Mem.adr[self.RegPC.val]     # получить текущую команду из памяти
        # сначала вычислить регистр
        reg=(cop & REG_MASK)>>8
        #if reg<REG_A or reg>=NOT_REG:
        #    print 'ERROR! In', self.RegPC.val, 'invalid reg! reg=', reg
        #    return 1
        # если это всё-таки регистр -- продолжить детектирование
        if cop==A_rset:          # установка значения регистра А значением регистра А
            self.RegPC.val+=1           # выровнять укзатель команд на следующую команду
            # сбросить все флаги, кроме Zero и Signed
            self.RegA.FlagO=0
            self.RegA.FlagC=0
        elif cop==A_radd:        # установка регистра А со сложением содержимого регистра А
            self.RegA.val+=self.RegA.val
            if self.RegA.val>=self.max_val: # если в регистре перебор
                self.RegA.FlagO=1   # установить флаг перебора
                self.RegA.val=self.max_val-self.RegA.val
            self.RegPC.val+=1
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
            self.RegPC.val+=1
        elif cop==A_rinc:        # установка регистра А с инкрементом содержимого регистра А
            self.RegA.val+=1
            if self.RegA.val>=self.max_val: # если в регистре перебор
                self.RegA.FlagO=1   # установить флаг перебора
                self.RegA.val=self.max_val-self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_rdec:        # установка регистра А с декрементом содержимого регистра А
            self.RegA.val-=1
            if self.RegA.val<0: # если в регистре недобор
                self.RegA.FlagC=1   # установить флаг заёма
                self.RegA.val=self.max_val+self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegPC.val+=1
        elif cop==A_rnot:      # инвертировать регистр А инверсным значением регистра А
            self.RegA.val=~self.RegA.val
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_rxor:      # поксорить регистр А значением регистра А
            self.RegA.val=0
            self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_ror:      # OR регистра А со значением регистра А
            self.RegPC.val+=1
        elif cop==A_rand:      # AND регистра А со значением регистра А
            self.RegPC.val+=1
        elif cop==A_rshr:      # сдвиг вправо регистра А со значением регистра А
            self.RegA.val>>=1
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_rshl:      # сдвиг влево регистра А со значением регистра А
            self.RegA.val<<=1
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            if self.RegA.val>self.max_val: # превышено ли максимальное значение?
                self.RegA.FlagO=1
                self.RegA.val=self.RegA.val-self.max_val
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nset:      # установить регистр А значением числа n
            self.RegPC.val+=1
            self.RegA.val=self.Mem.adr[self.RegPC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagO=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nadd:        # установка регистра А со сложением содержимого числа n
            self.RegPC.val+=1
            self.RegA.val+=self.Mem.adr[self.RegPC.val]
            if self.RegA.val>=self.max_val: # если в регистре перебор
                self.RegA.FlagO=1   # установить флаг перебора
                self.RegA.val=self.max_val-self.RegA.val
            self.RegPC.val+=1
            # установка необходимых флагов
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            self.RegA.FlagC=0
            self.RegA.FlagS=0
        elif cop==A_nsub:        # установка регистра А с вычитанием числа n
            self.RegPC.val+=1
            self.RegA.val=self.RegA.val-self.Mem.adr[self.RegPC.val]
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
            self.RegPC.val+=1
        elif cop==A_nnot:      # инвертировать регистр А инверсным значением числа n
            self.RegPC.val+=1
            self.RegA.val=~self.Mem.adr[self.RegPC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nxor:      # поксорить регистр А значением n
            self.RegPC.val+=1
            self.RegA.val^=self.Mem.adr[self.RegPC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nor:      # OR регистра А со значением n
            self.RegPC.val+=1
            self.RegA.val|=self.Mem.adr[self.RegPC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_nand:      # AND регистра А со значением n
            self.RegPC.val+=1
            self.RegA.val&=self.Mem.adr[self.RegPC.val]
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=1
        elif cop==A_mget:      # установка значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.Mem.adr[nn] # присовить
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagC=0
            self.RegA.FlagS=0
            self.RegPC.val+=2
        elif cop==A_madd:      # сложение значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
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
            self.RegPC.val+=2
        elif cop==A_msub:      # вычитание значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
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
            self.RegPC.val+=2
        elif cop==A_minc:      # увеличить на 1 значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
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
            self.RegPC.val+=2
        elif cop==A_mdec:      # уменьшить на 1 значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
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
            self.RegPC.val+=2
        elif cop==A_mnot:      # инвертировать значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=~self.Mem.adr[nn] # инвертировать
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mxor:      # исключающее ИЛИ значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val^=self.Mem.adr[nn] # исключающее ИЛИ
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mor:      # логическое И значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val|=self.Mem.adr[nn] # логическое ИЛИ
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mand:      # логическое И значение регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val&=self.Mem.adr[nn] # логическое ИЛИ
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mshr:      # правый сдвиг значения регистра А из ячейки с адресом nn
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.RegA.val>>(self.Mem.adr[nn]) # правый сдвиг
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.RegPC.val+=2
        elif cop==A_mshl:      # получить флаги регистра А
            nn=self.Mem.adr[self.RegPC.val+1] # получить адрес nn, в котором лежит число
            self.RegA.val=self.RegA.val>>self.Mem.adr[nn] # левый сдвиг
            if self.RegA.val==0:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegA.FlagO=0
            self.RegA.FlagS=0
            self.RegA.FlagC=0
            self.RegPC.val+=2
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
            self.RegPC.val+=1
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
            self.RegPC.val+=1
        elif cop==A_ifz:      # переход если "0"
            if self.RegA.FlagZ == 1:
                # переход, если регистр А равен нулю
                self.RegPC.val=self.Mem.adr[self.RegPC.val+1]
            else:
                self.RegPC.val+=2
        elif cop==A_ncmp:      # сравнить с числом
            self.RegPC.val+=1
            if self.RegA.val==self.Mem.adr[self.RegPC.val]:
                self.RegA.FlagZ=1
            else:
                self.RegA.FlagZ=0
            self.RegPC.val+=1
        elif cop==A_ifnz:      # переход если "0"
            if self.RegA.FlagZ <> 1:
                # переход, если регистр А равен нулю
                self.RegPC.val=self.Mem.adr[self.RegPC.val+1]
            else:
                self.RegPC.val+=2
        elif cop==A_mset:      # сохранить регистр А по адресу nn
            self.RegPC.val+=1
            # переход, если регистр А равен нулю
            self.Mem.adr[self.RegPC.val]=self.RegA.val
            self.RegPC.val+=1
        elif cop==A_push:      # сохранить регистр А в стеке
            self.Mem.adr[self.SP.val]=self.RegA.val
            self.SP.val-=1
            self.RegPC.val+=1
        elif cop==A_pop:      # восстановить регистр А из стека
            self.RegA.val=self.Mem.adr[self.SP.val]
            self.SP.val+=1
            self.RegPC.val+=1
        elif cop==A_call:      # вызвать процедуру по адресу в регистре А
            self.Mem.adr[self.SP.val]=self.RegA.val
            self.SP.val-=1
            self.RegPC.val=self.RegA.val
        elif cop==A_ret:      # возврат из процедуры
            self.RegPC.val=self.RegA.val
            self.SP.val+=1
        elif cop==A_in:      # чтение из порта
            self.RegPC.val+=1
            self.RegA.val=self.Port.adr[self.Mem.adr[self.RegPC.val]]
            self.RegPC.val+=1
        elif cop==A_out:      # запись в порт
            self.RegPC.val+=1
            self.Port.adr[self.Mem.adr[self.RegPC.val]]=self.RegA.val
            self.RegPC.val+=1
        #elif cop==A_vin:      # чтение из видеопорта
        #    self.RegPC.val+=1
        #    self.Port.adr[self.Mem.adr[self.RegPC.val]]=self.RegA.val
        #    self.RegPC.val+=1
