from numpy import *

#The goal is to generate f, A, b, A_eq, b_eq as input for matlab LP solver.

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

    f = -f #matlab only do minimum, so we invert the sign of f to get maximum
    return f


N=2
print(generateF(N))