from art import logo

print(logo)


def sub(n1, n2):
    """

    :param n1:
    :param n2:
    :return: difference between n1 and n2
    """
    return n1 - n2


def add(n1, n2):
    """

    :param n1:
    :param n2:
    :return: sum of n1 and n2
    """
    return n1 + n2


def mul(n1, n2):
    """

    :param n1:
    :param n2:
    :return: product of n1 and n2
    """
    return n1 * n2


def div(n1, n2):
    """

    :param n1:
    :param n2:
    :return: division of n1 and n2
    """
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

calculation_on = True

num1 = float(input("Enter the first number: "))
for key in operations:
    print(key)
while calculation_on:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Enter the second number: "))
    calculation_operation = operations[operation_symbol]
    answer = calculation_operation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_calculation = input("Do you want to continue calculation? Type 'y' or 'n': ").lower()
    if continue_calculation == "n":
        calculation_on = False
    else:
        num1 = answer
