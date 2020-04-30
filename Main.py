import os
import sys

def TDP(capacity, weights, values, n):
    if n == 0 or capacity == 0:
        return 0

    if (weights[n - 1] > capacity):
        return TDP(capacity, weights, values, n - 1)

    else:
        return max(values[n - 1] + TDP(capacity - weights[n - 1], weights, values, n - 1),
                   TDP(capacity, weights, values, n - 1))

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
    print(cFileName, wFileName, "", sep=", ", end=" "); print(vFileName)

    print("Knapsack capacity = {0}. Total number of items = {1}".format(c, len(w)))

    print('Traditional Dynamic Programming Optimal value:', TDP(c, w, v, len(w)))

main()