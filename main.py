from functions import *

# Ahora puedes añadir codigo aqui, como ejemplo:


while True:
    clear()
    multi_menu("Sumar", "Restar", "Multiplicar")
    option = input("Ingresa una opción: ")

    if option == "1":
        sumar()
        wait(2)
    if option == "2":
        restar()
        wait(2)
    if option == "3":
        multiplicar()
        wait(2)