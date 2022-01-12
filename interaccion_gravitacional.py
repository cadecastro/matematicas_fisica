#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:55:07 2021
@author: cadecastro.com
"""
import numpy as np
import matplotlib.pyplot as plt
#%Datos nave:
m=1000#;%[kg] Masa del satélite
#%Datos planeta:
M=5.972e24#;%[kg] Masa cuerpo central
R=6.371e6#;%[m] Radio cuerpo central
#%Condiciones iniciales:
x0=6.371e6#;%[m] Posición inicial en x
y0=0#;%[m] Posición inicial en y
vx0=8000#;%[m/s] Velocidad inicial en x
vy0=0#;%[m/s] Velocidad inicial en y
#%Datos segundo disparo cohete:
t1=600#;%[s] Tiempo inicial disparo cohete
dt1=60#;%[s] Intervalo de tiempo de disparo
Fx=-50000#;%[N] Componente fuerza segundo disparo en x
Fy=110000#;%[N] Componente fuerza segundo disparo en y
#%Parámetros simulación:
tf=3600*24*0.50#;%[s] Tiempo total simulación
dt=0.1#;%[s] Tamaño de paso de tiempo
G=6.67e-11#;%[N*m^2/kg^2] Constante gravitacional
#%SOLUCIÓN:
n=int(tf/dt+1)
t=np.linspace(0,tf,n)
x=np.zeros(n)
y=np.zeros(n)
vx=np.zeros(n)
vy=np.zeros(n)
x[0]=x0
y[0]=y0
vx[0]=vx0
vy[0]=vy0
for i in range(0,n-1):
    if t[i]>=t1 and t[i]<=t1+dt1:
        vx[i+1]=vx[i]+dt*(-G*M*x[i]/np.power(x[i]*x[i]+y[i]*y[i],1.5)+Fx/m)
        vy[i+1]=vy[i]+dt*(-G*M*y[i]/np.power(x[i]*x[i]+y[i]*y[i],1.5)+Fy/m)
    else:
        vx[i+1]=vx[i]-dt*(G*M*x[i]/np.power(x[i]*x[i]+y[i]*y[i],1.5))
        vy[i+1]=vy[i]-dt*(G*M*y[i]/np.power(x[i]*x[i]+y[i]*y[i],1.5))
    x[i+1]=x[i]+dt*vx[i+1]
    y[i+1]=y[i]+dt*vy[i+1]
#¨%Cuerpo central:
xp=np.linspace(-R,R,100)
yps=np.zeros(100)
ypi=np.zeros(100)
for i in range(0,100):
   yps[i]=np.sqrt(R*R-xp[i]*xp[i]);
   ypi[i]=-1*np.sqrt(R*R-xp[i]*xp[i]); 
#%Gráficas:
plt.figure(1)
plt.plot(xp,yps,'k')
plt.grid(True,'both','both')
plt.axis('equal')
plt.title('Trayectoria')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.plot(xp,ypi,'k')
plt.plot(x,y,'r')
plt.figure(2)
plt.subplot(211)
plt.plot(t,x,'b')
plt.plot(t,y,'r')
plt.grid(True,'both','both')
plt.title('Posición en el tiempo')
plt.xlabel('t [s]')
plt.ylabel('Posición [m]')
plt.legend(['x','y'])
plt.subplot(212)
plt.plot(t,vx,'b')
plt.plot(t,vy,'r')
plt.grid(True,'both','both')
plt.title('Velocidad en el tiempo')
plt.xlabel('t [s]')
plt.ylabel('Velocidad [m/s]')
plt.legend(['v_x','v_y'])