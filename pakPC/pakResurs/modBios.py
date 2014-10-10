# -*- coding: utf8 -*-
'''
модуль определяет БИОС виртуальной машины.

    A_rset=0        A_radd=1        A_rsub=2        A_rinc=3
    A_rdec=4        A_rnot=5        A_rxor=6        A_ror =7
    A_rand=8        A_rshr=9        A_rshl=10       A_nset=11
    A_nadd=12       A_nsub=13       A_nnot=14       A_nxor=15
    A_nor =16       A_nand=17       A_mget=18       A_madd=19
    A_msub=20       A_minc=21       A_mdec=22       A_mnot=23
    A_mxor=24       A_mor =25       A_mand=26       A_mshr=27
    A_mshl=28       A_getf =29      A_setf =30      A_ifz =31
    A_ncmp=32       A_ifnz=33       A_mset=34       A_push=35
    A_pop =36       A_call=37       A_ret =38       A_in  =39
    A_out =40       A_vin =41       A_jmp = 42
'''

class clsBios:
    def __init__(self, root=None):
        self.root=root
        self.data={
            0:11, # A.nset(10)
            1:10, # n=10
            2:1,  # A_radd(1)
            3:1,  # n=1
            4:42, # A_jmp(0)
            5:0,  # m=0
            }
