# Programa para calcular el area de un triangulo conociendo solo sus vertices, se utiliza la formula de Herón
# Ingresa los puntos del plano cartesiano
import matplotlib.pyplot as plt
import numpy as np
from math import *

x1 = int(input("Ingrese X1: "))
y1 = int(input("Ingrese Y1: "))
x2 = int(input("Ingrese X2: "))
y2 = int(input("Ingrese Y2: "))
x3 = int(input("Ingrese X3: "))
y3 = int(input("Ingrese Y3: "))

#Calcula e imprime las longitudes de los lados utilizando la formula de distancia entre 2 puntos
print("Los puntos son:(", x1, ",", y1, ")(", x2, ",", y2, ")(", x3, ",", y3, ")")
a1 = (y2-y1)**2 + (x2-x1)**2
a = sqrt(a1)
b1 = (y3-y2)**2 + (x3-x2)**2
b = sqrt(b1)
c1 = (y3-y1)**2 + (x3-x1)**2
c = sqrt(c1)


print("La longitud del lado a es:", a)
print("La longitud del lado b es:", b)
print("La longitud del lado c es:", c)

#Segun la formula de Herón para hallar el area de un triangulo conociendo solo sus lados es necesario el semiperimetro"

p = (a+b+c)/2.0

print("El semiperimetro es:", p)

#Calculando el area

A1 = p*(p-a)*(p-b)*(p-c)
A = sqrt(A1)


print("El Area del tringulo es:", A)


#Fin
