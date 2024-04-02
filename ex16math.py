#Exercices 16
def f(x):
    y = x**3-3*x+1
    return y

def Dichotomie(n):
    a=-1
    b=1

    while b-a>10**(-n):
        m=(a+b)/2
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
    return m

print(Dichotomie(4))
#Exercices 17
from math import exp

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