def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
    }

    print("Select operation:")
    for key, value in operations.items():
        print(f"{key}. {value[0]}")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operation_name, operation_func = operations[choice]
        result = operation_func(num1, num2)
        print(f"{num1} {operation_name} {num2} = {result}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()