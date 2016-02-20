__author__ = 'javon'


def start():
    choice = input("Press 1 to add\nPress 2 to subtract two numbers\nPress 3 to find product\n")
    if choice == 1:
        # accept numbers and add them here
        num1 = int(input("Enter the first number: \n"))
        num2 = int(input("Enter the second number: \n"))
        print("Sum: " + str(num1 + num2))
    elif choice == 2:
        # accept numbers and subtracts them here
        num1 = int(input("Enter the first number: \n"))
        num2 = int(input("Enter the second number: \n"))
        print("Difference: " + str(num1 - num2))

    if choice == 3:
        num1 = int(input("Enter the first number\n"))
        num2 = int(input("Enter the second number\n"))
        print("Product: " + str(num1 * num2))


# main function in python
if __name__ == "__main__":
    start()
