while True:
    X = input("Tool Cheghadr ast? ")
    if X.lower() == "stop" or X.lower() == "exit":
        break
    Y = input("Arz Cheghadr ast? ")
    if Y.lower() == "stop" or Y.lower() == "exit":
        break

    X = int(X)
    Y = int(Y)

    Mohit = (X + Y) * 2
    Masahat = X * Y

    print("Masahat = ",Masahat)
    print("Mohit = ",Mohit)

