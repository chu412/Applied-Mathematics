import numpy
import math
import pylab
import time
from random import randint
from sympy import *
import keyboard
import decimal
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D

from mathFunc import *

def goldenSlice(func, argsL1, argsR1, eps):
    iter = 0
    t1 = D(0.381966)
    t2 = D(1) - t1
    argsL = argsL1.copy()
    argsR = argsR1.copy()

    x1 = argsL + (argsR - argsL) * t1
    x2 = argsL + (argsR - argsL) * t2
    
    f1 = func(x1 - D(eps))
    f2 = func(x2 + D(eps))
    print(argsL, argsR)
    i = 0
    delta = D(0)
    while i < len(argsR):
        delta += (argsL[i] - argsR[i])**D(2)
        i += 1

    while delta > D(eps**2):
        if f1 < f2:
            argsR = x2
            x2 = x1
            f2 = f1
            x1 = argsL + (argsR - argsL) * t1
            f1 = func(x1)
        else:
            argsL = x1
            x1 = x2
            f1 = f2
            x2 = argsL + (argsR - argsL) * t2
            f2 = func(x2)
        i = 0
        delta = D(0)

        while i < len(argsR):

            delta += (argsL[i] - argsR[i])**D(2)
            i += 1
    return (argsL + argsR) / D(2)

def steepestDespect(f1, args, e):
    f = lambda a: eval(f1)
    iter = 0
    stop = False
    
    args0 = args.copy()
    args1 = args0.copy()

    while not stop:
        args1 = goldenSlice(f, args0, -myGradient(f, args0), e)

        i = 0
        delta = D(0)
        while i < len(args0):
            delta += (args1[i] - args0[i])**2
            i += 1
            
        if delta < D(e**2) and math.fabs(f(args1) - f(args0)) < D(e):
            stop = True
        args0 = args1.copy()
        print(iter)
    return iter

def steepestDespect3D(f, args, e):
    iter = 0
    stop = False
    
    args0 = args.copy()
    args1 = args0.copy()

    vertex = [[]]
    vertex.append([])

    while not stop:
        args1 = goldenSlice(f, args0, -myGradient(f, args0), e)

        i = 0
        delta = D(0)
        while i < len(args0):
            delta += (args1[i] - args0[i])**2
            i += 1

        vertex[0].append(float(args0[0]))
        vertex[0].append(float(args1[0]))

        vertex[1].append(float(args0[1]))
        vertex[1].append(float(args1[1]))

        if delta < D(e**2) and math.fabs(f(args1) - f(args0)) < D(e):
            stop = True
        args0 = args1.copy()
    return vertex