from functions import *

# Ahora puedes añadir codigo aqui, como ejemplo:


while True:
    clear()
    multi_menu("Sumar", "Restar", "Multiplicar")
    option = input("Ingresa una opción: ")

    if option == "1":
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        print(sumar(num1, num2))
        wait(2)
    if option == "2":
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        print(restar(num1, num2))
        wait(2)
    if option == "3":
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        print(multiplicar(num1, num2))
        wait(2)