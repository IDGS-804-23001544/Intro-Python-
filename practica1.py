#Crea un programa que permita realizar operaciones de multiplicacion con sumas

num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe un segundo numero: "))

contador = 1
resultado = 0
operacion = ""

while contador <= num1:
    resultado += num2
    operacion += str(num2)

    if contador < num1:
        operacion += " + "

    contador += 1

print("\nEl resultado de {0} por {1} es: {2}".format(num1, num2, resultado))
print(operacion)
