import sys
import numpy as np 
from sage.all import *
from random import *
import pdb

class Symbolic:
    def __init__(self,anfstuc):
        self.anfstuc = anfstuc        

    def SXOR(self,anfStuc1,anfStuc2):
        finalAnfStuc = [0,[]]

        for i in range(len(anfStuc1[1])):
            finalAnfStuc[1].append(anfStuc1[1][i])

        for i in range(len(anfStuc2[1])):
            finalAnfStuc[1].append(anfStuc2[1][i])
        
        finalAnfStuc[0]=(anfStuc1[0]+anfStuc2[0])%2
        finalAnfStuctemp=[]
        
        for i in range(len(finalAnfStuc[1])):
            count = finalAnfStuc[1].count(finalAnfStuc[1][i])
            if(count%2==1):
                if finalAnfStuc[1][i] not in finalAnfStuctemp:
                    finalAnfStuctemp.append(finalAnfStuc[1][i])

        finalAnfStuc[1]=finalAnfStuctemp
        # self.Symbolic = finalAnfStuc
        x = Symbolic(finalAnfStuc)

        return x

    def SAND(self,anfStuc1,anfStuc2):
        finalAnfStuc = [0,[]]
        for i in range(len(anfStuc1[1])):
            for j in range(len(anfStuc2[1])):
                tempTerm = list(set().union(anfStuc1[1][i], anfStuc2[1][j]))
                finalAnfStuc[1].append(tempTerm)

        if anfStuc1[0] == 1:
            for i in anfStuc2[1]:
                finalAnfStuc[1].append(i)

        if anfStuc2[0] == 1:
            for i in anfStuc1[1]:
                finalAnfStuc[1].append(i)
        temp = []
        for i in range(len(finalAnfStuc[1])):
            count = finalAnfStuc[1].count(finalAnfStuc[1][i])
            if(count%2==1):
                if finalAnfStuc[1][i] not in temp:
                    temp.append(finalAnfStuc[1][i])
        finalAnfStuc[1] = temp
        finalAnfStuc[0] = (anfStuc1[0] * anfStuc2[0])%2
        x = Symbolic(finalAnfStuc)
        return x

    def __mul__(self,a2):
        return self.SAND(self.anfstuc,a2.anfstuc)

    def __add__(self,a2):
        return self.SXOR(self.anfstuc,a2.anfstuc)

def FormEquations(IV,n):
    key = []
    z = []
    for i in range(32):
        key.append(Symbolic([0,[[i]]]))
    
    s = key
    b = IV

    for i in range(len(key) - len(IV)):
        b.append(Symbolic([1,[]]))

    for i in range(33):
        f1 = s[0] + s[4] + s[8] + s[12] + s[16] + s[20]
        
        g1 = s[0] + b[0] + b[5] + b[7] + b[10] + b[14] + b[17] + \
        b[19] + b[23] + b[26] + b[29]*b[31] + b[16]*b[19] + \
        b[5]*b[7] + b[29]*b[25]*b[22] + b[16]*b[14]*b[10] + \
        b[31]*b[23]*b[19]*b[4] + b[31]*b[25]*b[14]*b[5] + \
        b[29]*b[28]*b[19]*b[17] + b[31]*b[29]*b[10]*b[7] + \
        b[31]*b[29]*b[26]*b[23]*b[19] + b[17]*b[14]*b[10]*b[7]*b[5] + \
        b[26]*b[23]*b[19]*b[17]*b[14]*b[10]

        h1 = s[12] + b[31] + s[1]*s[31] + s[23]*s[31] + s[31]*b[31] + \
        s[1]*s[12]*s[23] + s[1]*s[23]*s[31] + \
        s[1]*s[23]*b[31] + s[12]*s[23]*b[31] + s[23]*s[31]*b[31]

        output = h1 + b[0] + b[1] + b[2] + b[6] + b[15] + b[21] + b[28]
        s[:31] = s[1:]
        s[31] = f1
        b[:31] = b[1:]
        b[31] = g1

        z.append(output.anfstuc)
        print(i)
    return z

def main():

    temp = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
    IV = []
    for i in range(8):
        IV.append(Symbolic([temp[i],[]]))
    
    a = FormEquations(IV,33)
    print(a[0])
    print('\n')
    print(a[1])
    pdb.set_trace()
if __name__ == '__main__':
    main()