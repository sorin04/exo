#Exercices 17
from math import exp

def f(x):
    y = exp (x)-x-2
    return y

def Dichotomie(n):
    a = 0
    b=2
    while b-a>10**(-n):
        m=(a+b)/2
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
    return m

print(Dichotomie(6))