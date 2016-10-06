val1 = []
agua = 0
fuego = 0

x = True
while x:
    frase = input("escriba su frase: \n")
    if "agua" in frase:
        agua=agua+1
    if "fuego" in frase:
        fuego=fuego+1

    if "agua" in frase or "fuego" in frase:
        val1.append(frase)
        print("escriba salir para salir o ")
    if frase == "salir":
        x = False

agua = {'agua' : agua}
fuego = {'fuego' : fuego}
print("agua =", agua)
print("fuego =",fuego)
print(val1)


















