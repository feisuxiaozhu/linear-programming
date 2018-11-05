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









