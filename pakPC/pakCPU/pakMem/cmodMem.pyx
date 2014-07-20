# -*- coding: utf8 -*-
'''
Главный класс памяти. Все операции с памятью проходят через него.
'''

cdef class clsMem:
    cdef readonly unsigned  char mem[0xFFFF]
    cdef readonly int max_adr
    cdef readonly int max_val
    def __init__(self, root=None, bios=[], int max_adr=0xFFFF, int max_val=0xFF):
        self.root=root
        self.max_adr=max_adr
        self.max_val=max_val
        cdef int i
        for i in xrange(0, len(bios)):
            #self.mem[i]=bios[i]
            self.set(adr=i, val=bios[i])
            
    cpdef int get(self, int adr=0):
        return self.mem[adr]
    
    cpdef int set(self, int adr=0, int val=0):
        if adr<0:
            print 'cmodMem.set(): ERROR -- adr<0!'
            return 1
        elif adr>self.max_adr:
            print 'cmodMem.set(): ERROR -- adr>MAX_ADR!'
            return 2
        elif val<0:
            print 'cmodMem.set(): ERROR -- val<0!'
            return 3
        elif val>self.max_val:
            print 'cmodMem.set(): ERROR -- val>MAX_VAL!'
            return 1
        else:
            self.mem[adr]=val
            return 0
