#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:37:21 2021
@author: cadecastro.com
«Todos amamos a Python, y a su glorioso régimen»
"""
import numpy as np
import matplotlib.pyplot as plt
v0=220#[m/s] Velocidad inicial de disparo
theta0=-180/np.pi*np.arctan(25/60)+1#[grados] Ángulo de disparo
y0=25.0 #[m] Altura inicial
tf=0.330#[s] Tiempo final simulación
dt=0.0001#[s] Paso de tiempo
m=1.15e-3#[kg] Masa del proyectil
S=np.pi/4*0.0055*0.0055#[m^2] Área frontal proyectil
CD=0.389#Coeficiente de arrastre medio
rho=0.91#[kg/m^3] Densidad del aire
g=9.81#[m/s^2] Magnitud aceleración gravedad

#SOLUCIÓN:
N=int(tf/dt+1)
theta0=theta0*np.pi/180#[rad]
t=np.linspace(0,tf,N)
x=np.zeros(N)#
y=np.zeros(N)#
vx=np.zeros(N)#
vy=np.zeros(N)#
v=np.zeros(N)#
D=np.zeros(N)#
theta=np.zeros(N)#
y[0]=y0#
vx[0]=v0*np.cos(theta0)#
vy[0]=v0*np.sin(theta0)#
v[0]=v0#
theta[0]=theta0#
D[0]=0.5*rho*v[0]*v[0]*S*CD#
for i in range(0,N-1):
    vx[i+1]=vx[i]-dt/m*(D[i]*np.cos(theta[i]))#
    vy[i+1]=vy[i]+dt/m*(-D[i]*np.sin(theta[i]))-g*dt#
    x[i+1]=x[i]+dt*vx[i+1]#
    y[i+1]=y[i]+dt*vy[i+1]#
    if vx[i+1]!=0:
        theta[i+1]=np.arctan(vy[i+1]/vx[i+1])#
    else:
        if vy[i+1]>=0:
            theta[i+1]=np.pi/2#
        else:
            theta[i+1]=-np.pi/2#
    v[i+1]=np.sqrt(vx[i+1]*vx[i+1]+vy[i+1]*vy[i+1])#
    D[i+1]=0.5*rho*v[i+1]*v[i+1]*S*CD#
theta=theta*180/np.pi#
E=0.5*m*v*v
if theta0==0:
    print('Disparo horizontal')
else:
    print('Disparo a',np.format_float_positional(theta0*180/np.pi,precision=2),'grados')
    print('Altura máxima =',np.format_float_positional(np.max(y),precision=2),'m')
print('Alcance horizontal =',np.format_float_positional(x[N-1],precision=2),'m')
print('Altura final =',np.format_float_positional(y[N-1],precision=2),'m')
print('Velocidad final =',np.format_float_positional(v[N-1],precision=2),'m/s')
print('Energía inicial =',np.format_float_positional(0.5*m*v[0]*v[0],precision=2),'J')
print('Energía final =',np.format_float_positional(0.5*m*v[N-1]*v[N-1],precision=2),'J')
print('Pérdida de energía =',np.format_float_positional((1-v[N-1]*v[N-1]/(v[0]*v[0]))*100,precision=2),'%')
apunte_x=np.array([0,x[N-1]])
apunte_y=np.array([y0,y0+x[N-1]*np.tan(theta0)])
#Gráficas:
plt.figure(1)
plt.grid(True,'both','both')
plt.title('Trayectoria')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.plot(x,y,'b')
plt.plot(apunte_x,apunte_y,'y--')
plt.legend(['Trayectoria','Línea de apunte'])
#
#plt.figure(2)
#plt.plot(t,vx,'b')
#plt.plot(t,vy,'r')
#plt.plot(t,v,'g')
#plt.grid(True,'both','both')
#plt.title('Velocidad')
#plt.xlabel('Tiempo [s]')
#plt.ylabel('Velocidad [m/s]')
#plt.legend(['v_x','v_y','|v|'])
#
#plt.figure(3)
#plt.plot(t,theta,'b')
#plt.grid(True,'both','both')
#plt.title('Dirección')
#plt.xlabel('t [s]')
#plt.ylabel('Ángulo inclinación [grados]')
#
#plt.figure(4)
#plt.plot(t,D,'r')
#plt.grid(True,'both','both')
#plt.title('Fuerza de arrastre')
#plt.xlabel('Tiempo [s]')
#plt.ylabel('Arrastre [N]')
#
#plt.figure(5)
#plt.plot(x,v,'r')
#plt.grid(True,'both','both')
#plt.title('Velocidad vs. distancia horizontal')
#plt.xlabel('Recorrido horizontal [m]')
#plt.ylabel('Velocidad [m/s]')
#
#plt.figure(6)
#plt.plot(x,E,'b')
#plt.grid(True,'both','both')
#plt.title('Energía cinética vs. distancia horizontal')
#plt.xlabel('Recorrido horizontal [m]')
#plt.ylabel('Energía cinética [J]')
#
#plt.figure(7)
#plt.plot(t,y,'b')
#plt.grid(True,'both','both')
#plt.title('Altura vs. tiempo')
#plt.xlabel('Tiempo [s]')
#plt.ylabel('Altura [m]')