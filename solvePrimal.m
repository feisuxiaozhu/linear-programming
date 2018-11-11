clear
load('primalPureCyclic.mat')
x=linsolve(Aeq,beq')
save('primalSolution.mat','x')
