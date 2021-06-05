from threading import Thread

from gradFunc import *

f = lambda a:  3 * a[0] ** 2 + a[1] ** 2 - a[0] * a[1] - 4 * a[0]
#f = lambda a:  a[0] ** 2.5 + a[1] ** 2.5  
print("1 - Default Grad\n2 - Steepest Despect\n3 - Conjugate Gradient\n4 - Conjugate Direction\n5 - Newton\nInput: ")
choose_grad = input()

if choose_grad == "1":
    defaultGraph(f)
elif choose_grad == "2":
    steepestDespectGraph(f)
elif choose_grad == "3":
    conjugateGradientGraph(f)
elif choose_grad == "4":
    conjugateDirectionGraph(f)
elif choose_grad == "5":
    newtonGraph(f)