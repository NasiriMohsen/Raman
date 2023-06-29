print("")
##sakhte list:
#a = [0,-1,1.5,[0],(2,5),{2},"str"]
#print(a,type(a)) 

##tedad khoone haye list (len)
#a = [1,2,3,4,5,6,7,8,9,10]
#print(a,len(a))

##namayesh meghdar khoone
#a = [0,0,0,0,0,0,1,0,0,0,0,0,0]
#print( a[6] )

##taghir meghdar khoone
#a = [0,0,0,0,0]
#print(a)
#a[2] = 1
#print(a)

##list dar list
#a = [0,0,"$",0,0]
#b = [[0,0,0],[0,0,"$"],[0,0,0]]
#c = [[[0,0,0],[1,1,1],[2,2,2]],[[3,3,3],[4,4,4],[5,5,5]]]
#print(c[0][0][0])

##namayesh akharin khoone ya khoone ha az akhar
#a = [0,1,2,3,4,5,6]
#print(a[-1])
#print(a[-2])
#print(a[-3])
#print(a[-4])
#print(a[-5])
#print(a[-6])
#print(a[-7])


##ezafe kardan be list (append)
#a = [0,0,0,0,0,0]
#print(a)
#a.append(1)
#a.append(2)
#a.append(3)
#a.append("hello")
#print(a)

##moratab sazi list int (sort)
#a = [0,4,3,6,5,8,7,1,9,2,20,100,4000,1.6,-1]
#print(a)
#a.sort()
#print(a)


##moratab sazi list str (sort)
#a = ["a","d","b","e","c","!","5","1"]
#print(a)
#a.sort()
#print(a)

##moratab sazi list baraks (sort)
#a = ["a","d","b","e","c","!","5","1"]
#b = [0,4,3,6,5,8,7,1,9,2,20,100,4000,1.6,-1]
#a.sort()
#b.sort()
#print(a)
#print(b)

##baraks kardan azaye list (reverse)
#a = [0,2,4,5,1,3,5,6,7,9]
#a.reverse()
#print(a)

##shomare khoone (index)
#a = ["a","b","c","d","ali","amir","ok"]
#print(a.index("amir"))

##ezafe kardan bedune taghir khoone (insert)
#a = [0,1,2,3,4,5]
#a.insert(3,"a")
#print(a)

##hazf ye meghdar as aval (remove)
#a = [2,3,2,3,2]
#a.remove(3)
#print(a)

##vojud ye meghadr dar list
#a = ["mohsen","ali",0,1,2,3]
#print("mohsen 2" in a)

##tedad ye meghadar dar list (count)
#a = [0,0,0,0,0,0,1,0,1,0,1,0,0]
#print(a.count(1))

##hazf khoone ya akharin dar list va return on (pop)
#a = [0,1,2,3,4,5]
#print(a.pop(2))
#print(a)

##namyesh list az khooneye felan ta felan
#a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(a[5:11])
#b = a[10:21]
#print(b)

##namyesh list az khooneye felan ta felan yeki darmion va ...
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(a[0:20])