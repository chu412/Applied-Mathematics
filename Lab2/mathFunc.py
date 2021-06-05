import decimal

def D(x):
    return decimal.Decimal(x)

def PD(f, args, i):
    d = D(0.00000001)
    args_local = args.copy()
    args_local[i] += d
    return (f(args_local) - f(args))/d

def PPD(func, args, i):
    d = D(0.000000001)
    args_local = args.copy()
    args_local[i] += d
    x1 = D(func(args_local))
    args_local[i] -= D(2)*d
    x2 = D(func(args_local))
    args_local[i] += d
    x3 = D(func(args_local))

    return (x1 - 2*x3 + x2)/(d**D(2))

def deltaArgs(args0, args1):
    sum = D(0)
    i = 0

    while i < len(args0):
        sum += (args0[i]-args1[i])**D(2)

        i += 1
    return sum

def inner(args1, args2):
    sum = D(0)

    for (x, y) in zip(args1, args2):
        sum += x * y
    return sum

def sqGrad(f, args):
    sum = D(0)

    i = 0

    while i < len(args):
        sum += PD(f, args, i)**2
        i += 1
    return sum

def myGradient(func, args): 
    argsPD = args.copy()

    i = 0
    while i < len(argsPD):
        argsPD[i] = PD(func, argsPD, i)
        i += 1
    return argsPD

def getFunc(n, k):
    k1 = k
    k1 /= n
    z_str = ' '

    for i in range(n):
        z_str += '(a[' + str(i) + ']**D('+ str(k1) +'))'

        if i != n - 1:
            z_str += ' + '
    return z_str