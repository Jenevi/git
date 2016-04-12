# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:35:21 2016

@author: Iv
"""

'''
Программа для расчета энергии системы зарядов расположенных на окружности
'''

import numpy as np

e = 1.6*10**(-19)
epsilon_0 = 8.85*10**(-12)
pi = 3.14
n = 2 #количество точек
r = 1*10**(0) #радиус сферы

x = np.zeros(n)
y = np.zeros(n)

#определяем координаты точек на окружности
for i in range(n):
    x[i] = np.cos(i*2*pi/n)*r
    y[i] = np.sin(i*2*pi/n)*r
    
su = 0
for i in range(n):
    for j in range(n):
        if i!=j:
            su = su + 1/(np.sqrt(x[i]*x[i] + y[i]*y[i]))
            
print 0.5*su*(1/(4*pi*(epsilon_0)))*(e)**2    

print 5+5