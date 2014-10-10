# -*- coding: utf8 -*-
'''
модуль определяет БИОС виртуальной машины.
'''
class clsBios:
    def __init__(self, root=None):
        self.root=root
        self.data={
            0:0, # A.rset(10)
            1:10, # n=10
            2:1,  # A_radd(1)
            3:1,  # n=1
            4:42, # A_jmp(0)
            5:0,  # m=0
            }
