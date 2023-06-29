##Variables 
#tuple 
#mot = (1,1,5,1,1)
#print(mot)
#print(mot[2])
#mot += (2,)
#print(mot)
#print(type(mot))

#bytes
#mot = b'Hi Hello Wolrd'
#print(type(mot))

#set
#mot = {1,1,1,1,1,1,2,2,2,2,2,None,"Hello"}
#print(mot)
#print(type(mot))
#print(len(mot))
#print("Hello" in mot)
#for meghdar in mot:
#    print(meghdar)

#Dictionary
#mot = { "Names" : ["Mohsen","Ali","Hassan","Sara","Nahal","MMd"]}
#print(mot)
#print(type(mot))
#print(mot["Names"])
#mot["Ages"] = [19,15,18,20,34,56,120]
#print(mot)
#for Khoone in mot:
#    print(mot[Khoone])
#Inter3 = {
#    "Names": ["Foad","AmirMohammad","Arsalan","Mohsen","Hossein","MohammadAli","Kiana","Amin"],
#    "Last Names": ["BaniHashemi","Anaghi","Tavangari","Khak Aji","Khosh doost","Mirkamali","Agha Ebrahim","Maleki"],
#    "Grades":[20,20,20,20,20,20,20,20,20]
#}
#
#print(Inter3)
#for Khoone in Inter3:
#    print(Khoone)
#for i in range(0,8):
#    print(Inter3["Names"][i],end=' ')
#    print(Inter3["Last Names"][i],end=' ')
#    print(Inter3["Grades"][i])

##STRINGS
#mot = "Hello My name is Mohsen Shnarden Mohsen Mohsen burden kharden bart"
#len()
#print(len(mot))

#count()
#mot = "aaaaaaaaabbbbbbccccccabMohsenALiALi"
#print(   mot.count("ALi")  )

#lower()
#mot = "Hello WORLD"
#print(mot.lower())

#upper()
#mot = "hello to you all"
#print(mot.upper())

#encode()
#mot = "Hello World!"
#mot2 = mot.encode()
#print(type(mot))
#print(type(mot2),mot2)

#decode()
#mot = b'Hello World!'
#mot2 = mot.decode()
#print(type(mot))
#print(type(mot2))

#index()
#mot = "abcdefghijklmnopqrstuvwxyz ab hello abr"
#print(mot.index("mnop"))
#print(mot[12:15])
#print(mot[36:39])
#print(mot[8:13:2])


#mot = "Mohsen,Ali,Hassan,Teame,Melli,Medale,Noghre,Gereft"
#print(mot)
#print( mot.replace(","," "))

##split() #splitlines()
#mot = "Mohsen,Ali,Hassan,Teame,Melli,Medale,Noghre,Gereft"
#lista = mot.split(",")
#print(lista)


##Functions
##def
#def Zarb(x,y):
#    print(x*y)
#    
#Zarb(3,5)
#Zarb(4,5)

#def mohsebat(x):
#    x += 10
#    x /= 5
#    x *= 40
#    x **= 2
#    print(x)
#    return x
#
#mot = mohsebat(5)

#def Radikal(x,y):
#    return x ** (1/y)
#
#javab = Radikal(16,2)
#print(javab)

#def Factoriel(x):
#    javab = 1
#    for i in range(1,x+1):
#        javab = javab * i
#    return javab





  



















