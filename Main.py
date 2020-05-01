import os
import sys
import time

# Traditional(Bottom Up) Approach
def TDP(capacity, weights, values, n):
    # start time
    start = time.time()
    # creates (capacity + 1)x(# of weights or values) table
    table = [[0 for w in range(capacity + 1)] for i in range(n + 1)]

    # adds values to Knapsack table
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weights[i - 1] <= w:
                table[i][w] = max(values[i - 1] + table[i - 1][w - weights[i - 1]],
                                  table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    # end time
    end = time.time() - start

    # stores the result of Knapsack table
    res = table[n][capacity]
    print('Traditional Dynamic Programming Optimal value:', res)

    w = capacity
    opt_values = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][w]:
            continue
        else:
            # optimal item indexes
            # print('w:', weights[i - 1], 'v:', values[i - 1])
            opt_values.append(i)

            # Since this weight is included
            # its value is deducted
            res = res - values[i - 1]
            w = w - weights[i - 1]

    opt_values.reverse()
    print('Traditional Dynamic Programming Optimal subset: ',
          '{', ', '.join(str(x) for x in opt_values), '}', sep="")
    print('Traditional Dynamic Programming Time Taken:', end, end='\n\n')

def main():
    args = sys.argv
    if len(args) != 3:
        print("Invalid number of arguments. Exiting...")
        return

    dir = args[1]
    num = args[2]
    files = os.listdir(dir)
    cFileName = "p" + num + "_c.txt"
    wFileName = "p" + num + "_w.txt"
    vFileName = "p" + num + "_v.txt"
    fileList = []
    for file in files:
        if cFileName == file:
            fileList.append(file)
        elif wFileName == file:
            fileList.append(file)
        elif vFileName == file:
            fileList.append(file)

    c = 0
    w = []
    v = []


    for file in fileList:
        FDir = dir + '/' + file
        F = open(FDir, 'r')

        if file[4] == 'c':
            f = F.read().splitlines()
            c = int(f[0])
            F.close()

        elif file[4] == 'w':
            w = F.read().splitlines()
            F.close()
            for i in range(len(w)):
                w[i] = int(w[i].strip(" "))

        elif file[4] == 'v':
            v = F.read().splitlines()
            for i in range(len(v)):
                v[i] = int(v[i].strip(" "))
            F.close()

    print("File containing the capacity, weights, and values are: ", end=" ")
    print(cFileName, wFileName, "", sep=", ", end=vFileName); print('\n')
    print("Knapsack capacity = {0}. Total number of items = {1}".format(c, len(w)))

    TDP(c,w, v, len(w))

main()