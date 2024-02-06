# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:18:10 2023

@author: Greg Krueper

Simple script that takes the predicted Fisher information for a cascaded interferometer with n phases
and optimizes the value of transmission for each reflector for maximum average sensitivity
"""

import numpy as np
import scipy as sp
import csv

# starting Fisher information element, eq. 22
def element(T, n):
    return 2*T**(n-1)

# implements eq. 23, 24
def FIMatrix(T, n):
    a = np.zeros([n,n])
    a[n-1, n-1] = element(T, n)
    ind = np.arange(n-1,0,-1)
    for i in ind:
        a[i-1,i-1] = a[i, i] - 8*T**(2*i-1) + 8*T**(2*i-2)
    for i in range(0,n):
        for j in range(0,i):
            a[i,j] = a[i,i]
            a[j,i] = a[i,i]    
    return a

# implements eq. 25
def FIMatrix2(T, n):
    a = FIMatrix(T,n)
    return a + np.flipud(np.fliplr(a))

# gets quantum Cramer-Rao bound from the Fisher information matrix
def QCRB(mat):
    return np.trace(np.linalg.inv(mat))

#implements the cost function given a transmission value x[0] and n phases
def costfunc(x,n):
    return QCRB(FIMatrix2(x[0],n))

N = 100
a = []
bnds = [(0.01, 0.9999)] # matrices are singular at 0 and 1
for i in range(1,N+1): # for each number of phases
    res = sp.optimize.minimize(costfunc, 0.9, args=(i),bounds=bnds)
    a.append([i, res.x[0]]) # record optimized values
    
with open('opt_reflectivities_3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    #writer.writerow(header)
    writer.writerows(a)
