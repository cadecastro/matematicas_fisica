#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:58:41 2021

@author: cadecastro.com
"""

import numpy as np
import matplotlib.pyplot as plt
N=int(input('Número de puntos, menor que 1000, N='))
if N<=1000:
    n=np.linspace(0,N,N+1)
    F=np.zeros(N+1)
    C=np.ones(N+1)
    F[1]=1
    for i in range(2,N+1):
        F[i]=F[i-1]+F[i-2]
        C[i]=F[i]/F[i-1]
    plt.figure(1)
    plt.bar(n,F,width=0.8,bottom=None,align='center',data=None,color='b')
    plt.title('Sucesión de Fibonacci')
    plt.xlabel('n')
    plt.ylabel('Fn')
    plt.grid(True,'both','both')
    plt.figure(2)
    plt.plot(n,C,'bo')
    plt.title('Razón entre números sucesivos de Fibonacci')
    plt.xlabel('n')
    plt.ylabel('Cn')
    plt.grid(True,'both','both')
    print('Aproximación razón aúrea con N=',N,'es:',C[N])
else:
    print('Valor excede el máximo de 1000.')