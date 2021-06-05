import numpy
import math
import numpy.ma as ma
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

def findM(func, a1, b1, eps):
    a = D(-1e3)
    b = D(1e3)
    
    while math.fabs(b - a) > D(eps):
        y1 = func(a1 + a * b1)
        y2 = func(a1 + b * b1)

        c = (a + b) / D(2)
        
        if y1 < y2:
            b = c
        else:
            a = c
    return (a + b) / D(2)

def conjugateDirection(f1, args, e):
    f = lambda a: eval(f1)
    s = numpy.zeros((len(args), len(args)), dtype=numpy.dtype(decimal.Decimal))

    i, j = 0, 0

    while j < len(args):
        while i < len(args):
            if i == j:
                s[i][j] = D(1)
            else:
                s[i][j] = D(0)
            i += 1
        j += 1
        i = 0
    iter = 0



    while sqGrad(f, args) > D(e)**D(2):
        iter += 1

        i = 2
        while i < len(args):
            lbm = findM(f, args, s[i], e)
            args = args + lbm*s[i]
            i += 1

        lbm = findM(f, args, s[0], e)
        args1 = args + lbm*s[0]

        lbm = findM(f, args1, s[1], e)

        args2 = args1 + lbm*s[1]

        lbm = findM(f, args2, s[0], e)
        args3 = args2 + lbm*s[0]

        s[0] = args3 - args1
        args = args3
    return iter

def conjugateDirection3D(f, args, e):
    s = numpy.zeros((len(args), len(args)), dtype=numpy.dtype(decimal.Decimal))

    i, j = 0, 0

    while j < len(args):
        while i < len(args):
            if i == j:
                s[i][j] = D(1)
            else:
                s[i][j] = D(0)
            i += 1
        j += 1
        i = 0
    
    vertex = [[]]
    vertex.append([])

    while sqGrad(f, args) > D(e)**D(2):
        i = 2
        while i < len(args):
            lbm = findM(f, args, s[i], e)
            args = args + lbm*s[i]
            i += 1

        lbm = findM(f, args, s[0], e)
        args1 = args + lbm*s[0]

        lbm = findM(f, args1, s[1], e)

        args2 = args1 + lbm*s[1]

        lbm = findM(f, args2, s[0], e)
        args3 = args2 + lbm*s[0]

        s[0] = args3 - args1

        vertex[0].append(float(args[0]))
        vertex[0].append(float(args3[0]))

        vertex[1].append(float(args[1]))
        vertex[1].append(float(args3[1]))

        args = args3
    return vertex