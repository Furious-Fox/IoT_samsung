import os.path
import sys
import cladmanUI
from PyQt5 import QtWidgets

basePath = "/mnt/server/iot/"
numCells = 10

class CladmanWindow(QtWidgets.QMainWindow, cladmanUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.action_done)


    def action_done(self):
        cellNum=self.FindFreeCell()
        if cellNum==0:
            self.label_2.setText("No free cells left")
        else:
            self.label_2.setText("Put your order ***" + " to cell number: " + str(cellNum))


    def CheckCellFile(self, fileName):
        filePath = basePath + fileName
        if os.path.exists(filePath):
            return True
        else:
            return False
        
    def FindFreeCell(self):
        num = 1
        while(num < 10):
            if (num < 10):
                if (not self.CheckCellFile("0" + str(num))):
                    return num
            else:
                if (not self.CheckCellFile(str(num))):
                    return num
            num = num + 1
        return 0

    def WriteHashInFile(self, fileName ,hashStr):
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
    app.exec_()
    
    
    freeCellNum = FindFreeCell()
    if freeCellNum == 0:
        pass
        #print("No free cells left")
    else:
        pass
        #print("Put your order " + str(orderNum) + " to cell number: " + str(freeCellNum))
    
        if (freeCellNum < 10):
            WriteHashInFile("0" + str(freeCellNum), "781e5e245d69b566979b86e28d23f2c7")
        else:
            WriteHashInFile(str(freeCellNum), "781e5e245d69b566979b86e28d23f2c7")

if __name__ == "__main__":
    main()