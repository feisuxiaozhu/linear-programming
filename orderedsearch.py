from numpy import *
from itertools import *
#The goal is to generate f, A, b, A_eq, b_eq, lb as input for matlab LP solver.

def validateX(x,N): #find if x is of pure form 00000001111111
    #corner cases:
    length = '{0:0' + str(N) + 'b}'
    if x== length.format(0):
        return False
    if x == length.format(pow(2,N)-1):
        return False

    sawOne = False
    for i in range(len(x)):
        if x[i]== '1':
            sawOne = True
        if x[i]=='0' and sawOne:
            return False
    return True

def findLeadingZero(x): #find the number of leading zeros if x is pure form
    counter=0
    for i in range(len(x)):
        if x[i] != '1':
            counter+=1
        else:
            break
    return counter

def generateF(N):
    #find the indices of f in our linear program
    f = zeros(2*pow(2,N))
    for i in range(pow(2,N)):
        length = '{0:0'+str(N)+'b}'
        x = str(length.format(i))
        #print(x)
        if validateX(x,N):
            index = findLeadingZero(x)
            f[2*i] = pow(-1, index)
            f[2*i+1] = pow(-1, index) * (-1)
        else:
            f[2*i] = -1
            f[2*i+1] = -1

    f = -f #matlab only does minimum, so we invert the sign of f to get maximum
    return f


#i.e. for all x, w_p(x)>=0 and w_n(x)>=0. The lb specify that lb<= w_p and lb<= w_n
def generatelb(N):
    lb=zeros(2*pow(2,N))
    return lb

#this function specifies the constraint Ax<=b, in our case the l-1 norm <=1
def generateA(N):
    A = zeros(2*pow(2,N))
    for i in range(len(A)):
        A[i] = 1
    return A
def generateb():
    b = zeros(1)
    b[0] = 1
    return b

#here we require A_eq*x = b_eq = 0, for low degree correspondence.
#generate sub matrix rows corresponding to rows in A for chi with degree d
#we will combine all these sub matrices for A_eq
def AeqRowHelper(degree,N):
    if degree == 0:
        res = zeros(2*pow(2,N))
        for i in range(len(res)):
            if i%2 == 0:
                res[i]=1
            else:
                res[i]=-1
        return res
    s = list(range(N))
    powerS = list(combinations(s,degree)) #generate all possible subset of s, where each element has length = degree
    for i in powerS:
        for j in i:
            print(j)
    return powerS


N=2
d=1

AeqRowHelper(1,N)
