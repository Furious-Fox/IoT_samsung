def OpenCell():
    print("Open your cell!")

userStr = input("Enter your code:")

checkStr = "12345"

if userStr == checkStr:
    OpenCell()
else:
    print("Code check error!")
