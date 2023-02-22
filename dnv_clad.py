# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:26:11 2023

@author: Groth
"""
import os
import numpy as np
import matplotlib.pyplot as plt


os.chdir('C:/Users/Groth/Desktop/scopes 2/dnv')

E=207e9     
ni=0.3       
fy_bs = 450e6   
fy_c  = 450e6  
D=0.3048
#Pc_dnv=np.zeros((4,5))

dt=np.array([7.5,15,20,30])

f0=np.array([0.005,0.01,0.02,0.03,0.04])    

Pc_dnv=np.zeros((len(dt),len(f0)))
t_c=np.array([3e-3])

for j in range(len(f0)):
    for i in range(len(dt)):
        t=D/dt[i]
        alpha_el=1-1.85*(t_c/t)+1.7*(t_c/t)**2 
        Pel_c=((2*E*(t/D)**3)/(1-ni**2))*alpha_el
        Pp_c=(fy_bs*2*t/D)+(fy_c*2*t_c/(D-2*t))
        A=Pel_c
        B=Pp_c
        C= Pel_c*Pp_c*f0[j]*(D/t)
        R=[1, -A, -(B**2+C) ,A*B**2]
        a=np.roots(R)
        Pc_dnv[i,j]=a[2]



fig, ax1 = plt.subplots(figsize=(7,3))
ax1.plot(dt, Pc_dnv,color='darkblue', linestyle='dotted', linewidth=1,marker='s', markersize=5, label='Friction Coefficient')
ax1.set_ylabel('colpase capacity')
ax1.set_xlabel('d/t ratio')

fig, ax2 = plt.subplots(figsize=(7,3))
ax2.plot(dt, Pc_dnv[:,i],color='darkblue', linestyle='dotted', linewidth=3,marker='s', markersize=3, label='Friction Coefficient')
ax2.set_ylabel('colpase capacity')
ax2.set_xlabel('d/t ratio')

def Pc_dnv():
    fig, ax1 = plt.subplots(figsize=(7,3))
    ax1.plot(dt, Pc_dnv,color='darkblue', linestyle='dotted', linewidth=1,marker='s', markersize=5, label='Friction Coefficient')
    ax1.set_ylabel('colpase capacity')
    ax1.set_xlabel('d/t ratio')
    
    



    
    
    
    
    