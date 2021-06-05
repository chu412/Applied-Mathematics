import numpy
import math
import pylab
import time
from sympy import *
import keyboard
from scipy.optimize import minimize_scalar
import decimal
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D

from mathFunc import *

def newton(f1, args, e):
    f = lambda a: eval(f1)
    stop = False
    iter = 0

    args0 = args.copy()

    while stop == False:
        i = 0

        while i < len(args):
            args[i] = args0[i] - PD(f, args0, i)/PPD(f, args0, i)
            i += 1
        if deltaArgs(args0, args) < D(e**2):
            stop = True

        args0 = args.copy()
        iter += 1
    return iter

def newton3D(f, args, e):
    stop = False

    args0 = args.copy()

    vertex = [[]]
    vertex.append([])

    while stop == False:
        i = 0
        while i < len(args):
            args[i] = args0[i] - PD(f, args0, i)/PPD(f, args0, i)
            i += 1

        if deltaArgs(args0, args) < D(e**2):
            stop = True
        vertex[0].append(float(args0[0]))
        vertex[0].append(float(args[0]))

        vertex[1].append(float(args0[1]))
        vertex[1].append(float(args[1]))

        args0 = args.copy()
    return vertex