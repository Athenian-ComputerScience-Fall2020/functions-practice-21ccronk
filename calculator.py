'''
Collaborators: 

'''
def add_function():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    answer = number1 + number2
    return answer

def subtract_function():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    answer = number1 - number2
    return answer

def multiply_function():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    answer = number1 * number2
    return answer

def divide_function():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    answer = number1 / number2
    return answer

operation = input("Enter 1 to add, 2 to subtract, 3 to multiply, and 4 to divide: ")
if operation == "1":
    print(add_function())

elif operation == "2":
    print(subtract_function())

elif operation == "3":
    print(multiply_function())

elif operation == "4":
    print(divide_function())