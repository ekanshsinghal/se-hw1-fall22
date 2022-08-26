def calculate(value1, value2, operation):
    result = None
    if operation == '+':
        result = value1 + value2
    elif operation == '-':
        result = value1 - value2
    elif operation == '*':
        result = value1 * value2
    elif operation == '/':
        result = value1 / value2
    elif operation == '%':
        result = value1 % value2
    return result

if __name__ == "__main__":

    while True:
        value1 = int(input("Enter number 1 : "))
        value2 = int(input("Enter number 1 : "))
        print("+, -, *, /, %")
        operation = input("Enter operation : ")
        
        result = calculate(value1, value2, operation)

        if not result:
            print("Invalid Input. Try again.")
            continue
        
        print(str(value1) + " " + operation + " " + str(value2) + " = " + str(result))

        select = input("Enter any key. Enter 'y' if you want to stop : ")
        if select == 'y':
            break