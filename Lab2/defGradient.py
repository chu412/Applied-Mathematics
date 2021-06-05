import numpy
import math
import pylab
import time
from random import randint
from sympy import *
import keyboard
from decimal import Decimal
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D

from mathFunc import *

def defGradient(f1, args0, e):
    f = lambda a: eval(f1)
    iter = 0
    lbm = D(0.01)
    stop = False
    args1 = args0.copy()
    args2 = args0.copy()
    while not stop:
        i = 0
        while i < len(args2):
            args2[i] = args1[i] - PD(f, args1, i) * lbm
            i += 1
        i = 0
        delta = D(0)
        while i < len(args2):
            delta += (args1[i] - args2[i])**2
            i += 1
            
        if delta < D(e**2) and math.fabs(f(args1) - f(args2)) < D(e):
            stop = True
        args1 = args2.copy()
        iter += 1
    return iter

def defGradient3D(f, args0, e):
    lbm = D(0.01)
    stop = False
    args1 = args0.copy()
    args2 = args0.copy()

    vertex = [[]]
    vertex.append([])
    while not stop:
        i = 0
        while i < len(args2):
            args2[i] = args1[i] - PD(f, args1, i) * lbm
            i += 1
        i = 0
        delta = D(0)
        while i < len(args2):
            delta += (args1[i] - args2[i])**2
            i += 1
        
        vertex[0].append(float(args1[0]))
        vertex[0].append(float(args2[0]))

        vertex[1].append(float(args1[1]))
        vertex[1].append(float(args2[1]))

        if delta < D(e**2) and math.fabs(f(args1) - f(args2)) < D(e):
            stop = True
        args1 = args2.copy()
    return vertex