import numpy as np
import sympy as sy
from texttable import Texttable

x = sy.symbols("x")

def CreateFunction():
    funcInput = input("Enter a function: ")
    func = sy.sympify(funcInput)
    return func


def NewtonRaphson(f, derF, boundary, epsilon):
    a = boundary[0]
    b = boundary[1]
    count = 1  # iteration count
    xr = (a + b) / 2  # initial guess
    table = Texttable()
    table.set_precision(10)
    rows = [["f'(x)", "f(x)", "Xr", "i"]]
    print()
    print("The Newton-Raphson table is:")
    while abs(f.subs(x, xr)) > epsilon and count < 500:  # iterate until f(x)>epsilon or count=500
        rows.append([derF.subs(x, xr), f.subs(x, xr), xr, count])
        xr = xr - (f.subs(x, xr) / derF.subs(x, xr))  # formula
        count = count + 1
    table.add_rows(rows)
    print(table.draw())
    return xr




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
    table.set_precision(10)
    rows = [['f(x)', 'x', 'i']]
    print(f'The difference is {difference}')
    print()
    while a <= b + 0.0001:
        count = count + 1
        y = function.subs(x, a)
        rows.append([str(y), str(a), str(count)])
        if count != 1:
            prev = current
        current = y
        if (current < 0 and prev > 0) or (current > 0 and prev < 0):  # sign change
            sus.append((a - difference, a))
        a = a + difference
    table.add_rows(rows)
    print(table.draw())
    print()
    table = Texttable()
    table.set_precision(10)
    xList = [["  ", "x1", "x2"]]
    rowsNum = 0
    if len(sus)==0:
        print("There are no roots for this table")
    else:
        print(f"The suspicious cutting roots are: ")
        for i in sus:
            rowsNum = rowsNum + 1
            xList.append([rowsNum, i[0], i[1]])
    table.add_rows(xList)
    if len(sus)!=0:
        print(table.draw())
    print()
    for i in sus:
        ans = NewtonRaphson(function, FindDerivative(function), [i[0], i[1]], epsilon)
        roots.append(ans)
    return roots


def FindDerivative(function):
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
#(x*E**(-(x**2)+5*x))*(2*x**2-3*x-5)
#(sin(x**2+5*x+6))/((2*E**-x))
b = [-3,1]
e = 0.000001
FindSolution(f, b, e)