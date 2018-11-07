from numpy import *
from itertools import *
import math
import scipy.io

def findJump(x):
#find the index where jump happens. 0011->2,1001->3,1100->4,0110->1
    for i in range(len(x)):
        prev = int(x[i])
        if i == len(x)-1:
            cur = int(x[0])
        else:
            cur = int(x[i+1])
        if prev == 0 and cur == 1:
            return i+1

def findCyclic(x):
# find all cyclic permutations of input
# input: 0011, output: [0011,1001,1100,0110]
    res = []
    n = len(x)
    lists = [[x[i - j] for i in range(n)] for j in range(n)]
    for a in lists:
        temp = ''.join(a)
        res.append(temp)
    return res


def generatePureInputs(N): #we require N to be a multiple of 4
    if N%4 != 0:
        print("N is not a multiple of 4")
        return False
    res = []
    length = int(N/2)
    tail = "1" * length
    head = "0" * length
    temp = head+tail
    temp = findCyclic(temp)
    for item in temp:
        res.append(item)
    return res

def generateF(N):
    inputs = generatePureInputs(N)
    length = len(inputs)
    f = zeros(2*length)
    i = 0
    for x in inputs:
        index = findJump(x)
        f[2*i] = pow(-1, index)
        f[2*i+1] = pow(-1, index) * (-1)
        i += 1
    f = -f
    return f

def generatelb(N):
    lb = zeros(2*N)
    return lb

def generateA(N):
    A = ones(2*N)
    return A

def generateb():
    return 1.

def AeqRowHelper(degree, N):
    if degree == 0:
        temp = []
        res = zeros(2*N)
        for i in range(len(res)):
            if i%2 == 0:
                res[i] = 1
            else:
                res[i] = -1
        temp.append(res)
        return temp
    s = list(range(N))
    powerS = list(combinations(s, degree))
    res = []
    inputs = generatePureInputs(N)
    print(inputs)
    for xIndices in powerS:
        temp = zeros(2*N)
        for i in range(N):
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

def generateBeq(Aeq):
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
beq = generateBeq(Aeq)



scipy.io.savemat('./pureCyclic.mat', mdict={'f': f, 'A':A, 'b':b, 'lb':lb, 'Aeq':Aeq,'beq':beq})






