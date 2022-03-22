#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:32:12 2022
Autor: Carlos Armando De Castro (cadecastro.com)
"""

def interpolacion_lagrange(x,y,xi):
    yi=0
    N=len(x)
    for i in range(0,N):
        L=1
        for j in range(0,N):
            if j!=i:
                L=L*(xi-x[j])/(x[i]-x[j])
        yi=yi+L*y[i]
    return yi