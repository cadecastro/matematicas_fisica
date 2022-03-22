#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 11:02:50 2022

Autor: Carlos Armando De Castro (cadecastro.com)
"""
import numpy as np

def interpolacion_lineal(x,y,xi):
    if xi>np.max(x) or xi<np.min(x):
        print('Valor a interpolar fuera del dominio.')
        return None
    else:
        for j in range(1,len(x)):
            if x[j]>x[j-1]:
                if xi<=x[j] and xi>=x[j-1]:
                    yi=y[j-1]+(y[j]-y[j-1])/(x[j]-x[j-1])*(xi-x[j-1])
                    return yi
            else:
                print('Valores de X no están en orden ascendente')
                return None