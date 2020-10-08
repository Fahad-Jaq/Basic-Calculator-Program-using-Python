# these 5 functions does the maths
def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def power(x, y):
    return pow(x, y)


# the num_input function is used to call the entire input method
# this is given as function because
# when an incorrect input type is given by the user , we can call the function again and ask to enter the input again.
def num_input():
    # this try block helps to get rid of errors occurred because of invalid input(other than float or int)
    try:
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the number: "))

        print("\n")
        print("Select")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Power")
        print("\n")

        # As it is given as a function ,input method can be called again and again on incorrect input
        def todo_input():
            todo = input("Enter the number of action to do(1-5): ")
            if todo == "1":
                print("result =", addition(num1, num2))
            elif todo == "2":
                print("result =", subtraction(num1, num2))
            elif todo == "3":
                print("result =", multiplication(num1, num2))
            elif todo == "4":
                print("result =", division(num1, num2))
            elif todo == "5":
                print("result =", power(num1, num2))
            else:
                print("invalid input")
                todo_input()

        todo_input()
    # except block lets you to handle the error.
    except ValueError:
        print("Sorry only numbers are allowed")
        num_input()  # this calls function again when an error is occurred


num_input()  # this line is required to call the entire function at the first place
