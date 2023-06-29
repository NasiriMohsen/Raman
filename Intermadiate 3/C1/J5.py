##Variables 
#tuple
#mot = (150,255,25)
#print(mot)
#print(mot[3])
#mot  = mot + (0,)
#mot = mot + (2,)
#mot += (5,)
#print(mot)
#print(type(mot))
#mot = (255,150,250)
#print(mot)
#Red,Green,Blue = mot
#print(Red)
#print(Green)
#print(Blue)

#bytes
#mot = b"Hello World"
#print(type(mot),mot)

#set
mot = {1,1,1,1,1,1,1,1,2,2,2,2,2,5,5,5,5,5,None,(0,1),"sasdasd"}
#print(mot)
#print(mot)
#print(type(mot))
#print(len(mot))
#print("Hello" in mot)
#for meghdar in mot:
#    print(meghdar)

#Dictionary
#mot = { 6: 0}
#print(mot)
#print(mot[6])
#print(mot)
#print(type(mot))
#print(mot["Esmha"])
#print(mot[5])
#Inter3 = {
#        "Names" : ["Hamid","Seyed Reza","Mahan","Mohammad","Matin","Kiarash"],
#        "Age" : [20,18,22,14,10,15],
#        "Grades" : [20,20,18,18,17,20],
#        "Last Name" : ["H","SR","Mah","Mo","Mat","K"]
#}
#
#Inter3["Ghad"] = [190,180,210,120,175,195]

##print(Inter3)
#print()
#print(Inter3["Ghad"])

#for Khoone in Inter3:
#    print(Khoone)
#
#print( )
#
#for meghdar in Inter3["Age"]:
#    print(meghdar)
#####################################################
##STRINGS
#mot = "Hello My name is Mohsen Shnarden Mohsen Mohsen burden kharden bart"
##len()
#print(len(mot))

##count()
#mot = "aaaaaaaaabbbbbbccccccabMohsenALiALi"
#print(   mot.count("ALi")  )

##lower()
#mot = "Hello WORLD"
#print( mot.lower() )
   
##upper()
#mot = "hello to you all"
#print( mot.upper() )



##encode()
#mot = "Hello World!"
#mot2 = mot.encode()
#print(type(mot),mot)
#print(type(mot2),mot2)

##decode()
#mot = b'Hello World!'
#mot2 = mot.decode()
#print(type(mot),mot)
#print(type(mot2),mot2)
