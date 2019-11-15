
# This file was *autogenerated* from the file grain.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_33 = Integer(33); _sage_const_25 = Integer(25); _sage_const_12 = Integer(12); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_19 = Integer(19); _sage_const_32 = Integer(32)
import sys
import numpy as np 
from sage.all import *
from random import *
import pdb

class Symbolic:
    def __init__(self,anfstuc):
        self.anfstuc = anfstuc        

    def SXOR(self,anfStuc1,anfStuc2):
        finalAnfStuc = [_sage_const_0 ,[]]

        for i in range(len(anfStuc1[_sage_const_1 ])):
            finalAnfStuc[_sage_const_1 ].append(anfStuc1[_sage_const_1 ][i])

        for i in range(len(anfStuc2[_sage_const_1 ])):
            finalAnfStuc[_sage_const_1 ].append(anfStuc2[_sage_const_1 ][i])
        
        finalAnfStuc[_sage_const_0 ]=(anfStuc1[_sage_const_0 ]+anfStuc2[_sage_const_0 ])%_sage_const_2 
        finalAnfStuctemp=[]
        
        for i in range(len(finalAnfStuc[_sage_const_1 ])):
            count = finalAnfStuc[_sage_const_1 ].count(finalAnfStuc[_sage_const_1 ][i])
            if(count%_sage_const_2 ==_sage_const_1 ):
                if finalAnfStuc[_sage_const_1 ][i] not in finalAnfStuctemp:
                    finalAnfStuctemp.append(finalAnfStuc[_sage_const_1 ][i])

        finalAnfStuc[_sage_const_1 ]=finalAnfStuctemp
        # self.Symbolic = finalAnfStuc
        x = Symbolic(finalAnfStuc)

        return x

    def SAND(self,anfStuc1,anfStuc2):
        finalAnfStuc = [_sage_const_0 ,[]]
        for i in range(len(anfStuc1[_sage_const_1 ])):
            for j in range(len(anfStuc2[_sage_const_1 ])):
                tempTerm = list(set().union(anfStuc1[_sage_const_1 ][i], anfStuc2[_sage_const_1 ][j]))
                finalAnfStuc[_sage_const_1 ].append(tempTerm)

        if anfStuc1[_sage_const_0 ] == _sage_const_1 :
            for i in anfStuc2[_sage_const_1 ]:
                finalAnfStuc[_sage_const_1 ].append(i)

        if anfStuc2[_sage_const_0 ] == _sage_const_1 :
            for i in anfStuc1[_sage_const_1 ]:
                finalAnfStuc[_sage_const_1 ].append(i)
        temp = []
        for i in range(len(finalAnfStuc[_sage_const_1 ])):
            count = finalAnfStuc[_sage_const_1 ].count(finalAnfStuc[_sage_const_1 ][i])
            if(count%_sage_const_2 ==_sage_const_1 ):
                if finalAnfStuc[_sage_const_1 ][i] not in temp:
                    temp.append(finalAnfStuc[_sage_const_1 ][i])
        finalAnfStuc[_sage_const_1 ] = temp
        finalAnfStuc[_sage_const_0 ] = (anfStuc1[_sage_const_0 ] * anfStuc2[_sage_const_0 ])%_sage_const_2 
        x = Symbolic(finalAnfStuc)
        return x

    def __mul__(self,a2):
        return self.SAND(self.anfstuc,a2.anfstuc)

    def __add__(self,a2):
        return self.SXOR(self.anfstuc,a2.anfstuc)

def FormEquations(IV,n):
    key = []
    z = []
    for i in range(_sage_const_32 ):
        key.append(Symbolic([_sage_const_0 ,[[i]]]))
    
    s = key
    b = IV

    for i in range(len(key) - len(IV)):
        b.append(Symbolic([_sage_const_1 ,[]]))

    for i in range(_sage_const_33 ):
        f1 = s[_sage_const_0 ] + s[_sage_const_4 ] + s[_sage_const_8 ] + s[_sage_const_12 ] + s[_sage_const_16 ] + s[_sage_const_20 ]
        
        g1 = s[_sage_const_0 ] + b[_sage_const_0 ] + b[_sage_const_5 ] + b[_sage_const_7 ] + b[_sage_const_10 ] + b[_sage_const_14 ] + b[_sage_const_17 ] + \
        b[_sage_const_19 ] + b[_sage_const_23 ] + b[_sage_const_26 ] + b[_sage_const_29 ]*b[_sage_const_31 ] + b[_sage_const_16 ]*b[_sage_const_19 ] + \
        b[_sage_const_5 ]*b[_sage_const_7 ] + b[_sage_const_29 ]*b[_sage_const_25 ]*b[_sage_const_22 ] + b[_sage_const_16 ]*b[_sage_const_14 ]*b[_sage_const_10 ] + \
        b[_sage_const_31 ]*b[_sage_const_23 ]*b[_sage_const_19 ]*b[_sage_const_4 ] + b[_sage_const_31 ]*b[_sage_const_25 ]*b[_sage_const_14 ]*b[_sage_const_5 ] + \
        b[_sage_const_29 ]*b[_sage_const_28 ]*b[_sage_const_19 ]*b[_sage_const_17 ] + b[_sage_const_31 ]*b[_sage_const_29 ]*b[_sage_const_10 ]*b[_sage_const_7 ] + \
        b[_sage_const_31 ]*b[_sage_const_29 ]*b[_sage_const_26 ]*b[_sage_const_23 ]*b[_sage_const_19 ] + b[_sage_const_17 ]*b[_sage_const_14 ]*b[_sage_const_10 ]*b[_sage_const_7 ]*b[_sage_const_5 ] + \
        b[_sage_const_26 ]*b[_sage_const_23 ]*b[_sage_const_19 ]*b[_sage_const_17 ]*b[_sage_const_14 ]*b[_sage_const_10 ]

        h1 = s[_sage_const_12 ] + b[_sage_const_31 ] + s[_sage_const_1 ]*s[_sage_const_31 ] + s[_sage_const_23 ]*s[_sage_const_31 ] + s[_sage_const_31 ]*b[_sage_const_31 ] + \
        s[_sage_const_1 ]*s[_sage_const_12 ]*s[_sage_const_23 ] + s[_sage_const_1 ]*s[_sage_const_23 ]*s[_sage_const_31 ] + \
        s[_sage_const_1 ]*s[_sage_const_23 ]*b[_sage_const_31 ] + s[_sage_const_12 ]*s[_sage_const_23 ]*b[_sage_const_31 ] + s[_sage_const_23 ]*s[_sage_const_31 ]*b[_sage_const_31 ]

        output = h1 + b[_sage_const_0 ] + b[_sage_const_1 ] + b[_sage_const_2 ] + b[_sage_const_6 ] + b[_sage_const_15 ] + b[_sage_const_21 ] + b[_sage_const_28 ]
        s[:_sage_const_31 ] = s[_sage_const_1 :]
        s[_sage_const_31 ] = f1
        b[:_sage_const_31 ] = b[_sage_const_1 :]
        b[_sage_const_31 ] = g1

        z.append(output.anfstuc)
        print(i)
    return z

def main():

    temp = [_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ,_sage_const_1 ,_sage_const_0 ]
    IV = []
    for i in range(_sage_const_8 ):
        IV.append(Symbolic([temp[i],[]]))
    
    a = FormEquations(IV,_sage_const_33 )
    print(a[_sage_const_0 ])
    print('\n')
    print(a[_sage_const_1 ])
    pdb.set_trace()
if __name__ == '__main__':
    main()

