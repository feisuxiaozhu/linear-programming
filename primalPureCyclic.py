# this script generates matrix to solve primal solution of degree N
# i.e. N = 4, d = 2, f(x) = a*x1x2+*bx1x3+cx1x4+dx2x3+ex2x3+fx3x4
# primal world we have f(0011)=1, f(1001)=-1, f(1100)=1, f(0110)=-1.
# hence 0+0+0+d+0+0 = -1, 0+0+0+0+0+f=1, 0+0+c+0+0+0=-1, a+0+0+0+0+0=1 => a=1,c=-1,d=-1, f=1
# the goal is to generate matrix A=(000100,000001,001000,100000), b=(-1,1,-1,1) s.t. Ax=b. Matlab will solve for x
