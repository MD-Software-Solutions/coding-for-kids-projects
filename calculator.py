def calculator(num1, num2, operator):
    if (operator == "+"):
        return num1 + num2

    if (operator == "-"):
        return num1 - num2

    if (operator == "/"):
        return num1 / num2

    if (operator == "*"):
        return num1 * num2

def main():
    boolean = True

    while(boolean == True):
        num1 = int(input("Enter number 1:"))
        num2 = int(input("Enter number 2:"))
        operator = input("Enter your operator (+,-,/,*):")

        num3 = calculator(num1, num2, operator)
        print(num3)

        x = input("Would you like to exit the program(y/n):")

        if (x == "y"):
            boolean = False
        else:
            pass

if (__name__=="__main__"):
    main()