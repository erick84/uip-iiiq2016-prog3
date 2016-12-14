class Estudiante:
    conteo = 0

    def __init__ (self, nombre, notas, promedio):
        self.nombre = nombre
        self.notas = notas
        self.promedio = promedio
        Estudiante.conteo +=1

    def mostrarConteo (self):
        print ("Total de Estudiantes: " + str(Estudiante.conteo))

    def mostrarEstudiante (self):
        print(" nombre " + self.nombre, + " notas " + self.notas, + " promedio " + self.promedio)

menu = [' 1. Crear Estudiante 2. Calcular promedio 3. Salir ']
print(menu)
opcion = input("Ingrese un numero")
nota1 = int
nota2 = int
nota3 = int


if int (opcion) == 1:
    estu1 = input("ingrese el nombre del estudiante: ")
    conteo = Estudiante()

elif int (opcion) == 2:
    nota1 = input("ingrese la primera nota")
    nota2 = input("ingrese la segunda nota")
    nota3 = input("ingrese la tercera nota")

else :
    print("salir")
