# crear un programa que permita realizar las operaciones basicas 
# utilizando una funcion para cada operacion y un menu principal 
# para desplegar y elegir que operacion realizaremos

import os

def suma():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("La suma es:", a + b)

def resta():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("La resta es:", a - b)

def multiplicacion():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("La multiplicación es:", a * b)

def division():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    if b != 0:
        print("La división es:", a / b)
    else:
        print("Error: No se puede dividir entre cero")

def menu():
    print("MENÚ PRINCIPAL")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    opcion = 0
    while opcion != 5:
        os.system("cls")  
        menu()
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
