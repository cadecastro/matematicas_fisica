#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:42:25 2021

@author: cdc
"""
import numpy as np
import matplotlib.pyplot as plt
#VALORES DE ENTRADA: (unidades varían según problema, verificar
#consistencia)
V0=100##Volumen inicial de solvente en el tanque
A0=10##Cantidad inicial de soluto
Qin=4##Caudal de ingreso al tanque
Qout=5##Caudal de salida del tanque
Cin=0.40##Concentración de ingreso al tanque
tf=100##Tiempo total de simulación
dt=0.1##Intervalo de tiempo
#SOLUCIÓN:
N=int(tf/dt+1)
t=np.linspace(0,tf,N)
dQ=Qin-Qout#
if dQ==0:
   A=np.zeros(N)#
   C=np.zeros(N)#
   for i in range(0,N):
      A[i]=V0*Cin+(A0-V0*Cin)*np.exp(-Qout/V0*t[i])#
      C[i]=A[i]/V0#
   
   plt.subplot(211)
   plt.plot(t,A,'b-')
   plt.grid(True,'both','both')
   plt.title('Cantidad de soluto en el tanque')
   plt.xlabel('t')
   plt.ylabel('A')
   plt.subplot(212)
   plt.plot(t,C,'b-')
   plt.grid(True,'both','both')
   plt.title('Concentración de soluto en el tanque')
   plt.xlabel('t')
   plt.ylabel('C')
else:
   V=np.zeros(N)#
   A=np.zeros(N)#
   C=np.zeros(N)#
   for i in range(0,N):
       V[i]=V0+dQ*t[i]#
       A[i]=Cin*V[i]+np.power(V[i],-Qout/dQ)*(A0*np.power(V0,Qout/dQ)-Cin*np.power(V0,Qin/dQ))#
       C[i]=A[i]/V[i]#

   plt.figure(1)
   plt.plot(t,A,'b-')
   plt.grid(True,'both','both')
   plt.title('Cantidad de soluto en el tanque')
   plt.xlabel('t')
   plt.ylabel('A')
   plt.figure(2)
   plt.plot(t,C,'b-')
   plt.grid(True,'both','both')
   plt.title('Concentración de soluto en el tanque')
   plt.xlabel('t')
   plt.ylabel('C')
   plt.figure(3)
   plt.plot(t,V,'b-')
   plt.grid(True,'both','both')
   plt.title('Volumen en el tanque')
   plt.xlabel('t')
   plt.ylabel('V')