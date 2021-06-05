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

def goldenSlice(func, argsL1, argsR1, eps):
    argsL = argsL1.copy()
    argsR = argsR1.copy()

    a = D(0)
    b = D(1e5)
    x0 = a + D(0.5) * (D(3) - D(math.sqrt(5))) * (b - a)
    x1 = b - x0 + a

    while math.fabs(b - a) > D(eps):
        Left = argsL + x0 * argsR
        Right = argsL + x1 * argsR

        if  func(Left) < func(Right):
            b = x1
        else:
            a = x0
        x1 = x0
        x0 = b + a - x1
    return (a + b)/D(2)

def conjugateGradient(f1, args, e):
    f = lambda a: eval(f1)
    stop = False
    iter = 0
    p = -myGradient(f, args)

    grad = p

    while not stop:
        iter += 1

        alpha = goldenSlice(f, args, p, e)
        args = args + alpha * p

        grad1 = -myGradient(f, args)

        if iter % 2 == 0:
            beta = 0    
        else:
            beta = inner(grad1, grad1) / inner(grad, grad)

        p = grad1 + beta * p
        
        grad = grad1.copy()

        if inner(grad, grad) <= e:
            stop = True
    return iter

def conjugateGradient3D(f, args, e):
    stop = False
    iter = 0

    args0 = args.copy()
    p = -myGradient(f, args)

    grad = p
    
    vertex = [[]]
    vertex.append([])

    while not stop:
        iter += 1

        alpha = goldenSlice(f, args, p, e)
        args = args + alpha * p

        vertex[0].append(float(args0[0]))
        vertex[0].append(float(args[0]))

        vertex[1].append(float(args0[1]))
        vertex[1].append(float(args[1]))

        args0 = args.copy()
        grad1 = -myGradient(f, args)

        if iter % 2 == 0:
            beta = 0    
        else:
            beta = inner(grad1, grad1) / inner(grad, grad)

        p = grad1 + beta * p
        
        grad = grad1.copy()

        if inner(grad, grad) <= e:
            stop = True
    return vertex