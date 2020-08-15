import hashlib

# Part w/ big block of code to open the cell
def OpenCell():
    print("Open your cell!")

checkStr = "827ccb0eea8a706c4c34a16891f84e7b"   # TODO: Move it in the file
userStr = input("Enter your code:")

hashStrObj = hashlib.md5(userStr.encode())

if hashStrObj.hexdigest() == checkStr:
    OpenCell()
else:
    print("Code check error!")
