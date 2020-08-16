import hashlib
import sys
import os.path
import time

from PyQt5 import QtWidgets
from PyQt5 import QtCore

import clientUI

basePath = "/mnt/server/iot/"
numCells = 10


class userInterface(QtWidgets.QMainWindow, clientUI.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_0.clicked.connect(self.add_0)
        self.pushButton_1.clicked.connect(self.add_1)
        self.pushButton_2.clicked.connect(self.add_2)
        self.pushButton_3.clicked.connect(self.add_3)
        self.pushButton_4.clicked.connect(self.add_4)
        self.pushButton_5.clicked.connect(self.add_5)
        self.pushButton_6.clicked.connect(self.add_6)
        self.pushButton_7.clicked.connect(self.add_7)
        self.pushButton_8.clicked.connect(self.add_8)
        self.pushButton_9.clicked.connect(self.add_9)
        self.pushButton_clear.clicked.connect(self.action_clear)
        self.pushButton_enter.clicked.connect(self.action_enter)


# Part w/ big block of code to open the cell
    def OpenCell(self, cellNumStr):
        self.label.setText("Open your cell "+cellNumStr+"!")
        print("Open your cell "+cellNumStr+"!")
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(3000, loop.quit)
        loop.exec_()
        self.label.setText("")

    def DeleteHashFile(self, fileName):
        try:
            if os.path.exists(basePath + fileName):
                os.remove(basePath + fileName)
                #os.system("rm " + basePath + fileName)
            else:
                print("File does not exist", file = sys.stderr)
        except Exception as ex:
            print("Cant remove file :" + fileName, file = sys.stderr)
            print(ex, file = sys.stderr)
            

    def WriteHashInFile(self, fileName, hashStr):
        try:
            fileObj = open(basePath + fileName, "w")
            fileObj.write(hashStr)
        except Exception as ex:
            print("Cant open and write to file :" + fileName, file = sys.stderr)
            print(ex, file = sys.stderr)
        finally:
            fileObj.close()

    def CheckCellFile(self, fileName):
        filePath = basePath + fileName
        if os.path.exists(filePath):
            return True
        else:
            return False

    def GetHashFromFile(self, fileName):
        try:
            fileObj = open(basePath + fileName, "r")
            lineFile = fileObj.readline()
        except Exception as ex:
            print("Cant open and read file: " + fileName, file = sys.stderr)
            print(ex, file = sys.stderr)
        finally:
            fileObj.close()
        
        return lineFile



    def add_0(self):
        self.lineEdit.setText(self.lineEdit.text()+"0")
        self.label.setText("")

    def add_1(self):
        self.lineEdit.setText(self.lineEdit.text()+"1")
        self.label.setText("")

    def add_2(self):
        self.lineEdit.setText(self.lineEdit.text()+"2")
        self.label.setText("")

    def add_3(self):
        self.lineEdit.setText(self.lineEdit.text()+"3")
        self.label.setText("")

    def add_4(self):
        self.lineEdit.setText(self.lineEdit.text()+"4")
        self.label.setText("")

    def add_5(self):
        self.lineEdit.setText(self.lineEdit.text()+"5")
        self.label.setText("")

    def add_6(self):
        self.lineEdit.setText(self.lineEdit.text()+"6")
        self.label.setText("")

    def add_7(self):
        self.lineEdit.setText(self.lineEdit.text()+"7")
        self.label.setText("")

    def add_8(self):
        self.lineEdit.setText(self.lineEdit.text()+"8")
        self.label.setText("")

    def add_9(self):
        self.lineEdit.setText(self.lineEdit.text()+"9")
        self.label.setText("")

    def action_enter(self):
        self.label.setText("")
        userStr = self.lineEdit.text()
        if not userStr: return
        cellNumStr = userStr[:2]

        # Maybe we need it
        #if cellNumStr[0] == '0':
        #    cellNumInt = int(cellNumStr[1])
        
        userStr = userStr[2:]
        hashFileStr=None
        if(self.CheckCellFile(cellNumStr)):
            hashFileStr = self.GetHashFromFile(cellNumStr)

        userStr = hashlib.md5(userStr.encode())

        if userStr.hexdigest() == hashFileStr:
            self.OpenCell(cellNumStr)
            self.DeleteHashFile(cellNumStr)
        else:
            print("Code check error!")
            self.label.setText("Code check error!")
        
        self.lineEdit.setText("")


    def action_clear(self):
        self.label.setText("")
        self.lineEdit.setText("")



        








def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = userInterface()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение



def main_old():

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
