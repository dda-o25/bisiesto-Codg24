"""
Carlos Osvaldo Díaz García

Fecha
18 de septiembre de 2025

Determinar si un año es o no bisiesto. Según la 
Wikipedia: “Año bisiesto es el divisible entre 4, 
salvo que sea año secular -último de cada siglo, 
terminado en «00»-, en cuyo caso ha de ser 
divisible entre 400”.
"""

# Declaraciones
año_bisiesto = 4
año_secular = 400

# Entradas
año = input("Introduzca un año: ")
año_numero = int(año)

# Proceso
if año_numero % año_secular == 0:
    # Salida
    print(año_numero, "sí es un año bisiesto")
elif año_numero % año_bisiesto == 0 and año[len(año)-2:len(año)] != "00":
    # Salida
    print(año_numero, "sí es un año bisiesto")
else:
    # Salida
    print(año_numero, "no es un año bisiesto")
