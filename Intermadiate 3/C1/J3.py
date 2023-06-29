##sakhte list:
##a = [1,0.1,"hi",'HI',[90],(1,2)]
#print(a)


##tedad khoone haye list (len)
#a = [0,1,2,3,4,5,6]
#print(len(a))


##namayesh meghdar khoone
#a = ["Yes",0,1,2,3,4,"Hi","Bye",(1,2)]
#print(a[3])

##taghir meghdar khoone
#a = [0,0,0,0,0,0,0]
#print(a)
#a[3] = 1
#a[5] = 5
#print(a)

###list dar list
#a = [0,"$"]
#b = [[0,0],[0,"$"]]
#c = [ [[0],[0]] , [[0],[0]] , [ [0] , ["$"]  ] ,[[0],[0]],[[0],[0]]]
#print( c[2][1][0] )
#print(   a[1]    )
#print(   b[1][1]   )

##namayesh akharin khoone ya khoone ha az akhar
#a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4]
#a = [1,5,2,9,8,7,6,3,1,4,2,1,5,2,7,3,8,3]
#print(a[-7])

##ezafe kardan be list (append)
#a = [0,1]
#print(a)
#a.append(545)
#print(a)
#a.append(5)
#print(a)
#a.append("DIDI APPEND KARDAM")
#print(a)
#a.append("Bye")
#print(a)
#a.append([1,1,1,1])
#print(a)

#moratab sazi list int (sort)
#a = [9,6,4,5,3,2,8,7,1,0]
#a.sort()
#print(a)

##moratab sazi list str (sort)
#a = ["a","!","A","b","B"]
#a.sort()
#print(a)

#moratab sazi list baraks (sort)
#a = [9,6,4,5,3,2,8,7,1,0]
#a.sort(reverse=True)
#print(a)

##baraks kardan azaye list (reverse)
#a = ["a","b",1,2,6,3]
#a.reverse()
#print(a)

##shomare khoone (index)
#a = ["a","b","c"]
#print(a.index("c"))

##ezafe kardan bedune taghir khoone (insert)
#a = [0,0,0,0,0]
#a.insert(2,"Hello")
#print(a)
#a.insert(5,5)
#print(a)

##hazf ye meghdar as aval (remove)
#a = [0,0,1,0,1,0,0,2,2,0,0,1,1,1]
#print(a)
#a.remove(1)
#print(a)

##vojud ye meghadr dar list
#a = ["A","b",0,1]
#print()

##tedad ye meghadar dar list (count)
#a = [0,0,0,0,0,0,1,1,1,1,2,2,2,2]
#print(a.count(1))

##hazf khoone ya akharin dar list va return on (pop)
#a = [0,1,2,3,4,5,6,7,8,9]
#print(a.pop(3),a)

##namyesh list az khooneye felan ta felan
#a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#b = a[5:11]
#print(a)
#print(b)

##namyesh list az khooneye felan ta felan yeki darmion va ...
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b = a[7:16:3]
print(b)