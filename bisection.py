import math
import sympy as sy
from texttable import Texttable
import numpy as np

x = sy.symbols("x")

def CreateFunction():  ## step 1 - choose a polynom
    ##fast example   x**4+x**3-3*x**2
    funcInput = input("Enter a function: ")
    func = sy.sympify(funcInput)
    return func


def MaxIterations(a, b, error):
    max = math.ceil(-(math.log(error / (b - a))) / math.log(2))
    return max


def Bisection_Method(f, boundary, epsilon):
    a = boundary[0]
    b = boundary[1]
    count = 0
    table=Texttable()
    rows=[["i","a","b","c","f(a)","f(b)","f(c)"]]
    print()
    print("The bisection table is:")
    while (b - a > epsilon and count < MaxIterations(a, b, epsilon)):
        c = (a + b) / 2  # calc middle
        if (f.subs(x, a) * f.subs(x, c) > 0):
            a = c  # ignore the left half
        else:
            b = c  # ignore the right half
        rows.append([count,round(a,6),round(b,6),round(c,6),round(f.subs(x, a), 6),round(f.subs(x, b), 6),round(f.subs(x, c), 6)])
        count = count + 1
    table.add_rows(rows)
    print(table.draw())
    return c


def StartIterating(function, boundry, epsilon):
    difference = 0.1
    a = boundry[0]
    b = boundry[1]
    count = 0
    prev = 0
    current = 0
    roots = []
    sus = []  # suspicious - may be roots
    table = Texttable()
    rows = [['f(x)', 'x', 'i']]
    print(f'The difference is {difference}')
    print()
    while a <= b+0.0001:
        count = count + 1
        y = function.subs(x, a)
        rows.append([str(y), str(a), str(count)])
        if count != 1:
            prev = current
        current = y
        if (current < 0 and prev > 0) or (current > 0 and prev < 0):
            sus.append((a - difference, a))
        a = a + difference
    table.add_rows(rows)
    print(table.draw())
    print()
    table=Texttable()
    xList=[["  ","x1","x2"]]
    rowsNum=0
    print(f"The suspicious cutting roots are: ")
    for i in sus:
        rowsNum=rowsNum+1
        xList.append([rowsNum,i[0],i[1]])
    table.add_rows(xList)
    print(table.draw())
    print()
    for i in sus:
        ans = Bisection_Method(function, [i[0], i[1]], epsilon)
        roots.append(ans)
    return roots


def FindDerivative(function):
    print()
    print("Now let's do the method for the derivative:")
    derivative = sy.diff(function, x)
    return derivative


def FindSolution(function, boundry, epsilon):
    roots = StartIterating(function, boundry, epsilon)
    derivative = FindDerivative(function)
    deriRoots = roots + StartIterating(derivative, boundry, epsilon)
    for dr in deriRoots:
        if (function.subs(x, round(dr)) == 0):
            roots.append(round(dr))
    print()
    if len(roots) == 0:
        print("There are no roots")
    else:
        if function.subs(x, boundry[0]) == 0:
            roots.append(function.subs(x, boundry[0]))
        elif function.subs(x, boundry[1]) == 0:
            roots.append(function.subs(x, boundry[1]))
        print(f'The roots are: {roots}')


f = CreateFunction()
#(x*E**(-x**2+5*x))*(2*x**2-3*x-5)
#(0.5*2.718281**x)*(math.sin(x**2 + 5*x + 6))
b = [-3,1]
e = 0.000001
FindSolution(f, b, e)