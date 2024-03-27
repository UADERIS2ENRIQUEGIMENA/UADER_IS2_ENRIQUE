#!/usr/bin/python3
#*-------------------------------------------------------------------------*
#* factorial_range.py                                                      *
#* Calcula los factoriales dentro de un rango especificado                  *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

def factorial(num):
    if num < 0:
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

def calculate_factorials_within_range(start, end):
    for num in range(start, end + 1):
        print("Factorial", num, "! es", factorial(num))

# Obteniendo los límites del rango desde la entrada del usuario
range_input = input("Ingrese el rango (desde-hasta) para calcular los factoriales: ")
start, end = map(int, range_input.split('-'))

print(f"Los factoriales entre {start} y {end} son:")
calculate_factorials_within_range(start, end)
