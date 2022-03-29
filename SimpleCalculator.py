import SimpleCalculatorTools

def print_operations(operations):
    print("Operations:")
    for choice, operation in operations.items():
        print(f"{choice}: {operation.__name__}")


def get_operation(operations):
    operation = input("Choose an operation: ")

    while operation not in operations:
        print("Invalid choice")
        operation = input("Choose an operation: ")
    else:
        return operation


def get_operands():
    num1 = float(input("First operand: "))
    num2 = float(input("Second operand: "))

    return num1, num2


def main():
    print("Simple Calculator")

    operations = {
        "1": SimpleCalculatorTools.add,
        "2": SimpleCalculatorTools.subtract,
        "3": SimpleCalculatorTools.multiply,
        "4": SimpleCalculatorTools.divide,
    }

    while True:

        print_operations(operations)

        chosen_operation = operations[get_operation(operations)]

        print("Result:", chosen_operation(*get_operands()))


if __name__ == "__main__":
    main()
