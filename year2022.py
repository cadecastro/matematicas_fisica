#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:33:14 2021
SERIE PARA EL AÑO 2022
Asesorías en Matemáticas
Física e Ingeniería (tutor.cadecastro.com)
"""
import matplotlib.pyplot as plt
import numpy as np
N=int(input('N = '))
n=np.linspace(0,N,N+1)
S=np.zeros(N+1)
S[0]=1
for i in range(0,len(n)-1):
    S[i+1]=S[i]+np.power(2021/2022,n[i+1])
print('Suma acumulada =',np.format_float_positional(S[len(S)-1],precision=1))
plt.figure(1)
plt.fill_between(n,S,color='blue')
plt.xlabel('n - tutor.cadecastro.com')
plt.ylabel('Suma acumulada')
plt.xlim(0,N)
plt.ylim(0,2022)
plt.title('FELIZ AÑO NUEVO',loc='left')
plt.title('Asesorías en Matemáticas, Física e Ingeniería',loc='right')