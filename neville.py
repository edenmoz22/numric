def neville(list, x):
    dict={}
    tempdict ={}
    n = len(list)
    iters = 1
    while len(dict) != 1:
        for i in range(n - iters):
            temp = ((x - list[i][0]) * list[i + iters][1] - (x - list[i + iters][0]) * list[i][1]) / (list[i + iters][0] - list[i][0])
            tempdict['p' + str(i) + ',' + str(i + iters)] = temp
            #print('p' + str(i) + ',' + str(i + iters))
        dict = tempdict
        tempdict = {}
        print('Iteration Number: ',iters,dict)
        iters += 1


    return dict


list = [[2, 0], [2.25, 0.112463], [2.3, 0.167996], [2.7, 0.222709]]
print('The answer is: ',neville(list,2.4))