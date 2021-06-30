# calculator
from art import logo
from os import system


# addition
def add(n1, n2):
    return n1 + n2


# subtraction
def sub(n1, n2):
    return n1 - n2


# multiplication
def multi(n1, n2):
    return n1 * n2


# division
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}


def calculator():
    print(logo)

    num1 = float(input("First Number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Next Number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calculating = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type press any "
            f"key to exit: ")
        if calculating == 'y':
            num1 = answer
        elif calculating == 'n':
            should_continue = False
            system("clear")
            system("cls")
            calculator()
        else:
            pass


calculator()
