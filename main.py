def OpenCell():
    print("Open your cell!")


def main():

    userStr = input("Enter your code:")

    checkStr = "12345"

    if userStr == checkStr:
        OpenCell()
    else:
        print("Code check error!")

if __name__ == "__main__":
    main()