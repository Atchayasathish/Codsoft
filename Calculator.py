def add(x , y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    if y == 0:
        print(f'The number {y} cannot be divided')
    else:
        return x / y
    
while True:
    print("Options")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter Quit to end the program")

    user_input = input("Enter the operation : ")

    if user_input == "quit":
        break
    elif user_input in ["add" , "subtract" , "multiply" , "division"]:
        num1 = float(input("Enter the first value : "))
        num2 = float(input("Enter the second value : "))

        if user_input == "add":
            result = add(num1 , num2)
        elif user_input == "subtract":
            result = subtract(num1 , num2)
        elif user_input == "multiply":
            result = multiply(num1 , num2)
        elif user_input == "divide":
            result = divide(num1, num2)

        print(f'The result is {result}')

    else:
        print("Invalid input. Please enter the valid input")


    