# -*- coding: utf8 -*-
'''
модуль определяет БИОС виртуальной машины.

    A.rset(A)=0     A.radd(A)=1     A.rsub(A)=2     A.rinc()=3
    A.rdec()=4      A.rnot(A)=5     A.rxor(A)=6     A.ror(A)=7
    A_rand=8        A_rshr=9        A_rshl=10       A.nset(n)=11
    A.nadd(n)=12    A_nsub=13       A_nnot=14       A_nxor=15
    A_nor =16       A_nand=17       A_mget=18       A_madd=19
    A_msub=20       A_minc=21       A_mdec=22       A_mnot=23
    A_mxor=24       A_mor =25       A_mand=26       A_mshr=27
    A_mshl=28       A_getf =29      A_setf =30      A_ifz =31
    A_ncmp=32       A_ifnz=33       A_mset=34       A_push=35
    A_pop =36       A_call=37       A_ret =38       A.in(p)=39
    A_out =40       A_vin =41       A.jmp(m)=42
'''

bios={
    0:11, # A.nset(10)
    1:10, # n=10
    2:12, # A.nadd(1)
    3:1,  # n=1
    4:12, # A.nadd(5)
    5:5,  # n=5
    6:12, # A.nadd(8)
    7:8,  # n=8
    8:2,  # A.rsub()
    9:42, # A.jmp()
    10:0, # m=0
    11:0, #
    12:42, #A.jmp(11)
    13:11, #
    14:0, #
    15:0, #
    16:0, #
}
