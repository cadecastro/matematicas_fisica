#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 19:54:36 2021

@author: cadecastro.com
"""

import numpy as np
import matplotlib.pyplot as plt
E=120 #[V] Voltaje DC fuente
R=5e6 #[Ohm] Resistencia total
C=1.2e-9 #[F] Capacitancia total
N=100 #Puntos a graficar
#SOLUCIÓN:
tau=R*C #[s] Constante de tiempo
t=np.linspace(0,7*tau,N)
Imax=E/R #[A] Corriente máxima
Qmax=C*E #[C] Carga máxima almacenada
Qcarga=Qmax*(1-np.exp(-t/tau))
Qdescarga=Qmax*np.exp(-t/tau)
I=Imax*np.exp(-t/tau)
#Resultados:
print('Cte. de tiempo tau= ',np.format_float_scientific(tau,precision=4),'s')
print('Carga máxima Qmax= ',np.format_float_scientific(Qmax,precision=4),'C')
print('Corriente máxima Imax= ',np.format_float_scientific(Imax,precision=4),'A')
#Gráficas:
plt.figure(1)
plt.plot(t,Qcarga,'r')
plt.plot(t,Qdescarga,'b')
plt.legend(['Proc. de carga','Proc. de descarga'])
plt.grid(True,'both','both')
plt.title('Carga en el capacitor')
plt.xlabel('Tiempo [s]')
plt.ylabel('Carga almacenada [C]')

plt.figure(2)
plt.plot(t,I,'r')
plt.grid(True,'both','both')
plt.title('Corriente')
plt.xlabel('Tiempo [s]')
plt.ylabel('Corriente [A]')