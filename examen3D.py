"""
Intersection example
"""
import tools3d
from math import sin, cos, radians, sqrt
from tools3d import rotRx, rotRy, rotRz
import matplotlib.pyplot as plt
import numpy as np
from math import cos, radians, sin, sqrt

#___Coordenadas iniciales
xg = []
yg = []
zg = []

#____Coordenadas centrales
xc = 80
yc = 40
zc = 40

#______Plano y linea del sistema
x = [-40, -40, 40, 40, -40, 50]
y = [0, 0, 0, 0, -20, 3]
z = [-10, 10, 10, -10, 15, 10]

for i in range(len(x)):
  xg.append(x[i]+xc)
  yg.append(y[i]+yc)
  zg.append(z[i]+zc)

#_____Plotear el sistema


def plotPlaneLine(xg, yg, zg, xh, yh, xhg, yhg, hitcolor):
  plt.axis([0, 250, 200, 0])
  plt.axis('on')
  plt.grid(True)
  plt.plot([xg[0], xg[1]], [yg[0], yg[1]], color='k')
  plt.plot([xg[1], xg[2]], [yg[1], yg[2]], color='k')  # Plano
  plt.plot([xg[2], xg[0]], [yg[2], yg[0]], color='k')

  plt.plot([xg[3], xg[4]], [yg[3], yg[4]], color='b')  # Line

  if hitcolor == 'g':
    plt.scatter(xg[4], yg[4], s=20, color=hitcolor)
  else:
    plt.scatter(xhg, yhg, s=20, color=hitcolor)

  plt.show()

def areas(x,y,z):

  a=x[0]-[1]
  b=x[0]-y[1]
  c=x[0]-y[1]
  Q01 = sqrt(a*a+b*b+c*c)

  a = x[1]-[2]
  b = x[1]-y[2]
  c = x[1]-y[2]
  Q12 = sqrt(a*a+b*b+c*c)

  a = x[2]-[0]
  b = x[2]-y[0]
  c = x[2]-y[0]
  Q20 = sqrt(a*a+b*b+c*c)




def hitpoint(x, y, z):

  #___Distancia point 4 to 3
  a = x[4]-x[3]
  b = y[4]-y[3]
  c = z[4]-z[3]
  Q45 = sqrt(a*a+b*b+c*c)
  #___unit vector components point 4 to 5
  lx = a/Q45
  ly = b/Q45
  lz = c/Q45

  #___Distancia point  0 to 3
  a = x[3]-x[0]
  b = y[3]-y[0]
  c = z[3]-z[0]
  Q03 = sqrt(a*a+b*b+c*c)
  #___unit vector components point 0 to 3
  ux = a/Q03
  uy = b/Q03
  uz = c/Q03

  #___Distancia point 0 to 1
  a = x[1]-x[0]
  b = y[1]-y[0]
  c = z[1]-z[0]
  Q01 = sqrt(a*a+b*b+c*c)
  #___unit vector components point 0 to 1
  vx = a/Q01
  vy = b/Q01
  vz = c/Q01

  #____Normal vector unit
  nx = uy*vz-uz*vy
  ny = uz*vx-ux*vz
  nz = ux*vy-uy*vx
  #___vector components 0 yo 4
  vx1b = x[4]-x[0]
  vy1b = y[4]-y[0]
  vz1b = z[4]-z[0]
  #___perpenticular distance 4 to plane
  Qn = (vx1b*nx+vy1b*ny+vz1b*nz)
  #____Cos of angle p

  cosp = lx*nx+ly

  #___DIstance 4 to hit POINT

  Qh = abs(Qn/cosp)

  #___Hit point coordinates
  xh = x[4]+Qh*lx
  yh = y[4]+Qh*ly
  zh = z[4]+Qh*lz

  #___global point coordinates
  xhg = xh+xc
  yhg = yh+yc
  zhg = zh+zc
  #__________Checar si la linea de 4 a 5 queda fuera de los valores del rectangulo
  #__________Component of vector V0H
  a = xh-x[0]
  b = yh-y[0]
  c = zh-z[0]
  #_________dot products
  up = a*ux+b*uy+c*uz
  vp = a*vx+b*vy+c*vz

  #_______SI NO ESTAMOS SALIENDO DEL PLANO DEL OBJETO RECTANGULO
  hitcolor = 'r'
  if up < 0:
    hitcolor = 'b'
  if up > Q03:
    hitcolor = 'b'
  if vp < 0:
    hitcolor = 'b'
  if vp > Q01:
    hitcolor = 'b'

  #_______SI EL PUNTO DE 4 A 5 NO ALCANZA EL HITPOINT
  a = x[4] - x[3]
  b = y[4] - y[3]
  c = z[4] - z[3]
  Q45 = sqrt(a*a+b*b+c*c)
  if Q45 < Qh:
    hitcolor = 'g'
  return xh, yh, xhg, yhg, hitcolor


def plotPlaneLinex(xc, yc, zc, Rx):
  for i in range(len(y)):
    [xg[i], yg[i], zg[i]] = rotRx(xc, yc, zc, x[i], y[i], z[i], Rx)
    [x[i], y[i], z[i]] = [xg[i]-xc, yg[i]-yc, zg[i]-zc]
  xh, yh, xhg, yhg, hitcolor, = hitpoint(x, y, z)
  plotPlaneLine(xg, yg, zg, xh, yh, xhg, yhg, hitcolor)


def plotPlaneLiney(xc, yc, zc, Ry):
  for i in range(len(y)):
    [xg[i], yg[i], zg[i]] = rotRy(xc, yc, zc, x[i], y[i], z[i], Ry)
    [x[i], y[i], z[i]] = [xg[i]-xc, yg[i]-yc, zg[i]-zc]
  xh, yh, xhg, yhg, hitcolor, = hitpoint(x, y, z)
  plotPlaneLine(xg, yg, zg, xh, yh, xhg, yhg, hitcolor)


def plotPlaneLinez(xc, yc, zc, Rz):
  for i in range(len(y)):
    [xg[i], yg[i], zg[i]] = rotRz(xc, yc, zc, x[i], y[i], z[i], Rz)
    [x[i], y[i], z[i]] = [xg[i]-xc, yg[i]-yc, zg[i]-zc]
  xh, yh, xhg, yhg, hitcolor, = hitpoint(x, y, z)
  plotPlaneLine(xg, yg, zg, xh, yh, xhg, yhg, hitcolor)


#______Pedir al usuario que eje desea trabajr y plotear
while True:
  axis = input(
      "Teclea el eje que deseas visualizar 'x,y,z' o pulsa w para salir: ")
  if axis == 'x':  # plotear el eje x
    Rx = radians(float(input('Dame los grados de rotacion: ')))
    plotPlaneLinex(xc, yc, zc, Rx)  # Llamamos a la funcion de ploteo
  if axis == 'y':
    Ry = radians(float(input('Dame los grados de rotacion: ')))
    plotPlaneLiney(xc, yc, zc, Ry)  # Llamamos a la funcion de ploteo
  if axis == 'z':
    Rz = radians(float(input('Dame los grados de rotacion: ')))
    plotPlaneLinez(xc, yc, zc, Rz)  # Llamamos a la funcion de ploteo
  if axis == 'w':
    break
