
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division By zero ;)"
    return x / y


def main():
    while True:
        menu = """
        Select Operation:

        1. Add
        2. Substract
        3. Multiply
        4. Divide
        5. Exit
        """
        print(menu)

        choise = input("Enter choice (1/2/3/4/5): ")

        if choise == "5":
            break
        num1 = float(input("Entert First Number: "))
        num2 = float(input("Entert Second Number: "))

        if num1 == int(num1):
            num1 = int(num1)

        if num2 == int(num2):
            num2 = int(num2)

        if choise == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choise == '2':
            print(f"{num1} - {num2} = {substract(num1, num2)}")
        elif choise == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choise == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            prtin("Invalid Number ;D")




if __name__ == "__main__":
    main()