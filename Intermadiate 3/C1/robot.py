from time import sleep
from random import randint,choice

def Radikal(Addad,Forge=2):
    return Addad ** (1/Forge)

def Ghadrmotlagh(X):
    """
    Ghadre motlagh ya abs() ye addad
    """
    if X < 0:
        return -X
    else:
        return X

def delay(X):
    X = X/1000
    sleep(X)

def RobotMove():
    mot = ["Right","Left","Forward","Backward"]
    return choice(mot)

def Hello():
    """
    Says Hello :)
    """
    print("Hello to You Ay User")

