#Code for Experiment 1
#I19PH004 Keith Kamson Fernandes
#Question 1 - False-Position Method (Regula-Falsi Method)

#Formula & Method
#y1 = x1 - f(x1)*[(x1-x0)/{f(x1)-f(x0)}]
#if f(x1)*f(y)<0, then y=x1
#if f(x1)*f(y)>0, then y=x0

from math import isclose, exp

def false_posi(f, x0, x1, err):
    if x1 < x0:
        print('The Input points a0 and a1 should be such that x0 < x1')
        quit()
    if f(x0)*f(x1)>0:
        print(f'No roots exist between {x0} and {x1}')
        quit()


    accuracy = 1e-9


    if isclose(f(x0), 0, abs_tol=accuracy):
        return x0
    if isclose(f(x1), 0, abs_tol=accuracy):
        return x1

    Xold = x0


    while True:
        Xnew = x0 - f(x0)*((x1 - x0)/(f(x1) - f(x0)))
        if isclose(f(Xnew), 0, abs_tol=accuracy):
            return Xnew
        if isclose(abs((Xnew-Xold)/Xold), err , abs_tol= accuracy):
            return Xnew
        if f(x0)*f(Xnew)<0:
            x1 = Xnew
        else:
            x0 = Xnew
        Xold = Xnew


def fun(x):
    return((1 - exp(-15*9/x))*9.8*x/15 -35)


for i in range(1,50):
    low, up = i*2, (i+1)*2
    if fun(low)*fun(up) < 0:
        break


root = false_posi(fun,low,up,0.001)
print(root)