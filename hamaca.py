#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:37:43 2021
CÁLCULOS HAMACA
Autor: cadecastro.com
"""
import numpy as np
import matplotlib.pyplot as plt
#Valores geométricos:"
L=2500 #[mm] Longitud de la hamaca entre soportes
l=1720 #[mm] Espacio libre entre soportes hamaca
H=1400 #[mm] Altura anclajes hamaca
h=230#[mm] Altura nivel plataforma
#%Carga:
M=150 #;%[kgf] Carga puntual hamaca
g=9.81 #;%[m/s^2] Gravedad
#%Parámetros iteración:
a0=1000 #;%[mm] Valor inicial del parámetro de forma
Nmax=100 #;%Máximo de iteraciones
tol=1e-4 #;%Tolerancia relativa
it=0
cdc=1
n=200 #;%Puntos a graficar
#%SOLUCIÓN:
W=M*g #;%[N] Carga hamaca
dx=l/(n-1) #;%[mm] Resolución longitud
x=np.linspace(-l/2,l/2,n) #;%[mm]
y=np.zeros(n)
y1=np.zeros(n)
y_piso=np.zeros(n)
y_plat=np.zeros(n)
#%Cálculo parámetro catenaria:
while cdc==1:
   it=it+1
   a=l/(2*np.arcsinh(0.5*L/a0))#;%[mm]
   error=abs(a-a0)/a0#;%Error relativo
   if it>=Nmax or error<=tol:
      cdc=0;
   else:
       a0=a
#%Curva catenaria:
k=H-a*np.cosh(0.5*l/a)#;%[mm] Ajuste
for i in range(0,n):
   y[i]=a*np.cosh(x[i]/a)+k#;%[mm]
   y_plat[i]=h#;%[mm]
#%Hamaca cargada:
phi=np.arccos(l/L)#;%[rad] Ángulo
T=0.5*W/np.sin(phi)#;%[N] Tensión
y0=0.5*np.sqrt(L*L-l*l)#;%[mm] Distancia que baja la hamaca cargada
b=H-y0#;%[mm] Intercepto
m=2*y0/l #Pendiente
#Curva hamaca cargada:
for i in range(0,n):
    if x[i]>=0:
        y1[i]=m*x[i]+b
    else:
        y1[i]=-m*x[i]+b
#%Cargas sobre soporte:
Rx=T*np.cos(phi)#;%[N]
Ry=W/2#;%[N]
M0=Rx*H#;%[N*mm]
print('CÁLCULOS HAMACA:')
print('Altura mínima sobre el piso sin carga [mm] =',np.min(y))
print('Altura mínima sobre el piso cargada [mm] =',b)
print('Espacio libre mínimo sobre la plataforma [mm] =',b-h)
print('Ángulo máximo inclinación [grados] =',phi*180/np.pi)
print('Tensión hamaca cargada [N] =',T)
print('Fuerza horizontal sobre el soporte [N] =',Rx)
print('Fuerza vertical sobre el soporte [N] =',Ry)
print('Momento flector base columna [N*mm] =',M0)
print('Parámetro a [mm] =',a)
print('Iteraciones =',it)
print('Error relativo =',error)
#%Gráfica:
plt.figure(1)
plt.plot(x,y,'b')
plt.plot(x,y1,'r')
plt.plot(x,y_plat,'k')
plt.plot(x,y_piso,'k')
plt.grid(True,'both','both')
plt.axis('square')
plt.title('Forma de la hamaca')
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
plt.legend(["Libre","Cargada","Plataforma","Piso"])