import os.path
import sys
from cladmanUI import Ui_MainWindow
from PyQt5 import QtWidgets

basePath = "/mnt/server/iot/"
numCells = 10

class CladmanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CladmanWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def CheckCellFile(fileName):
    filePath = basePath + fileName
    if os.path.exists(filePath):
        return True
    else:
        return False
    
def FindFreeCell():
    num = 1
    while(num < 10):
        if (num < 10):
            if (not CheckCellFile("0" + str(num))):
                return num
        else:
            if (not CheckCellFile(str(num))):
                return num
        num = num + 1
    return 0

def WriteHashInFile(fileName ,hashStr):
    try:
        fileObj = open(basePath + fileName, "w")
        fileObj.write(hashStr)
    except Exception as ex:
        print("Cant open and write to file: " + fileName, file = sys.stderr)
        print(ex, file = sys.stderr)
    finally:
        fileObj.close()

def main():
    app = QtWidgets.QApplication([])
    application = CladmanWindow()
    application.show()

    
    
    freeCellNum = FindFreeCell()
    if freeCellNum == 0:
        exit(-1)
        #print("No free cells left")
    else:
        pass
        #print("Put your order " + str(orderNum) + " to cell number: " + str(freeCellNum))
    
    #if (freeCellNum < 10):
        #WriteHashInFile("0" + str(freeCellNum), "781e5e245d69b566979b86e28d23f2c7")
    #else:
        #WriteHashInFile(str(freeCellNum), "781e5e245d69b566979b86e28d23f2c7")

if __name__ == "__main__":
    main()