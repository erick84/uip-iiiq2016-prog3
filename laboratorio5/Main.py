a = "fiebre"
b = "muerto"
c = "normal"
d = "enfermo"
x = True
temp = float

while x:

    while x:
        try:
            archivo = open('temperatura.txt', 'a+')
            temp = float(input("ingrese una temperatura "))
            x = False
        except Exception:
            print("intenta de nuevo")
        else:
            archivo = open('temperatura.txt', 'a+')
            if temp > 37.5:
                print("tienes fiebre " )
                archivo.write(str(temp) + " " + a + "\n")
                archivo.close()

            elif temp < 5:
                print("jajajajaja estas muerto " )
                archivo.write(str(temp) + " " + b + "\n")

            elif temp >=5 and temp <=35 :
                print("estas enfermo " )
                archivo.write(str(temp) + " " + d + "\n")

            else:
                print("estas bien " )
                archivo.write(str(temp) + " " + c + "\n")
                archivo.close()
    else:

        s = input("desea continuar s / n")
        if s == 's':
            x = True
else :
    print("good by..")
    x = False
