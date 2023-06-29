import random

def Radikal(x,y):
    return x ** (1/y)

def Factoriel(x):
    javab = 1
    for i in range(1,x+1):
        javab = javab * i
    return javab

def Zarb(X,Y):
    return X*Y

def Tavan(X,Y):
    return X**Y

def Tas():
    return random.randint(1,6)

def Shans(X,Y):
    return random.randint(X,Y)