def get_int():
    while True:
        try:
            num = int(input("Input an Integer -> "))
            print()
            print("Number is an integer")
        except ValueError:
            print()
            print("Bad Input - Number is not an Integer. Try again.")
            continue
        else:
            return num
            

def get_float():
    while True:
        try:
            print()
            num = float(input("Input a Float Number -> "))
            print()
            print("Number is a float")
        except ValueError:
            print()
            print("Bad Input - Number is not a Float. Try again.")
            continue
        else:
            return num
            