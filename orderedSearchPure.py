from numpy import *
from itertools import *
import math
import scipy.io

def findLeadingZero(x): #find the number of leading zeros if x is pure form
    counter=0
    for i in range(len(x)):
        if x[i] != '1':
            counter+=1
        else:
            break
    return counter

def generatePureInputs(N):
# return all pure inputs of length N. If N = 3, return [001,011]
    res=[]
    for i in range(1,N):
        tail = "1" * i
        head = "0" * (N-i)
        temp = head+tail
        res.append(temp)
    return res

def generateF(N):
    inputs = generatePureInputs(N)
    length = len(inputs)
    f = zeros(2*length)
    i = 0
    for x in inputs:
        index = findLeadingZero(x)
        f[2*i] = pow(-1, index)
        f[2*i+1] = pow(-1, index) * (-1)
        i += 1
    f = -f
    return f

def generatelb(N):
    lb = zeros(2*(N-1))
    return lb

def generateA(N):
    A = ones(2*(N-1))
    return A

def generateb():
    return 1.

def AeqRowHelper(degree, N):
    if degree == 0:
        temp = []
        res = zeros(2*(N-1))
        for i in range(len(res)):
            if i%2 == 0:
                res[i] = 1
            else:
                res[i] = -1
        temp.append(res)
        return temp
    s = list(range(N))
    powerS = list(combinations(s, degree))
    print(powerS)
    res = []
    inputs = generatePureInputs(N)
    for xIndices in powerS:
        temp = zeros(2*(N-1))
        for i in range(N-1):
            x=inputs[i]
            temp[2*i] = 1
            temp[2*i+1] = -1
            for xIndex in xIndices:
                bit = int(x[xIndex])
                temp[2*i] *= -1*pow(-1,bit)
                temp[2*i+1] *= -1*pow(-1,bit)
        res.append(temp)
    return res

def generateAeq(d,N):
    res = []
    for degree in range(d+1):
        temp = AeqRowHelper(degree, N)
        for row in temp:
            res.append(row)
    return res

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def generateBeq(d,N):
    temp=[]
    res = 1
    for i in range(1,d+1):
        res += nCr(N,i)
    res = int(res)
    for j in range(res):
        temp.append(0.)
    return temp

def generateBeqV2(Aeq):
    temp = []
    for i in range(len(Aeq)):
        temp.append(0.)
    return temp

N=4
d=1

f = generateF(N)
A = generateA(N)
b = generateb()
lb = generatelb(N)
Aeq = generateAeq(d,N)
beq = generateBeqV2(Aeq)
scipy.io.savemat('./pure.mat', mdict={'f': f, 'A':A, 'b':b, 'lb':lb, 'Aeq':Aeq,'beq':beq})














