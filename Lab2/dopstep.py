from sympy import *
 
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
 
# f = 3 * x**2 + y**2 - x*y - 4 * x
# f= 3 * x^2 + y^2 -x*y -4x
def f(x,y):
    return 3 * x**2 + y**2 - x*y - 4 * x
 
def gradX(x,y):
    return  6*x - y - 4
def gradY(x,y):
    return 2*y -x 
 
def gradient(x,y,f):
    # # First partial derivative with respect to x
    # fpx = diff(f, x)
 
    # # First partial derivative with respect to y
    # fpy = diff(f, y)
 
    # # Gradient
    # grad = [fpx,fpy]
 
    # Data
    # theta = -38  #x
    # theta1 = 20 #y
    # alpha0 = .3
    lamda = 1.0
    delta = .45
    iterations = 0
    check = 0
    eps = 1/1000000
    printData = True
    maxIterations = 1000
 
    # while abs(temptheta-theta) < precision and abs(temptheta1-theta1) < precision:
    #     alpha = alpha0
    #     temptheta = theta - alpha*N(fpx.subs(x,theta).subs(y,theta1)).evalf()
    #     temptheta1 = theta1 - alpha*N(fpy.subs(y,theta1)).subs(x,theta).evalf()
 
    #     #If the number of iterations goes up too much, maybe theta (and/or theta1)
    #     #is diverging! Let's stop the loop and try to understand.
    #     iterations += 1
    #     if iterations > maxIterations:
    #         print("Too many iterations. Adjust alpha and make sure that the function is convex!")
    #         printData = False
    #         break
 
    #     #If the value of theta changes less of a certain amount, our goal is met.
    #     #Đoạn này em đang không biết sửa điều kiện
    #     if abs(temptheta-theta) < precision and abs(temptheta1-theta1) < precision:
    #         # alpha=alpha*delta
    #         # temptheta = theta - alpha*N(fpx.subs(x,theta).subs(y,theta1)).evalf()
    #         # temptheta1 = theta1 - alpha*N(fpy.subs(y,theta1)).subs(x,theta).evalf()
    #         break
 
    #     #Simultaneous update
    #     theta = temptheta
    #     theta1 = temptheta1
 
    # if printData:
    #     print("The function "+str(f)+" converges to a minimum")
    #     print("Number of iterations:",iterations,sep=" ")
    #     print("theta (x0) =",temptheta,sep=" ")
    #     print("theta1 (y0) =",temptheta1,sep=" ")
    fv = f(x,y)
    it = 0
    while lamda > eps:
        it += 1
        gx = gradX(x,y)
        gy = gradY(x,y)
        nx = x - lamda * gx
        ny = y - lamda * gy
        nf = f(nx,ny)
        if (nf <= (fv-0.5 * lamda*(gx**2 + gy**2))):
            x = nx
            y = ny
            fv = nf
        else:
            lamda = lamda * delta
 
    print(str(x) + " " + str(y) +" " + str(it)+ "\n")
    return 
 
gradient(-38,20,f)