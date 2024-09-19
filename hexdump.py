# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:11:11 2024

@author: CJCU-CC
"""
def hexdump(file,num):
    from math import ceil
    f = open(file,'rb')
    h = f.read(num)
    h1 = [hex(c)[2:].zfill(2) for c in h]
    h12 = h1 + (-len(h1)%16)*['  ']
    asc = ['.']*num
    
    for i in range(num):
        ii = int(h1[i],16)
        if ii>=32 and ii<=126:
            asc[i] = chr(ii)
    
    asc = asc + (-len(h1)%16)*[' ']
    for n in range(int(ceil(num/16.0))):
        print(hex(n*16)[2:].zfill(6)+': ',
              ' '.join([h12[16*n+2*i]+h12[16*n+2*i+1] for i in range(8)]),
              ' |'+''.join([asc[16*n+i] for i in range(16)])+'|')
