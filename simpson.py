import math
from texttable import Texttable
def f(x):
    return (x*math.e**(-(x**2)+5*x))*(2*x**2-3*x-5)
    #return (0.5*math.e**x)*(math.sin(x**2 + 5*x + 6))

def simpson(f,a,b,n):
    i = n/2
    h = (b-a)/n
    x = 0
    simlist= []
    k= a
    while k < b:
        simlist.append(k)
        k += h
    res=[["I","X","F(X)"]]
    for w in range(len(simlist)):
        res.append([w,simlist[w],f(simlist[w])])
    table.add_rows(res)
    print(table.draw())

    for j in range(0,len(simlist)):
        if int(j) == 0:
            x = f(a)
        elif int(j)%2 == 1:
            x += 4*f(simlist[j])
        else:
            x += 2 * f((simlist[j]))
    x += f(b)
    x = (1/3)*h*x
    return x

table = Texttable()
print("The result is:",simpson(f,0.5,1,4))