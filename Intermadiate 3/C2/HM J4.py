Yekan = ['',"I","II","III","IV","V","VI","VII","VIII","IX"]								
Dahgan = ['',"X","XX","XXX","XL","L","LX","LXX","LXXX","XC"] 								
Sadgan = ['',"C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]

while True:
    adad = int(input("Adade mored nazar ra vared konid: "))

    sad = int(adad % 1000 / 100) #sadgane yek adad
    dah = int(adad % 100 / 10) #dahgane yek adad
    yek = int(adad % 10 )#yekane yek adad

    print(Sadgan[sad] + Dahgan[dah] + Yekan[yek])
#Yekan[yek] #Yekanemon be shekl yunani
#Dahgan[dah] #Dahganemon be shekl yunani
#Sadgan[sad] #Sadganemon be shekl yunani

















































