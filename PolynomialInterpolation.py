from yaakobiAndZaydel import YaakobiAndZaydel

def PolynomialInterpolation(list, x):
    n = len(list)
    gaus = []
    for i in range(0, n):
        temp = []
        for j in range(0, n):
            if j == 0:
                temp.append(1)
            else:
                temp.append(list[i][0]**j)
        gaus.append(temp)
    for i in range(0, n):
        gaus[i].append(list[i][1])
    print(gaus)
    zidel = YaakobiAndZaydel()
    zidel.insertFunc(gaus)
    zidel.Zaydel()
    res =zidel.getAnswer()
    #res = [-1.95482,1.34938,-0.14288,-0.02155]
    p = 0
    for i in range(0, len(res)):
        if i == 0:
            p += res[i]
        else:
            p += res[i] * pow(x,i)
    return p



#list = [[2, 0], [2.25, 0.112463], [2.3, 0.167996], [2.7, 0.222709]]
list = [[1.2,3.5095],[1.3,3.6984],[1.4,3.9043],[1.5,4.1293],[1.6,4.3756]]
print(PolynomialInterpolation(list, 1.37))
