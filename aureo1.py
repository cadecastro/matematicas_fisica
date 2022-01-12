#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:32:11 2021
tutor.cadecastro.com
"""
import numpy as np
import matplotlib.pyplot as plt
n=int(input('Número de puntos, n = '))
C=float(input('Factor que multiplica al ángulo, C = '))
if n<=1000:
    for r in range(0,n):
        x=r*np.cos(r*(1+np.sqrt(5))/2*C); 
        y=r*np.sin(r*(1+np.sqrt(5))/2*C);
        plt.plot(x,y,'b.')
    plt.axis(False)
    plt.axis('square')
    plt.title('tutor.cadecastro.com')
else:
    print('Cantidad excede máximo de 1000.')