"""
Examen de Recuperación 3D
Graficacion 
ISIC
EDUARDO GONZALEZ FLORES
El siguiente ejercicio plotea tres triangulos uno de base y otros 2 
segun el hitpoint, el ejercicio nos pide utilizar la formula de Heron
para calcular las areas de los triangulos.
"""
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, sqrt

plt.axis([0, 150, 100, 0])
plt.axis('on')
plt.grid(False)
x = [50, 65, 70, 75]  # Aqui podemos cambiar las coordenadas de los puntos *obvio*
y = [60, 10, 70, 60]
z = [0, 0, 0, 0]

plt.plot([x[0], x[1]], [y[0], y[1]], color='k')  # PLoteamos las lineas del Trinagulo Base "A"
plt.plot([x[1], x[2]], [y[1], y[2]], color='k')
plt.plot([x[2], x[0]], [y[2], y[0]], color='k')
plt.scatter(x[3], y[3], s=20, color='r')
#PLoteamos los vertices de los otros triangulos segun el hitpoint
plt.plot([x[0], x[3]], [y[0], y[3]], linestyle=':', color='GREEN')
plt.plot([x[1], x[3]], [y[1], y[3]], linestyle=':', color='GREEN')
plt.plot([x[2], x[3]], [y[2], y[3]], linestyle=':', color='GREEN')


a = x[1]-x[0]  # calculamos las vertices de los puntos 0 y 1
b = y[1]-y[0]
c = z[1]-z[0]
Q01 = sqrt(a*a+b*b+c*c)

a = x[2]-x[1]  # calculamos las vertices de los puntos 1 y 2
b = y[2]-y[1]
c = z[2]-z[1]
Q12 = sqrt(a*a+b*b+c*c)

a = x[2]-x[0]  # calculamos las vertices de los puntos 2 y 0
b = y[2]-y[0]
c = z[2]-z[0]
Q02 = sqrt(a*a+b*b+c*c)

a = x[1]-x[3] #Calculamos la distancia del punto 1 al hitpoint que es 3
b = y[1]-y[3]
c = z[1] = z[3]
Q13 = sqrt(a*a+b*b+c*c)

a = x[2]-x[3]  # Calculamos la distancia del punto 2 al hitpoint que es 3
b = y[2]-y[3]
c = z[2]-z[3]
Q23 = sqrt(a*a+b*b+c*c)

a = x[0]-x[3]  # Calculamos la distancia del punto 3 al hitpoint que es 3
b = y[0]-y[3]
c = z[0]-z[3]
Q03 = sqrt(a*a+b*b+c*c)

s = (Q01+Q12+Q02)/2  #Se calculan las areas de los triangulos A, A1 Y A2 segun HERON
A = sqrt(s*(s-Q01)*(s-Q12)*(s-Q02))

s1 = (Q01+Q03+Q13)/2
A1 = sqrt(s1*(s1-Q01)*(s1-Q03)*(s1-Q13))

s2 = (Q02+Q23+Q03)/2
A2 = sqrt(s2*(s2-Q02)*(s2-Q23)*(s2-Q03))

#Ploteamos los textos que muestran las areas calculadas 
plt.text(20, 70, 'A1=', color='b')
dle = '%7.0f' % (A1)
dls = str(dle)
plt.text(25, 70, dls)

plt.text(20, 75, 'A2=', color='b')
dle = '%7.0f' % (A2)
dls = str(dle)
plt.text(25, 75, dls)

plt.text(20, 80, 'A1+A2=', color='b')
dle = '%7.0f' % (A1+A2)
dls = str(dle)
plt.text(32, 80, dls)

#Condicion que muestra un mensaje si el hitpoint esta dentro o fuera de los limites
if A1+A2 > A:
    plt.text(20, 85, 'Fuera del limite', color='b')
else:
    plt.text(20, 85, 'Dentro del limite', color='b')

plt.show()
