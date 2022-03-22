"""
@author: cadecastro.com
«Todos amamos a Python, y a su glorioso régimen»
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#VALORES DE ENTRADA:
xf=80 #[m] Distancia horizontal final de interés
E0=2.9 #[J] Energía inicial de disparo
theta0=-np.arctan(25/80)*180/np.pi #[grados] Ángulo de disparo
y0=30.0 #[m] Altura inicial
tf=2.5000#[s] Tiempo final simulación
dt=0.0001#[s] Paso de tiempo
m=4/3*np.pi*(0.0045/2)**3*7800#[kg] Masa del proyectil
S=np.pi/4*0.0045**2#[m^2] Área frontal proyectil
CD=0.500#Coeficiente de arrastre medio
rho=0.91#[kg/m^3] Densidad del aire
g=9.81#[m/s^2] Magnitud aceleración gravedad

#SOLUCIÓN:
print('-------------------  ANÁLISIS TRAYECTORIA PROYECTIL  -------------------')
print('               Carlos Armando De Castro  - cadecastro.com               ')
print('________________________________________________________________________')
print('                                          ')

#Función de interpolación:
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

#Solución numérica método de Euler:
v0=np.sqrt(2*E0/m)#[m/s] Velocidad inicial de disparo
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
#Línea de apunte:
apunte_x=np.array([0,x[N-1]])
apunte_y=np.array([y0,y0+x[N-1]*np.tan(theta0)])

#Tabla Resumen de la simulación:
tabla1=pd.DataFrame(data=[np.format_float_positional(theta0*180/np.pi,precision=2),np.format_float_positional(np.max(y),precision=2),
                          np.format_float_positional(xf,precision=2),np.format_float_positional(y0+xf*np.tan(theta0),precision=2),
                          np.format_float_positional(interpolacion_lineal(x,y,xf),precision=2),np.format_float_positional(v0,precision=2),
                          np.format_float_positional(interpolacion_lineal(x,v,xf),precision=2),np.format_float_positional(E0,precision=2),
                          np.format_float_positional(interpolacion_lineal(x,E,xf),precision=2),np.format_float_positional((1-interpolacion_lineal(x,E,xf)/E0)*100,precision=2)],
                    index=['Ángulo de disparo [grados]','Altura máxima [m]','Alcance horizontal [m]','Altura de apunte [m]','Altura final [m]',
                           'Velocidad inicial [m/s]','Velocidad final [m/s]','Energía cinética inicial [J]','Energía cinética final [J]',
                           'Pérdida de energía cinética [%]']).rename(columns={0:'Valor'})

print('                                                    ')
print('                 RESUMEN SIMULACIÓN                 ')
print('____________________________________________________')
print(tabla1)

#Tabla de valores según distancia:
X=np.linspace(0,xf,11)
yt=np.zeros(len(X))
Et=np.zeros(len(X))
vt=np.zeros(len(X))
for i in range(0,len(X)):
  yt[i]=interpolacion_lineal(x,y,X[i])
  vt[i]=interpolacion_lineal(x,v,X[i])
  Et[i]=interpolacion_lineal(x,E,X[i])

tabla2=pd.DataFrame(data=[X,yt,vt,Et]).transpose().rename(columns={0:'Recorrido horizontal [m]',
                                                                         1:'Altura [m]',2:'Velocidad [m/s]',3:'Energía cinética [J]'}).set_index('Recorrido horizontal [m]')

print('                                                        ')
print('________________________________________________________________________')
print('                 TABLA DE VALORES EN ALGUNAS DISTANCIAS                 ')
print('________________________________________________________________________')
print(tabla2)

#Gráficas:
plt.figure(1,figsize=(12,12))
plt.subplot(211)
plt.grid()
plt.title('Trayectoria del proyectil')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.plot(x,y,color='blue')
plt.plot(apunte_x,apunte_y,color='gold',linestyle='--')
plt.legend(['Trayectoria','Línea de apunte'])
plt.ylim(np.min(y),1.1*np.max(y))
plt.xlim(0,xf)
plt.subplot(212)
plt.plot(x,E,color='red')
plt.grid(True,'both','both')
plt.title('Energía cinética vs. distancia horizontal')
plt.xlabel('Recorrido horizontal [m] - cadecastro.com')
plt.ylabel('Energía cinética [J]')
plt.xlim(0,xf)

plt.figure(2,figsize=(12,12))
plt.subplot(211)
plt.plot(x,vx,color='blue')
plt.plot(x,vy,color='violet')
plt.plot(x,v,color='lime')
plt.grid(True,'both','both')
plt.title('cadecastro.com',loc='right')
plt.title('Velocidad')
plt.xlabel('Recorrido horizontal [m]')
plt.ylabel('Velocidad [m/s]')
plt.legend(['v_x','v_y','|v|'])
plt.xlim(0,xf)
plt.subplot(212)
plt.plot(x,theta,color='green')
plt.grid(True,'both','both')
plt.title('Dirección del proyectil')
plt.xlabel('Recorrido horizontal [m] - cadecastro.com')
plt.ylabel('Ángulo inclinación [grados]')
plt.xlim(0,xf)

plt.figure(3,figsize=(12,6))
plt.plot(x,D,color='cyan')
plt.grid(True,'both','both')
plt.title('Arrastre aerodinámico')
plt.title('cadecastro.com',loc='right')
plt.xlabel('Recorrido horizontal [m]')
plt.ylabel('Arrastre [N]')
plt.xlim(0,xf)

plt.figure(4,figsize=(12,6))
plt.plot(t,y,color='magenta')
plt.grid(True,'both','both')
plt.title('Altura vs. tiempo')
plt.title('cadecastro.com',loc='right')
plt.xlabel('Tiempo [s]')
plt.ylabel('Altura [m]')
