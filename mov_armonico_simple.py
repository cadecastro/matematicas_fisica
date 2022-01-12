#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:32:11 2021
tutor.cadecastro.com
"""
import numpy as np
import matplotlib.pyplot as plt
print("Movimiento armónico simple")
m=float(input("Masa m [kg]="))
k=float(input("Constante resorte k [N/m]="))
x0=float(input("Posición inicial x0 [m]="))
v0=float(input("Velocidad inicial v0 [m]="))
N=int(input("Número de puntos a graficar ="))
w0=np.sqrt(k/m)
T=2*np.pi/w0
A=np.sqrt(x0*x0+(v0/w0)*(v0/w0))
E=0.5*k*A*A
print("RESULTADOS:")
print("Frecuencia natural w0=",np.format_float_positional(w0,precision=3),'rad/s')
print("Período T=",np.format_float_positional(T,precision=3),'s')
print("Amplitud A=",np.format_float_positional(A,precision=3),'m')
print("Energía total=",np.format_float_positional(E,precision=3),'J')
t=np.linspace(0,T,num=N)
x=np.zeros(N)
v=np.zeros(N)
a=np.zeros(N)
for i in range(0,N):
    x[i]=x0*np.cos(w0*t[i])+v0/w0*np.sin(w0*t[i])
    v[i]=-w0*x0*np.sin(w0*t[i])+v0*np.cos(w0*t[i])
    a[i]=-w0*w0*x[i]
plt.figure(1)
plt.plot(t,x)
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.title("Movimiento armónico simple")
plt.grid(True,'both','both')
plt.figure(2)
plt.plot(t,v)
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.grid(True,'both','both')
plt.figure(3)
plt.plot(t,a)
plt.xlabel("Tiempo [s]")
plt.ylabel("Aceleración [m/s²]")
plt.grid(True,'both','both')
plt.show()