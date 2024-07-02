# Imports
import os
import time
import json
import csv

# Funcs

def clear():
    return os.system("cls")

def wait(s):
    return time.sleep(s)

def multi_menu(*texts):
    for i, option in enumerate(texts, start=1):
        print(f"{i}.- {option}")


# Example Functions
def sumar():
    num1 = int(input("Ingresa tu primer numero: "))
    num2 = int(input("Ingresa tu segundo numero: "))
    return print(num1 + num2)

def restar():
    num1 = int(input("Ingresa tu primer numero: "))
    num2 = int(input("Ingresa tu segundo numero: "))
    return print(num1 - num2)

def multiplicar():
    num1 = int(input("Ingresa tu primer numero: "))
    num2 = int(input("Ingresa tu segundo numero: "))
    return print(num1 * num2)

