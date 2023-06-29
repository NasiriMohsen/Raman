#def mohsen(x,y,c,g,a):
#    """
#    Check kardane meghdar x
#    """
#
#    if x > 100:
#        return 100
#    else:
#        return x

#mohsen = lambda x: x > 100

#print(abs(-50),abs(-100),abs(99))

#print(round(1.4),round(1.5),round(1.6))

#help(mohsen)

import math 
#import math as M
#from math import *

#print(    math.sqrt(36)            )
#print(    math.factorial(5)        )
#print(    math.pow(5,2)            )
#print(    math.pi                  )
#print(    math.inf                 )
#print(    math.radians(180)        )
#print(    math.degrees(math.pi)    )
#print(    math.sin(1)              )
#print(    math.cos(1)              )
#print(    math.tan(1)              )
#print(    math.cot(1)              )

#import time
#import time as T
#from time import time,ctime,sleep

#print("Start counting")
#sleep(5)
#print("BOOOOM")

#start = time()
#print("smt")
#end = time()
#print(end-start)

#while True:
#    alan = time()
#    print(ctime(alan))


#import random
#import random as R
#from random import random,randint,choice

#print(random())
#print(randint(1,10000))

#mot = [54,45,51]
#mot2 = [mot,1000,2000,-200]
#
#print( choice(mot2) )


#import robot
#import robot as r
#from robot import *

#robot.Hello()
#print( robot.Radikal(27,3) )
#print( robot.Ghadrmotlagh(100) )

#while True:
#    print( RobotMove() )
#    delay(500)


#Error: ZeroDivisionError
#print( 2 / 0)

#Error: NameError
#print( X ) 


#try:
#    print( X ) 
#    print( 2/0 ) 
#except NameError:
#    print(" X ro tarif nakrdim")
#except:
#    print("Error dad")





from time import sleep

while True:
    sleep(0.5)

    try:
        print( X ) 
        print(  2/X)
        print("asdasda"**"asdasdasd")

    except NameError:
        print("Moteghayere X tarif nashode bud")
        X = 0

    except ZeroDivisionError:
        print("X mosavi sefrast error mide")
        X = 1

    except Exception as Peygham:
        pass