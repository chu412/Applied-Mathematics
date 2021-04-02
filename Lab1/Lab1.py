from math import *
def y(x):
    try:
        y = sin(x) - log(x*x) - 1 
        return sin(x) - log(x*x) - 1 
    except:
        return None
    
    
def dichotomy_method(a,b,eps):
    itt = 0
    calculations = 0
    
    while(b-a>=eps):
        x0 = (a+b)/2
        itt+=1 
        calculations +=2
        y1 = y(x0 - eps/2)
        y2 = y(x0 + eps/2)
        
        if(y1<=y2):
            b = x0
        else:
            a = x0

    return [a,itt,calculations]

def golden_ratio(a,b,eps):
    itt = 0
    calculations = 2
    c = a + (b-a)*( 3 - 5**0.5)/2
    d = b - (b-a)*( 3 - 5**0.5)/2
    y1 = y(c)
    y2 = y(d)
    
    while(b-a>=eps):
        itt+=1 
        # print(a," ",b)
        
        if(y1>y2):
            # print("!")
            a = c 
            c = d
            y1=y2
            d = b - (b-a)*( 3 - 5**0.5 )/2 
            calculations +=1 
            y2 = y(d)
        else:
            b = d 
            d = c
            y2 = y1
            c = a + (b-a)*(3 - 5**0.5 )/2
            calculations +=1 
            y1 = y(c)
            
    return [c,itt,calculations]    

def Bine(n):
    return ((((1 + 5**0.5)/2)**n) - (((1 - 5**0.5)/2)**n))/(5**0.5)
    
def Fibonacci(a,b,eps):
    n = int((b-a)/(10*eps) + 0.5)
        
    itt = 0
    calculations = 2
    #воспользуемся формулой Бинэ для определения примерного значения числа Фибоначчи
    x1 = a + Bine(n-2)/Bine(n)*(b-a)
    x2 = b - Bine(n-2)/Bine(n)*(b-a)
    
    y1 = y(x1)
    y2 = y(x2)
    
    # print(Bine(n-2))
    
    while(n>itt + 3):
        x1 = a + Bine(n - itt - 2)/Bine(n - itt)*(b-a)
        x2 = b -  Bine(n - itt - 2)/Bine(n - itt)*(b-a)
        
        
        itt+=1 
        calculations +=2
        
        if(y1>y2):
            a = x1 
            # x2 = a + Bine(n - itt - 2)/Bine(n - itt)*(b-a)
            calculations +=1
            
            y2 = y(x2)
        else:
            b = x2 
            # x1 = b -  Bine(n - itt - 2)/Bine(n - itt)*(b-a)
            calculations +=1 
            
            y1 = y(x1)
            
            
    return [a,itt,calculations] 
    
def parabola(a,b,eps):
    x1 = a 
    x2 = (a+b)/2 
    x3 = b 
    
    calculations = 3
    itt = 0
    f1 = y(x1)
    f2 = y(x2)
    f3 = y(x3)
    
    x2 = (x1+x3)/2
    
    #ищем нужные точки пока не выполниться равенство f1 >= f2 <= f3
    while(x3-x1>=eps and not (f1 >= f2 <= f3)):
        x2 = (x1+x3)/2
        itt+=1 
        calculations +=2
        f1 = y(x2 - eps/2)
        f3 = y(x2 + eps/2)
        
        if(f1 >= f2 <= f3):
            break
        
        if(f1<=f3):
            x3 = x2
        else:
            x1 = x2
    
    calculations +=1 
    x2 = (x1+x3)/2
    f2 = y(x2)
    
    a0 = f1
    a1 = (f2-f1)/(x2-x1)
    a2 = ((f3 - f1)/(x3-x1) - (f2 - f1)/(x2-x1))/(x3-x2)
    x_d = (x1+x2 - a1/a2)/2
    
    
    while(abs(x_d - x2)>=eps):
        # print(x1," ",x2," ",x3)
        itt +=1 
        
        a0 = f1
        a1 = (f2-f1)/(x2-x1)
        a2 = ((f3 - f1)/(x3-x1) - (f2 - f1)/(x2-x1))/(x3-x2)
        
        x_d = (x1+x2 - a1/a2)/2 
        
        calculations +=1        
        f_d = y(x_d)
        
        if(f_d>=f2):
            
            x1 = x_d
            f1 = f_d
        else:
            # print("!")
            x1 = x2
            f1 = f2
            x2 = x_d
            

    return [x2,itt,calculations]
    
def H_parab(x1,x2,x3,y1,y2,y3):
    try:
        d = (x1 - x2)*(x1 - x3)*(x2 - x3)
        A = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / d
        B = (x3^2 * (y1 - y2) + x2^2 * (y3 - y1) + x1^2 * (y2 - y3)) / d
        C = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / d
        
        return -b /(2*a)
    except:
        return None
    
def Brenta(a,b,eps):
    r = (3 - 5**0.5)/2
    x=w=v = a - r*(b-a)
    d_c = d_p = b - a
    
    itt = 0
    calculations = 0
    u = None 
    while(max(x -a , b - x) > eps):
        itt+=1 
        g = d_p/2 
        d_p = d_c
        # print(x," ",w," ",u)
        
        u = H_parab(x,w,u,y(x),y(w),y(u))
        
        if(u == None or u<a or u>b or abs(u-x)>g):
            if(x<(a+b)/2):
                u=x + r*(b-x)
                d_p = b-x
            else:
                u=x - r*(x - a)
                d_p = x - a 
        
            
        d_c = abs(u - x)
        
        calculations +=2
        f_u = y(u)
        f_x = y(x)
        
        
        if(f_u>f_x):
            if(u<x):
                a = u 
            else:
                b = u
                
            calculations +=1 
            f_w = y(w)
            
            if(f_u<=f_w or w==x):
                v = w 
                w = u 
            elif(f_u <= f_w or v == x or v == w):
                v = u 
        else:
            if(u<x):
                b = x 
            else:
                a = x 
            v = w 
            w = x 
            x = u      
    return [u,itt,calculations]
        
        

print(dichotomy_method(0,1,0.005))

#золотое сечение не будет работать верно если при первом приближении окажется f(c)>f(d) но x_min<c . Как вариант такое может быть если правильно подобрать интервал при y = sin x
print(golden_ratio(0,1,0.005)) 
print(Fibonacci(0,1,0.005))
print(parabola(0.01,1,0.005))

# # не способен правильно вычилисть при монотонной функиии
# print(Brenta(0.01,1,0.005))

print("")
print(dichotomy_method(4,6,0.005))
print(golden_ratio(4,6,0.005)) 
print(Fibonacci(4,6,0.005))
print(parabola(4,6,0.005))
print(Brenta(4,6,0.005))





