import os.path
import sys
import cladmanUI
from PyQt5 import QtWidgets
from PyQt5 import QtCore

basePath = "/mnt/server/iot/"
numCells = 10

class CladmanWindow(QtWidgets.QMainWindow, cladmanUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.action_done)
        self.comboBox.addItem("451")
        self.comboBox.addItem("061")
        self.comboBox.addItem("039")
        self.comboBox.addItem("444")
        self.comboBox.addItem("777")
        self.comboBox.addItem("666")

    def PutOrderInCell(self, cellNum):
        self.label_2.setText("Положите заказ №" + self.comboBox.currentText() + " в ячейку: " + str(cellNum))
        self.comboBox.removeItem(self.comboBox.findText(self.comboBox.currentText()))
        if (cellNum < 10):
            self.WriteHashInFile("0" + str(cellNum), "781e5e245d69b566979b86e28d23f2c7")
        else:
            self.WriteHashInFile(str(cellNum), "781e5e245d69b566979b86e28d23f2c7")
        
        self.clear_text_3s_delay()


    # Clear main text after 3s
    def clear_text_3s_delay(self):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(3000, loop.quit)
        loop.exec_()
        self.label_2.setText("")


    def action_done(self):
        cellNum=self.FindFreeCell()
        if cellNum==0:
            self.label_2.setText("Свободных ячеек не осталось")
            self.clear_text_3s_delay()
        else:
            self.PutOrderInCell(cellNum)
            


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
        

if __name__ == "__main__":
    main()