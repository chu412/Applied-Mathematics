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
from newton import *
from defGradient import *
from steepestDespect import *
from conjugateGradient import *
from conjugateDirection import *

def T(f, n, k):
    args = numpy.array([D(5)])
    i = 1
    while i < n:
        args = numpy.append(args, D(5))
        i += 1
    return newton(f, args, 0.01)


def makeData(func):
    x = numpy.arange(-40, 40, 0.5)
    y = numpy.arange(-60, 40, 0.5)
    xgrid, ygrid = numpy.meshgrid(x, y)

    zgrid = func([xgrid, ygrid])
    return xgrid, ygrid, zgrid

def init(func):
    x, y, z = makeData(func)

    pylab.ion()

    fig, ax = pylab.subplots()

    ax.contourf(x, y, z, levels=20)
    ax.axis([-40, 40, -60, 40])
    ax.set_ylabel('y', fontsize = 15)
    ax.set_xlabel('x', fontsize = 15)

    return (ax, fig)

def newtonGraph(func):
    ax, fig = init(func)

    start = numpy.array([D(-38), D(20)])

    arr = newton3D(func, start, D(0.001))
    ax.plot(arr[0], arr[1], c='red')

    pylab.ioff()
    pylab.show()

def defaultGraph(func):
    ax, fig = init(func)

    start = numpy.array([D(-38), D(20)])

    arr = defGradient3D(func, start, D(0.0001))
    ax.plot(arr[0], arr[1], c='red')

    pylab.ioff()
    pylab.show()


def steepestDespectGraph(func):
    ax, fig = init(func)

    start = numpy.array([D(-38), D(20)])

    arr = steepestDespect3D(func, start, D(0.0001))
    ax.plot(arr[0], arr[1], c='red')

    pylab.ioff()
    pylab.show()

def conjugateGradientGraph(func):
    ax, fig = init(func)

    start = numpy.array([D(-38), D(20)])

    arr = conjugateGradient3D(func, start, D(0.0001))
    ax.plot(arr[0], arr[1], c='red')

    pylab.ioff()
    pylab.show()

def conjugateDirectionGraph(func):
    ax, fig = init(func)

    start = numpy.array([D(-38), D(20)])

    arr = conjugateDirection3D(func, start, D(0.0001))
    ax.plot(arr[0], arr[1], c='red')

    pylab.ioff()
    pylab.show()