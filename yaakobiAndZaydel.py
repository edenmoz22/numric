import texttable
import numpy as np
class YaakobiAndZaydel:
    mat_flag = False
    index = 0
    flag = False
    equations = []
    temp = []
    answer = []
    rows = 0
    cols = 0
    col_swaper_index = 0
    max_iter = 2
    counter = 0
    def insertFunc(self, listOfLists):
        self.equations = list(listOfLists)


    def MatrixPrint(self):
        if self.flag == False:

            if self.mat_flag == False:
                print('** Matrix Representation: **')
                eq = list(self.equations)
                eq.insert(0,['X', 'Y', 'Z','W','K', 'B'])
                table_mat = texttable.Texttable()
                table_mat.set_precision(3)
                table_mat.add_rows(eq)
                print(table_mat.draw())
                self.mat_flag = False
                print()



            print('\nyour self.equations are:\n')

            for x in self.equations:
                for i in range(len(x)):
                    if x[i] >= 0:
                        if i == len(x) - 2:
                            print('+ {} = '.format(x[i]), end='')
                        else:
                            print('+ {} '.format(x[i]), end='')

                    else:
                        if i == len(x) - 2:
                            print('{} = '.format(x[i]), end='')
                        else:
                            print('{} '.format(x[i]), end='')
                print()
        else:
            print('\nyour self.equations are:\n')

            for x in self.equations:
                for i in range(len(x)):
                    if x[i] >= 0:
                        if i == 0:
                            print('+ {} = '.format(x[i]), end='')
                        else:
                            print('+ {} '.format(x[i]), end='')

                    else:
                        if i == 0:
                            print('{} = '.format(x[i]), end='')
                        else:
                            print('{} '.format(x[i]), end='')
                print()


    def findDominantRow(self, index):
        for i in range(index, len(self.equations)):
            if abs(self.equations[i][index - 1]) > sum(map(abs, self.equations[i][:index - 1])) + sum(map(abs, self.equations[i][index - 1 + 1:len(self.equations[i]) - 1])):
                return i

    def isValid(self):
        self.MatrixPrint()

        for i in range(self.index, len(self.equations)):
            j = None

            if abs(self.equations[i][i]) < sum(map(abs, self.equations[i][:i])) + sum(
                    map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1])):
                self.col_swaper_index += 1

                sumA = sum(map(abs, self.equations[i][:i])) + sum(
                    map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1]))


                print('\npivot: ', self.equations[i][i], ' sum: ',
                      sum(map(abs, self.equations[i][:i])) + sum(
                          map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1])),
                      ' - need to be changed!\n')

                j = self.findDominantRow(i + 1)
                if j is None:
                    if self.col_swaper_index < len(self.equations[0]) - 1:

                        np_eq = np.array(self.equations)
                        np_eq[:, [i, self.col_swaper_index]] = np_eq[:, [self.col_swaper_index, i]]

                        self.equations = list(np_eq)
                        for i in range(len(np_eq)):
                            self.equations[i] = list(np_eq[i])

                        self.MatrixPrint()
                        self.isValid()

                    elif self.col_swaper_index == len(self.equations[0]) - 1:
                        if self.max_iter > self.counter:
                            self.col_swaper_index = 0
                            self.counter += 1
                            self.isValid()
                        else:

                            print('cannot find dominant diagonal for this matrix - thus, there is no answer.')
                            exit(1)

        # self.MatrixPrint()
        #
        # for i in range(len(self.equations)):
        #     j = None
        #     if abs(self.equations[i][i]) < sum(map(abs, self.equations[i][:i])) + sum(
        #             map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1])):
        #         print('pivot: ', self.equations[i][i], ' sum: ',
        #               sum(map(abs, self.equations[i][:i])) + sum(map(abs, self.equations[i][i + 1:len(self.equations[i]) - 1])),
        #               ' - need to be changed!')
        #         j = self.findDominantRow(i + 1)
        #         if j is None:
        #             print('cannot find dominant number - thus, there is no answer.')
        #             exit(1)
        #         self.changeRow(i, j)
        #         self.MatrixPrint()


    def changeRow(self, row_index1, row_index2):
        self.equations[row_index1], self.equations[row_index2] = self.equations[row_index2], self.equations[row_index1]


    def Yaakobi(self):
        variables = []
        temp = [0 for i in range(self.cols)]
        changes = []
        variables.append(list(temp))
        self.isValid()

        self.flag = True
        i = 0
        table_ans = texttable.Texttable()
        table_ans.set_precision(5)

        for x in self.equations:  ## x = 5 + y + z
            x[0], x[i] = x[i], x[0]
            changes.append(tuple([0, i]))
            i += 1
            print()

        for x in self.equations:  ## 2x = - 10y - 3z
            for i in range(1, len(x) - 1):
                x[i] *= -1

        j = 0
        for x in self.equations:  ## ## x = - (10*0 - 3*0)/2
            c1, c2 = changes[j][0], changes[j][1]
            temp1 = list(variables[len(variables) - 1])
            temp1[c1], temp1[c2] = temp1[c2], temp1[c1]

            sum_temp = 0
            k = 1
            for i in range(1, len(x) - 1):
                sum_temp = sum_temp + (x[i] * temp1[k]) / x[0]
                k += 1

            sum_temp = x[len(x) - 1] / x[0] + sum_temp

            temp[j] = sum_temp

            j += 1

        self.MatrixPrint()
        variables.append(list(temp))

        while (abs(variables[len(variables) - 1][0] - variables[len(variables) - 2][0]) > 0.001):
            j = 0
            for x in self.equations:  ## ## x = - (10*0 - 3*0)/2
                c1, c2 = changes[j][0], changes[j][1]
                temp1 = list(variables[len(variables) - 1])
                temp1[c1], temp1[c2] = temp1[c2], temp1[c1]

                sum_temp = 0
                k = 1
                for i in range(1, len(x) - 1):
                    sum_temp = sum_temp + (x[i] * temp1[k]) / x[0]
                    k += 1
                sum_temp = x[len(x) - 1] / x[0] + sum_temp

                temp[j] = sum_temp

                j += 1
            variables.append(list(temp))
        print()
        j = 0
        for i in range(len(variables)):

            variables[i].insert(0,j)
            j += 1
        variables.insert(0,['Index','Xr+1','Yr+1','Zr+1'])
        self.answer = list(variables[len(variables) - 1][1:])
        table_ans.add_rows(variables)


        print(table_ans.draw())



    def Zaydel(self):
        self.MatrixPrint()
        variables = []
        temp = [0 for i in range(len(self.equations))]
        changes = []
        variables.append(list(temp))
        # self.isValid()
        table_ans = texttable.Texttable()
        table_ans.set_precision(5)

        self.flag = True
        print('the fun part starts here:')
        i = 0
        for x in self.equations:  ## x = 5 + y + z
            x[0], x[i] = x[i], x[0]
            changes.append(tuple([0, i]))
            i += 1
            print()

        for x in self.equations:
            for i in range(1, len(x) - 1):
                x[i] *= -1

        j = 0
        for x in self.equations:
            c1, c2 = changes[j][0], changes[j][1]
            temp1 = list(temp)
            temp[c1], temp[c2] = temp[c2], temp[c1]

            sum_temp = 0
            k = 1
            for i in range(1, len(x) - 1):
                sum_temp = sum_temp + (x[i] * temp[k]) / x[0]
                k += 1

            sum_temp = x[len(x) - 1] / x[0] + sum_temp

            temp[j] = sum_temp

            j += 1
        temp[0] = temp[1]
        self.MatrixPrint()
        variables.append(list(temp))

        counter1 = 0
        max_iter1 = 50
        while (abs(variables[len(variables) - 1][0] - variables[len(variables) - 2][0]) > 0.001 and max_iter1 > counter1):
            j = 0
            for x in self.equations:  ## ## x = - (10*0 - 3*0)/2
                c1, c2 = changes[j][0], changes[j][1]
                temp1 = list(variables[len(variables) - 1])
                temp1[c1], temp1[c2] = temp1[c2], temp1[c1]

                sum_temp = 0
                k = 1
                for i in range(1, len(x) - 1):
                    sum_temp = sum_temp + (x[i] * temp1[k]) / x[0]
                    k += 1
                sum_temp = x[len(x) - 1] / x[0] + sum_temp

                temp[j] = sum_temp

                j += 1
            variables.append(list(temp))
            counter1 += 1
        print()

        for i in range(len(variables)):

            variables[i].insert(0,j)
            j += 1
        variables.insert(0, ['Index', 'Xr+1', 'Yr+1', 'Zr+1','Wr+1','Kr+1'])
        table_ans.add_rows(variables)

        self.answer = list(variables[len(variables)-1][1:])

        print(table_ans.draw())
    def getAnswer(self):
        if self.answer != []:
            return self.answer


