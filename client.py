import hashlib
import sys
import os.path

basePath = "/mnt/server/iot/"
numCells = 10

# Part w/ big block of code to open the cell
def OpenCell(cellNumStr):
    print("Open your cell "+cellNumStr+"!")

def DeleteHashFile(fileName):
    try:
        if os.path.exists(basePath + fileName):
            os.remove(basePath + fileName)
            #os.system("rm " + basePath + fileName)
        else:
            print("File does not exist", file = sys.stderr)
    except Exception as ex:
        print("Cant remove file :" + fileName, file = sys.stderr)
        print(ex, file = sys.stderr)
        

def WriteHashInFile(fileName ,hashStr):
    try:
        fileObj = open(basePath + fileName, "w")
        fileObj.write(hashStr)
    except Exception as ex:
        print("Cant open and write to file :" + fileName, file = sys.stderr)
        print(ex, file = sys.stderr)
    finally:
        fileObj.close()

def CheckCellFile(fileName):
    filePath = basePath + fileName
    if os.path.exists(filePath):
        return True
    else:
        return False

def GetHashFromFile(fileName):
    try:
        fileObj = open(basePath + fileName, "r")
        lineFile = fileObj.readline()
    except Exception as ex:
        print("Cant open and read file: " + fileName, file = sys.stderr)
        print(ex, file = sys.stderr)
    finally:
        fileObj.close()
    
    return lineFile


def main():

    userStr = input("Enter your code: ")
    cellNumStr = userStr[:2]

    # Maybe we need it
    #if cellNumStr[0] == '0':
    #    cellNumInt = int(cellNumStr[1])
    
    userStr = userStr[2:]
    hashFileStr=None
    if(CheckCellFile(cellNumStr)):
        hashFileStr = GetHashFromFile(cellNumStr)

    userStr = hashlib.md5(userStr.encode())

    if userStr.hexdigest() == hashFileStr:
        OpenCell(cellNumStr)
        DeleteHashFile(cellNumStr)
    else:
        print("Code check error!")

    main()

if __name__ == "__main__":
    main()
