import scipy.io
from numpy import *
from itertools import *

# we want to take the solution of primal from Matlab and output the nonzero indices and their value
name = "primalSolution.mat"
mat = scipy.io.loadmat(name)
x = mat['x']
N = 100
degree = 2
res={}

s = list(range(N))
powerS = list(combinations(s,degree))
epsilon = 0.001
for i in range(len(powerS)):
    value = x[i]
    if abs(value - 0) > epsilon:
        res[powerS[i]] = value[0]
temp=""
for key, value in res.items():
    i,j= key
    newkey = (i+1,j+1)
    value = float("%0.3f" % (value))
    temp += str(newkey) + ":" + str(value) + ","

print(temp)
