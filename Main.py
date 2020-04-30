import os
import sys

def dynamic(capacity, weights, values):

    return

def main():
    args = sys.argv
    #print(len(args))
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

    c = []
    w = []
    v = []

    for file in fileList:
        FDir = dir + '/' + file
        #print(FDir, type(FDir))
        F = open(FDir, 'r')

        if file[4] == 'c':
            c = F.read().splitlines()
            F.close()

        elif file[4] == 'w':
            w = F.read().splitlines()
            F.close()
            for i in range(len(w)):
                w[i] = w[i].strip(" ")

        elif file[4] == 'v':
            v = F.read().splitlines()
            for i in range(len(v)):
                v[i] = v[i].strip(" ")
            F.close()

    print("File containing the capacity, weights, and values are: ", end=" ")
    print(cFileName, wFileName, "", sep=", ", end=" "); print(vFileName)

    print("Knapsack capacity = {0}. Total number of items = {1}".format(c[0], len(w)))

main()