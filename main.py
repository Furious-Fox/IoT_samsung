import hashlib
import sys
import os.path

basePath = "/mnt/server/iot/"
numCells = 3

# Part w/ big block of code to open the cell
def OpenCell(cellNumStr):
    print("Open your cell "+cellNumStr+"!")

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
    # Debug init
    WriteHashInFile("01", "781e5e245d69b566979b86e28d23f2c7")
    WriteHashInFile("02", "781e5e245d69b566979b86e28d23f2c7")
    WriteHashInFile("03", "781e5e245d69b566979b86e28d23f2c7")
    #

    userStr = input("Enter your code:")
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
    else:
        print("Code check error!")

if __name__ == "__main__":
    main()
