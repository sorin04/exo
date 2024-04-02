from math import exp

def f(x):
    y = 3*x**3 - x**2 - 3
    return y

def Dichotomie(n):
    a = 1
    b = 2
    while b - a > 10**(-n):
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return a, b

interval = Dichotomie(6)
print(f"La racine de l'équation se situe dans l'intervalle [{interval[0]}, {interval[1]}]")
