# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:46:44 2022

@author: Greg Krueper

Calculation methods used to generate data for the three-phase interferometer.
In current implementation, gives results for the "three phase sequential" case in appendix D
"""
import numpy as np
import scipy as sp
import csv

# 3 phase interferometer matrix with 12 modes, copy/pasted from Mathematica file
def mat(p1, p2, p3, T):
    return [[(-((-1.+T)**5.)*((T**0.5)*(np.cos((p1+((11.*p2)+p3)))))), ((-1.+T)**5.)*((T**0.5)*(np.sin((p1+((11.*p2)+p3))))), ((1.-T)**5.5)*(np.cos(((11.*p2)+p3))), (-((1.-T)**5.5)*(np.sin(((11.*p2)+p3)))), ((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.cos((2.*((5.*p2)+p3))))), (-((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.sin((2.*((5.*p2)+p3)))))), ((-1.+T)**4.)*((T**0.5)*(np.cos((p1+((9.*p2)+p3))))), (-((-1.+T)**4.)*((T**0.5)*(np.sin((p1+((9.*p2)+p3)))))), (-((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.cos((2.*((4.*p2)+p3)))))), ((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.sin((2.*((4.*p2)+p3))))), (-((-1.+T)**3.)*((T**0.5)*(np.cos((p1+((7.*p2)+p3)))))), ((-1.+T)**3.)*((T**0.5)*(np.sin((p1+((7.*p2)+p3))))), (((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.cos((2.*((3.*p2)+p3))))), (-(((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.sin((2.*((3.*p2)+p3)))))), (((-1.+T)**2))*((T**0.5)*(np.cos((p1+((5.*p2)+p3))))), (-(((-1.+T)**2))*((T**0.5)*(np.sin((p1+((5.*p2)+p3)))))), ((1.-T)**1.5)*((T**0.5)*(np.cos((2.*((2.*p2)+p3))))), (-1.+T)*((((-(-1.+T)*T))**0.5)*(np.sin((2.*((2.*p2)+p3))))), (-(-1.+T)*((T**0.5)*(np.cos((p1+((3.*p2)+p3)))))), (-1.+T)*((T**0.5)*(np.sin((p1+((3.*p2)+p3))))), (((-(-1.+T)*T))**0.5)*(np.cos((2.*(p2+p3)))), (-(((-(-1.+T)*T))**0.5)*(np.sin((2.*(p2+p3))))), (T**0.5)*(np.cos((p1+(p2+p3)))), (-(T**0.5)*(np.sin((p1+(p2+p3)))))], [(-((-1.+T)**5.)*((T**0.5)*(np.sin((p1+((11.*p2)+p3)))))), (-((-1.+T)**5.)*((T**0.5)*(np.cos((p1+((11.*p2)+p3)))))), ((1.-T)**5.5)*(np.sin(((11.*p2)+p3))), ((1.-T)**5.5)*(np.cos(((11.*p2)+p3))), ((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.sin((2.*((5.*p2)+p3))))), ((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.cos((2.*((5.*p2)+p3))))), ((-1.+T)**4.)*((T**0.5)*(np.sin((p1+((9.*p2)+p3))))), ((-1.+T)**4.)*((T**0.5)*(np.cos((p1+((9.*p2)+p3))))), (-((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.sin((2.*((4.*p2)+p3)))))), (-((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.cos((2.*((4.*p2)+p3)))))), (-((-1.+T)**3.)*((T**0.5)*(np.sin((p1+((7.*p2)+p3)))))), (-((-1.+T)**3.)*((T**0.5)*(np.cos((p1+((7.*p2)+p3)))))), (((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.sin((2.*((3.*p2)+p3))))), (((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.cos((2.*((3.*p2)+p3))))), (((-1.+T)**2))*((T**0.5)*(np.sin((p1+((5.*p2)+p3))))), (((-1.+T)**2))*((T**0.5)*(np.cos((p1+((5.*p2)+p3))))), ((1.-T)**1.5)*((T**0.5)*(np.sin((2.*((2.*p2)+p3))))), ((1.-T)**1.5)*((T**0.5)*(np.cos((2.*((2.*p2)+p3))))), (-(-1.+T)*((T**0.5)*(np.sin((p1+((3.*p2)+p3)))))), (-(-1.+T)*((T**0.5)*(np.cos((p1+((3.*p2)+p3)))))), (((-(-1.+T)*T))**0.5)*(np.sin((2.*(p2+p3)))), (((-(-1.+T)*T))**0.5)*(np.cos((2.*(p2+p3)))), (T**0.5)*(np.sin((p1+(p2+p3)))), (T**0.5)*(np.cos((p1+(p2+p3))))], [(-((1.-T)**0.5)*(np.cos((2.*p1)))), ((1.-T)**0.5)*(np.sin((2.*p1))), (T**0.5)*(np.cos(p1)), (-(T**0.5)*(np.sin(p1))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [-2.*(((1.-T)**0.5)*((np.cos(p1))*(np.sin(p1)))), (-((1.-T)**0.5)*(np.cos((2.*p1)))), (T**0.5)*(np.sin(p1)), (T**0.5)*(np.cos(p1)), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), (-(((-(-1.+T)*T))**0.5)*(np.cos((p2+p3)))), (((-(-1.+T)*T))**0.5)*(np.sin((p2+p3))), ((1.-T)**0.5)*(np.cos((2.*p3))), -2.*(((1.-T)**0.5)*((np.cos(p3))*(np.sin(p3)))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), (-(((-(-1.+T)*T))**0.5)*(np.sin((p2+p3)))), (-(((-(-1.+T)*T))**0.5)*(np.cos((p2+p3)))), ((1.-T)**0.5)*(np.sin((2.*p3))), ((1.-T)**0.5)*(np.cos((2.*p3))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2))))), (-1.+T)*((T**0.5)*(np.cos((p1+(2.*p2))))), (-(-1.+T)*((T**0.5)*(np.sin((p1+(2.*p2)))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p1))), -2.*(((1.-T)**0.5)*((np.cos(p1))*(np.sin(p1)))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), (-1.+T)*((T**0.5)*(np.sin((p1+(2.*p2))))), (-1.+T)*((T**0.5)*(np.cos((p1+(2.*p2))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p1))), ((1.-T)**0.5)*(np.cos((2.*p1))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-1.+T)*((((-(-1.+T)*T))**0.5)*(np.cos(((3.*p2)+p3)))), ((1.-T)**1.5)*((T**0.5)*(np.sin(((3.*p2)+p3)))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p3))), -2.*(((1.-T)**0.5)*((np.cos(p3))*(np.sin(p3)))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-1.+T)*((((-(-1.+T)*T))**0.5)*(np.sin(((3.*p2)+p3)))), (-1.+T)*((((-(-1.+T)*T))**0.5)*(np.cos(((3.*p2)+p3)))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p3))), ((1.-T)**0.5)*(np.cos((2.*p3))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), ((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2)))))), (-(((-1.+T)**2))*((T**0.5)*(np.cos((p1+(4.*p2)))))), (((-1.+T)**2))*((T**0.5)*(np.sin((p1+(4.*p2))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p1))), -2.*(((1.-T)**0.5)*((np.cos(p1))*(np.sin(p1)))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2))))))), (-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), (-(((-1.+T)**2))*((T**0.5)*(np.sin((p1+(4.*p2)))))), (-(((-1.+T)**2))*((T**0.5)*(np.cos((p1+(4.*p2)))))), (-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p1))), ((1.-T)**0.5)*(np.cos((2.*p1))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3))))), (-(((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.cos(((5.*p2)+p3))))), (((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.sin(((5.*p2)+p3)))), (-((1.-T)**1.5)*(T*(np.cos((2.*((2.*p2)+p3)))))), ((1.-T)**1.5)*(T*(np.sin((2.*((2.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p3))), -2.*(((1.-T)**0.5)*((np.cos(p3))*(np.sin(p3)))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-(((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (-(((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.sin(((5.*p2)+p3))))), (-(((-1.+T)**2))*((((-(-1.+T)*T))**0.5)*(np.cos(((5.*p2)+p3))))), (-((1.-T)**1.5)*(T*(np.sin((2.*((2.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.cos((2.*((2.*p2)+p3)))))), (-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p3))), ((1.-T)**0.5)*(np.cos((2.*p3))), 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], [(-((1.-T)**2.5)*(T*(np.cos((2.*(p1+(3.*p2))))))), ((1.-T)**2.5)*(T*(np.sin((2.*(p1+(3.*p2)))))), ((-1.+T)**3.)*((T**0.5)*(np.cos((p1+(6.*p2))))), (-((-1.+T)**3.)*((T**0.5)*(np.sin((p1+(6.*p2)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3))))), (-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), ((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2)))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p1))), -2.*(((1.-T)**0.5)*((np.cos(p1))*(np.sin(p1)))), 0., 0., 0., 0., 0., 0., 0., 0.], [(-((1.-T)**2.5)*(T*(np.sin((2.*(p1+(3.*p2))))))), (-((1.-T)**2.5)*(T*(np.cos((2.*(p1+(3.*p2))))))), ((-1.+T)**3.)*((T**0.5)*(np.sin((p1+(6.*p2))))), ((-1.+T)**3.)*((T**0.5)*(np.cos((p1+(6.*p2))))), (-(((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2))))))), (-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), (-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p1))), ((1.-T)**0.5)*(np.cos((2.*p1))), 0., 0., 0., 0., 0., 0., 0., 0.], [((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), (-((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3)))))), ((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.cos(((7.*p2)+p3)))), (-((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.sin(((7.*p2)+p3))))), (-((1.-T)**2.5)*(T*(np.cos((2.*((3.*p2)+p3)))))), ((1.-T)**2.5)*(T*(np.sin((2.*((3.*p2)+p3))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3))))), (-((1.-T)**1.5)*(T*(np.cos((2.*((2.*p2)+p3)))))), ((1.-T)**1.5)*(T*(np.sin((2.*((2.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p3))), -2.*(((1.-T)**0.5)*((np.cos(p3))*(np.sin(p3)))), 0., 0., 0., 0., 0., 0.], [((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3))))), ((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), ((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.sin(((7.*p2)+p3)))), ((-1.+T)**3.)*((((-(-1.+T)*T))**0.5)*(np.cos(((7.*p2)+p3)))), (-((1.-T)**2.5)*(T*(np.sin((2.*((3.*p2)+p3)))))), (-((1.-T)**2.5)*(T*(np.cos((2.*((3.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.sin((2.*((2.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.cos((2.*((2.*p2)+p3)))))), (-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p3))), ((1.-T)**0.5)*(np.cos((2.*p3))), 0., 0., 0., 0., 0., 0.], [(-((1.-T)**3.5)*(T*(np.cos((2.*(p1+(4.*p2))))))), ((1.-T)**3.5)*(T*(np.sin((2.*(p1+(4.*p2)))))), (-((-1.+T)**4.)*((T**0.5)*(np.cos((p1+(8.*p2)))))), ((-1.+T)**4.)*((T**0.5)*(np.sin((p1+(8.*p2))))), ((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), (-((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3)))))), (-((1.-T)**2.5)*(T*(np.cos((2.*(p1+(3.*p2))))))), ((1.-T)**2.5)*(T*(np.sin((2.*(p1+(3.*p2)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3))))), (-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), ((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2)))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p1))), -2.*(((1.-T)**0.5)*((np.cos(p1))*(np.sin(p1)))), 0., 0., 0., 0.], [(-((1.-T)**3.5)*(T*(np.sin((2.*(p1+(4.*p2))))))), (-((1.-T)**3.5)*(T*(np.cos((2.*(p1+(4.*p2))))))), (-((-1.+T)**4.)*((T**0.5)*(np.sin((p1+(8.*p2)))))), (-((-1.+T)**4.)*((T**0.5)*(np.cos((p1+(8.*p2)))))), ((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3))))), ((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), (-((1.-T)**2.5)*(T*(np.sin((2.*(p1+(3.*p2))))))), (-((1.-T)**2.5)*(T*(np.cos((2.*(p1+(3.*p2))))))), (-(((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2))))))), (-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), (-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p1))), ((1.-T)**0.5)*(np.cos((2.*p1))), 0., 0., 0., 0.], [(-((-1.+T)**4.)*(T*(np.cos((p1+((9.*p2)+p3)))))), ((-1.+T)**4.)*(T*(np.sin((p1+((9.*p2)+p3))))), (-((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.cos(((9.*p2)+p3))))), ((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.sin(((9.*p2)+p3)))), (-((1.-T)**3.5)*(T*(np.cos((2.*((4.*p2)+p3)))))), ((1.-T)**3.5)*(T*(np.sin((2.*((4.*p2)+p3))))), ((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), (-((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3)))))), (-((1.-T)**2.5)*(T*(np.cos((2.*((3.*p2)+p3)))))), ((1.-T)**2.5)*(T*(np.sin((2.*((3.*p2)+p3))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3))))), (-((1.-T)**1.5)*(T*(np.cos((2.*((2.*p2)+p3)))))), ((1.-T)**1.5)*(T*(np.sin((2.*((2.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p3))), -2.*(((1.-T)**0.5)*((np.cos(p3))*(np.sin(p3)))), 0., 0.], [(-((-1.+T)**4.)*(T*(np.sin((p1+((9.*p2)+p3)))))), (-((-1.+T)**4.)*(T*(np.cos((p1+((9.*p2)+p3)))))), (-((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.sin(((9.*p2)+p3))))), (-((-1.+T)**4.)*((((-(-1.+T)*T))**0.5)*(np.cos(((9.*p2)+p3))))), (-((1.-T)**3.5)*(T*(np.sin((2.*((4.*p2)+p3)))))), (-((1.-T)**3.5)*(T*(np.cos((2.*((4.*p2)+p3)))))), ((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3))))), ((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), (-((1.-T)**2.5)*(T*(np.sin((2.*((3.*p2)+p3)))))), (-((1.-T)**2.5)*(T*(np.cos((2.*((3.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.sin((2.*((2.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.cos((2.*((2.*p2)+p3)))))), (-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p2+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p2+p3)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p3))), ((1.-T)**0.5)*(np.cos((2.*p3))), 0., 0.], [(-((1.-T)**4.5)*(T*(np.cos((2.*(p1+(5.*p2))))))), ((1.-T)**4.5)*(T*(np.sin((2.*(p1+(5.*p2)))))), ((-1.+T)**5.)*((T**0.5)*(np.cos((p1+(10.*p2))))), (-((-1.+T)**5.)*((T**0.5)*(np.sin((p1+(10.*p2)))))), (-((-1.+T)**4.)*(T*(np.cos((p1+((9.*p2)+p3)))))), ((-1.+T)**4.)*(T*(np.sin((p1+((9.*p2)+p3))))), (-((1.-T)**3.5)*(T*(np.cos((2.*(p1+(4.*p2))))))), ((1.-T)**3.5)*(T*(np.sin((2.*(p1+(4.*p2)))))), ((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), (-((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3)))))), (-((1.-T)**2.5)*(T*(np.cos((2.*(p1+(3.*p2))))))), ((1.-T)**2.5)*(T*(np.sin((2.*(p1+(3.*p2)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3))))), (-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), ((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2)))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-(-1.+T)*(T*(np.sin((p1+((3.*p2)+p3)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), ((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2))))), (-T*(np.cos((p1+(p2+p3))))), T*(np.sin((p1+(p2+p3)))), ((1.-T)**0.5)*(np.cos((2.*p1))), -2.*(((1.-T)**0.5)*((np.cos(p1))*(np.sin(p1))))], [(-((1.-T)**4.5)*(T*(np.sin((2.*(p1+(5.*p2))))))), (-((1.-T)**4.5)*(T*(np.cos((2.*(p1+(5.*p2))))))), ((-1.+T)**5.)*((T**0.5)*(np.sin((p1+(10.*p2))))), ((-1.+T)**5.)*((T**0.5)*(np.cos((p1+(10.*p2))))), (-((-1.+T)**4.)*(T*(np.sin((p1+((9.*p2)+p3)))))), (-((-1.+T)**4.)*(T*(np.cos((p1+((9.*p2)+p3)))))), (-((1.-T)**3.5)*(T*(np.sin((2.*(p1+(4.*p2))))))), (-((1.-T)**3.5)*(T*(np.cos((2.*(p1+(4.*p2))))))), ((-1.+T)**3.)*(T*(np.sin((p1+((7.*p2)+p3))))), ((-1.+T)**3.)*(T*(np.cos((p1+((7.*p2)+p3))))), (-((1.-T)**2.5)*(T*(np.sin((2.*(p1+(3.*p2))))))), (-((1.-T)**2.5)*(T*(np.cos((2.*(p1+(3.*p2))))))), (-(((-1.+T)**2))*(T*(np.sin((p1+((5.*p2)+p3)))))), (-(((-1.+T)**2))*(T*(np.cos((p1+((5.*p2)+p3)))))), (-((1.-T)**1.5)*(T*(np.sin((2.*(p1+(2.*p2))))))), (-((1.-T)**1.5)*(T*(np.cos((2.*(p1+(2.*p2))))))), (-1.+T)*(T*(np.sin((p1+((3.*p2)+p3))))), (-1.+T)*(T*(np.cos((p1+((3.*p2)+p3))))), (-((1.-T)**0.5)*(T*(np.sin((2.*(p1+p2)))))), (-((1.-T)**0.5)*(T*(np.cos((2.*(p1+p2)))))), (-T*(np.sin((p1+(p2+p3))))), (-T*(np.cos((p1+(p2+p3))))), ((1.-T)**0.5)*(np.sin((2.*p1))), ((1.-T)**0.5)*(np.cos((2.*p1)))]]

# mean vector for input modes. a is constant, th is an array for each angle,
# modes are the list of input modes used, m is the total number of modes
# th and modes must be of the same length
def meanvec(a, th, modes, m):
    ans = np.zeros(2*m);
    for i in range(0,len(modes)):
        ans[2*(modes[i]-1)] = a * np.cos(th[i])
        ans[2*(modes[i]-1)+1] = a * np.sin(th[i])
    return ans

# single-mode squeezing matrix with squeezing strength r and squeezing angle ts
def squeeze(r, ts) : 
    ans = [[(np.cosh(r))+((np.cos(ts))*(np.sinh(r))), (np.sin(ts))*(np.sinh(r))], [(np.sin(ts))*(np.sinh(r)), (np.cosh(r))-((np.cos(ts))*(np.sinh(r)))]]
    return np.matmul(ans, ans)

# general squeezing matrix of strength r, angle list for each mode ts, in a list of modes, with total modes m
def squeezemat(r, ts, modes, m):
    ans = np.identity(2*m)
    for i in range(0, len(modes)):
        if i <= m:
            ans[2*(modes[i]-1):2*modes[i], 2*(modes[i]-1):2*modes[i]] = squeeze(r, ts[i])
    return ans

# loss matrix for mean vector from truncation of a reflector of transmission T
# in mode n of total modes m. Usage: d --> loss1.d, c --> loss1.c.np.transpose(loss1)
def loss1(T, n, m):
    ans = np.identity(2*m)
    ans[2*(n-1):2*n, 2*(n-1):2*n] = np.sqrt((1-T))*ans[2*(n-1):2*n, 2*(n-1):2*n]
    return ans

# loss matrix for covariance matrix. Usage: c --> loss1.c.transpose(loss1) + loss2
# adds thermal noise to the state in proportion to loss
def loss2(T, n, m):
    ans = np.zeros([2*m, 2*m])
    ans[2*(n-1):2*n, 2*(n-1):2*n] = [[1-T,0],[0,1-T]]
    return ans

# m: total number of modes
# modes: list of modes used as input
# matparams: list of parameters used in the unitary matrix. Format [{phi}, T]
# angles_c: angles of the mean vector. List is same length as modes
# angles_s: angles of the squeezed modes in the covariance matrix. List is same length as modes
# phases: integer number of phases to measure in matparams. Should be equal to len({phi}) from matparams
# r: squeezing strength, positive number. 0 --> classical light.
# loss: T/F do we use truncation loss (1-T) on mode 1, default False
def FIMat2(m, modes_c, modes_s, matparams, angles_c, angles_s, phases, r, loss=False):
    a = 1000
    dp = 0.001 # phase increment for calculating derivatives
    d = meanvec(a, angles_c, modes_c, m) # define inputs
    c = squeezemat(r, angles_s, modes_s, m)
    lo1 = loss1(matparams[-1],1,m) # loss matrices on mode 1, if needed for truncation
    lo2 = loss2(matparams[-1],1,m)
    unitary = mat(matparams[0], matparams[1], matparams[2], matparams[3]) # get unitary given values for T and phases
    dout = np.matmul(unitary, d) # output vector
    cout = np.matmul(np.matmul(unitary, c), np.transpose(unitary)) # output covar
    if loss:
        dout = np.matmul(lo1,dout)
        cout = np.matmul(np.matmul(lo1, cout), lo1) + lo2
    invc = np.linalg.inv(cout) # inverse of covariance
    dd = np.zeros((phases, 2*m)) # set up arrays for derivatives
    #dc = np.zeros((phases, 2*m, 2*m)) # calculating second term in Fisher information is unnecessary because it's negligible when |a|>>1
    
    for i in range(0,phases): # compute each unique derivative
        matparams[i] = matparams[i]-dp # offset one phase
        dmat = mat(matparams[0], matparams[1], matparams[2], matparams[3]) # get new unitary matrix
        matparams[i] = matparams[i]+dp # arrays pass by reference; restore for next run
        d2 = np.matmul(dmat, d) # get new outputs
        #c2 = np.matmul(np.matmul(dmat, c), np.transpose(dmat))
        if loss:
            d2 = np.matmul(lo1, d2)
            #c2 = np.matmul(np.matmul(lo1, c2), lo1) + lo2
        dd[i] = (dout-d2)/dp # take derivative & store
        #dc[i] = (cout-c2)/dp
    ans = np.zeros((phases, phases)) # create Fisher information matrix
    for i in range(0,phases):
        k = 0
        while k <= i: # calculate all unique elements
            inf1 = 2*np.matmul(np.matmul(np.transpose(dd[i]),invc), dd[k])
            #inf2 = 0.25*np.trace(np.matmul(np.matmul(np.matmul(invc, dc[i]), invc), dc[k]))
            inf2 = 0
            ans[i,k] = inf1 + inf2 # calculate Fisher Info
            k = k+1
    for i in range(0,phases): # fill in non-unique elements
        k = i+1
        while k < phases: # fill upper triangle of matrix
            ans[i,k] = ans[k,i]
            k = k+1
    
    return ans

# debugging method to return the output state given matrix parameters and initial state
def CVoutput(m, modes_c, modes_s, matparams, angles_c, angles_s, phases, r, loss=False):
    a = 1000
    #dp = 0.001 # phase increment for calculating derivatives
    d = meanvec(a, angles_c, modes_c, m) # define inputs
    c = squeezemat(r, angles_s, modes_s, m)
    lo1 = loss1(matparams[-1],1,m) # loss matrices on mode 1, if needed for truncation
    lo2 = loss2(matparams[-1],1,m)
    unitary = mat(matparams[0], matparams[1], matparams[2], matparams[3]) # get unitary given values for T and phases
    dout = np.matmul(unitary, d) # output vector
    cout = np.matmul(np.matmul(unitary, c), np.transpose(unitary)) # output covar
    if loss:
        dout = np.matmul(lo1,dout)
        cout = np.matmul(np.matmul(lo1, cout), lo1) + lo2
    #invc = np.linalg.inv(cout) # inverse of covariance
    #dd = np.zeros((phases, 2*m)) # set up arrays for derivatives
    return [np.round(dout,2), np.round(cout,2)]

# computes the quantum Cramer-Rao bound from a Fisher information matrix, giving the summed phase variance of all parameters
def QCRB(fimat) : 
    return np.trace(np.linalg.inv(fimat))

# cost function for optimization given one displaced squeezed state
def costfunc1s(x, T, r):
    return QCRB(FIMat2(12, [1], [1], [x[0],x[1],x[2], T], [0], [x[3]], 3, r, True))

# cost function for optimization given two displaced squeezed states
def costfunc2s(x, T, r):
    return QCRB(FIMat2(12, [1,3], [1,3], [x[0],x[1],x[2], T], [0, x[3]], [x[4], x[5]], 3, r, True))

# cost function for optimization given three displaced squeezed states
def costfunc3s(x, T, r):
    return QCRB(FIMat2(12, [1, 3, 4], [1, 3, 4], [x[0],x[1],x[2], T], [0, x[3], x[4]], [x[5], x[6], x[7]], 3, r, True))

# cost function for optimization given four displaced squeezed states
def costfunc4s(x, T, r):
    return QCRB(FIMat2(12, [1, 3, 4, 5], [1, 3, 4, 5], [x[0],x[1],x[2], T], [0, x[3], x[4], x[5]], [x[6], x[7], x[8], x[9]], 3, r, True))

# cost function for optimization given five displaced squeezed states
def costfunc5s(x, T, r):
    return QCRB(FIMat2(12, [1, 3, 4, 5, 6], [1, 3, 4, 5, 6], [x[0],x[1],x[2], T], [0, x[3], x[4], x[5], x[6]], [x[7], x[8], x[9], x[10],x[11]], 3, r, True))

# cost function for optimization given one coherent state
def costfunc1c(x, T, r):
    return QCRB(FIMat2(12, [1], [1], [x[0],x[1],x[2], T], [0], [x[3]], 3, r, True))

# cost function for optimization given two coherent states
def costfunc2c(x, T, r):
    return QCRB(FIMat2(12, [1, 3], [1], [x[0],x[1],x[2], T], [0, x[3]], [x[4]], 3, r, True))

# cost function for optimization given three coherent states
def costfunc3c(x, T, r):
    return QCRB(FIMat2(12, [1, 3, 4], [1], [x[0],x[1],x[2], T], [0, x[3], x[4]], [x[5]], 3, r, True))

# cost function for optimization given four coherent states
def costfunc4c(x, T, r):
    return QCRB(FIMat2(12, [1, 3, 4, 5], [1], [x[0],x[1],x[2], T], [0, x[3], x[4], x[5]], [x[6]], 3, r, True))

# cost function for optimization given five coherent states
def costfunc5c(x, T, r):
    return QCRB(FIMat2(12, [1, 3, 4, 5, 6], [1], [x[0],x[1],x[2], T], [0, x[3], x[4], x[5], x[6]], [x[7]], 3, r, True))
########## 2 input optimization
# bnds = ((0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi))
# res1c = []
# #t = [0.9]
# t = np.arange(0.01, 1, 0.01)
# if __name__ == '__main__':
#     for i in t:
#         res = sp.optimize.differential_evolution(costfunc1, bnds, args=(i,0),disp=False, popsize=50, polish=True, workers=5, atol=1e-7)
#         x0 = res.x
#         res1c.append([i, x0[0], x0[1],x0[2], x0[3], res.fun])
#         print(res.fun)
#     print('done')
    # header = ['T','phi1','phi2','phi3','theta_s1', 'QCRB']
    # with open('opt1c.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     #writer.writerow(header)
    #     writer.writerows(res1c)
     
############### 15 input optimization
bnds = ((0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi),(0, 2*np.pi))
res1c = []
t = np.arange(0.01, 1, 0.01) # range of transmission values to test
if __name__ == '__main__':
    for i in t: # replace cost function as needed
        res = sp.optimize.differential_evolution(costfunc2c, bnds, args=(i,0),popsize=50, disp=False, polish=True, workers=5, atol=1e-9)
        x1 = res.x
        res1c.append([i, x1[0], x1[1],x1[2], x1[3], x1[4], res.fun]) # record end sensitivity and optimized values
        print(round(i,2), res.nfev, res.nit, res.fun) # evaluation statistics
    print('done')

#     header = ['T','phi1','phi2','phi3','theta_s1', 'QCRB']
    with open('opt_3p_c2.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        #writer.writerow(header)
        writer.writerows(res1c)