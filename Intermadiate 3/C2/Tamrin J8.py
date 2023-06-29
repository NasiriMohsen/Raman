while True:
    listadad = []
    adad = input("Adad ra vared konid: ")
    for i in adad:
        listadad.append(i)   
    listadad.reverse()
    for j in listadad:
        print(j,end="")
    print("")