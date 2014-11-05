# -*- coding: utf8 -*-
"""
модуль определяет БИОС виртуальной машины.

    A.rset(A)=0     A.radd(A)=1     A.rsub(A)=2     A.rinc()=3
    A.rdec()=4      A.rnot(A)=5     A.rxor(A)=6     A.ror(A)=7
    A_RAND=8        A_RSHR=9        A_RSHL=10       A.nset(n)=11
    A.nadd(n)=12    A_NSUB=13       A_NNOT=14       A_NXOR=15
    A.nor =16       A_NAND=17       A_MGET=18       A_MADD=19
    A.msub=20       A_MINC=21       A_MDEC=22       A_MNOT=23
    A_MXOR=24       A_MOR =25       A_MAND=26       A_MSHR=27
    A_MSHL=28       A_GETF =29      A_SETF =30      A_IFZ =31
    A_NCMP=32       A_IFNZ=33       A_MSET=34       A.push()=35
    A_POP =36       A.call(m)=37    A.ret() =38     A.in(p)=39
    A.out(p)=40     A_VIN =41       A.jmp(m)=42

При старте системы происходит обход начальных процедур путём прыжка за них.

Список процедур БИОСа:
SET_VIDEO_MODE -- установка режима экрана
    adr=2
    reg_a=1

"""

__version__ = 5

ADR_SET_VIDEO_MODE = 2  # устанавливает видео-режим
ADR_CLEAR_SCREEN = 5  # адрес очитски экрана
ADR_FILL_SCREEN = 12  # адрес заливки экрана

BIOS = {
    0: 42, 1: 50,  # A.jmp(50) # обход начальных процедур.

    # --- SET_VIDEO_MODE  START ---
    2: 40, 3: 1,  # A.out(1) -- запись в порт один режима видеокарты
    4: 38,  # A.ret()
    # --- SET_VIDEO_MODE  END ---

    # --- CLEAR_SCREEN  START ---
    5: 35,  # A.push() # сохранить регистр в стеке
    6: 11, 7: 1,  # A.nset(1) # команда 1 -- очистка экрана
    8: 40, 9: 2,  # A.out(2) # записать в порт видеокарты команду
    10: 36,  # A.pop() # восстановить регистр со стека
    11: 38,  # A.ret()
    # --- CLEAR_SCREEN  END ---

    # --- FILL_SCREEN  START ---
    12: 35,  # A.push() # сохранить регистр в стеке
    13: 40, 14: 3,  # A.out(3) # записать в порт видеокарты команду
    15: 36,  # A.pop() # восстановить регистр со стека
    16: 38,  #  A.ret()
    # --- FILL_SCREEN  END ---


    17: 0,
    18: 0,
    19: 0,  #
    20: 0,  #
    21: 0,  #
    22: 0,  #
    23: 0,  #
    24: 0,  #
    25: 0,  #
    26: 0,  #
    27: 0,  #
    28: 0,  #
    29: 0,  #
    30: 0,  #
    31: 0,  #
    32: 0,  #
    33: 0,  #
    34: 0,  #
    35: 0,  #
    36: 0,  #
    37: 0,  #
    38: 0,  #
    39: 0,  #
    40: 0,  #
    41: 0,  #
    42: 0,  #
    43: 0,  #
    44: 0,  #
    45: 0,  #
    46: 0,  #
    47: 0,  #
    48: 0,  #
    49: 0,  #

    50: 11, 51: 1,  # A.nset(1) -- инициализация режима видеокарты
    52: 37, 53: ADR_SET_VIDEO_MODE,  # A.call(ADR_SET_VIDEO_MODE)

    54: 37, 55: ADR_CLEAR_SCREEN,  # A.call(ADR_CLEAR_SCREEN)

    56: 11, 57: 35,  # A.nset(35) # заливка экрана символом "#"
    58: 37, 59: ADR_FILL_SCREEN,  # A.call(ADR_FILL_SCREEN)
    60: 0,  #
}
