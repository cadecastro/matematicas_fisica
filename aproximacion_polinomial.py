#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:21:39 2022

Autor: Carlos Armando De Castro (cadecastro.com)
"""
import numpy as np
import matplotlib.pyplot as plt
def aproximacion_polinomial(x,y,n):
    p=np.polyfit(x,y,n)
    y_pred=np.polyval(p,x)
    y_m=np.mean(y)
    SST=0
    SSR=0
    for i in range(0,len(y)):
        SSR=SSR+(y[i]-y_pred[i])**2
        SST=SST+(y[i]-y_m)**2
    R2=1-SSR/SST
    R2s=str(np.format_float_positional(R2,precision=3))
    
    xp=float(input('Valor de x para predecir ='))
    yp=np.polyval(p,xp)
    print('Valor aproximado yp =',yp)
    
    plt.figure(1,figsize=(12,6))
    plt.plot(x,y,'bo')
    plt.plot(x,y_pred,color='red')
    plt.grid()
    plt.title('Aproximación polinomio grado '+str(n)+' - R²='+R2s,size=12,loc='center')
    plt.title('cadecastro.com',size=10,loc='right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Datos','Polinomio'])
    
    return R2,y_pred,yp