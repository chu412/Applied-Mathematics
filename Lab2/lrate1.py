from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

f = 3 * x**2 + y**2 - x*y - 4 * x

# First partial derivative with respect to x
fpx = f.diff(x)

# First partial derivative with respect to y
fpy = f.diff(y)

# Gradient
grad = [fpx,fpy]

# Data
theta = -38  #x
theta1 = 20 #y
alpha = .3
iterations = 0
check = 0
precision = 1/1000000
printData = True
maxIterations = 1000

while True:
    temptheta = theta - alpha*N(fpx.subs(x,theta).subs(y,theta1)).evalf()
    temptheta1 = theta1 - alpha*N(fpy.subs(y,theta1)).subs(x,theta).evalf()

    #If the number of iterations goes up too much, maybe theta (and/or theta1)
    #is diverging! Let's stop the loop and try to understand.
    iterations += 1
    if iterations > maxIterations:
        print("Too many iterations. Adjust alpha and make sure that the function is convex!")
        printData = False
        break

    #If the value of theta changes less of a certain amount, our goal is met.
    if abs(temptheta-theta) < precision and abs(temptheta1-theta1) < precision:
        break

    #Simultaneous update
    theta = temptheta
    theta1 = temptheta1

if printData:
    print("The function "+str(f)+" converges to a minimum")
    print("Number of iterations:",iterations,sep=" ")
    print("theta (x0) =",temptheta,sep=" ")
    print("theta1 (y0) =",temptheta1,sep=" ")
    
    
# Output
#
# The function x**2 - 2*x*y + y**2 converges to a minimum
# Number of iterations: 401
# theta (x0) = 525.000023717248
# theta1 (y0) = 524.999976282752