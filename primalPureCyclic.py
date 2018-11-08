from numpy import *
from itertools import *
import math
import scipy.io

# this script generates matrix to solve primal solution of degree N
# i.e. N = 4, d = 2, f(x) = a*x1x2+*bx1x3+cx1x4+dx2x3+ex2x3+fx3x4
# primal world we have f(0011)=1, f(1001)=-1, f(1100)=1, f(0110)=-1.
# hence 0+0+0+d+0+0 = -1, 0+0+0+0+0+f=1, 0+0+c+0+0+0=-1, a+0+0+0+0+0=1 => a=1,c=-1,d=-1, f=1
# the goal is to generate matrix A=(000100,000001,001000,100000), b=(-1,1,-1,1) s.t. Ax=b. Matlab will solve for x

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

def generateAeq(degree,N):
    inputs = generatePureInputs(N)
    s = list(range(N))
    powerS = list(combinations(s,degree))
    #print(inputs)
    #print(powerS)
    res=[]
    for input in inputs:
        temp = ones(len(powerS))
        for i in range(len(powerS)):
            xIndices = powerS[i]
            for xIndex in xIndices:
                bit = int(input[xIndex])
                temp[i] *= -1*pow(-1,bit)
        res.append(temp)
    return res

def generateBeq(N):
    inputs = generatePureInputs(N)
    res = zeros(N)
    for i in range(len(res)):
        jump = findJump((inputs[i]))
        res[i] = pow(-1,jump)
    return res

N=100
degree = 2

Aeq = generateAeq(degree, N)
beq = generateBeq(N)

scipy.io.savemat('./primalPureCyclic.mat', mdict={'Aeq':Aeq,'beq':beq})
