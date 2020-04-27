import os
import sys

def main():
    args = sys.argv
    print(len(args))
    if len(args) != 3:
        print("Invalid number of arguments. Exiting...")
        return

    dir = args[1]
    num = args[2]
    files = os.listdir(dir)
    cFile = "p0" + num + "_c.txt"
    wFile = "p0" + num + "_w.txt"
    vFile = "p0" + num + "_v.txt"
    fileList = []
    for file in files:
        if cFile == file:
            fileList.append(file)
        elif wFile == file:
            fileList.append(file)
        elif vFile == file:
            fileList.append(file)
    print(fileList)

main()