from math import exp

def f(x):
    y = -(x**3) +(x) + 2
    return y

def Balayages(n):
    s = -2
    while f(s) <= 10:
        s = s + 10**(-n)
    s = round(s, n)
    t = round(s - 10**(-n), n)
    return t, s

t, s = Balayages(4)
print(t, f"< racine(4) <", s)
