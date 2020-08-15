import os.path

basePath = "/mnt/server/iot"
numCells = 10

def CheckCellFile(fileName):
    filePath = basePath + fileName
    if os.path.exists(filePath):
        return True
    else:
        return False
    
def FindFreeCell():
    num = 1
    while(num < 100):
        if (num < 10):
            if (not CheckCellFile("0" + str(num))):
                return num
        else:
            if (not CheckCellFile(str(num))):
                return num
        num = num + 1
    return 0

def main():
    input("Press 'Enter' to show all orders")
    print("Order 36")
    orderNum = input("Type order number: ")
    orderNum = int(orderNum)
    
    freeCellIndex = FindFreeCell()
    if freeCellIndex == 0:
        print("No free cells left")
    else:
        print("Put your order " + str(orderNum) + " to cell number: " + str(freeCellIndex))

if __name__ == "__main__":
    main()