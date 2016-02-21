__author__ = 'javon'


def start():

    # accept operation
    choice = input("Press 1 to add\nPress 2 to subtract two numbers\nPress 3 to find product\nPress 4 to find the exponent of a number")
    
    if choice == 1:
        # adds them here
	num1 = int(input("Enter the first number: \n"))
        num2 = int(input("Enter the second number: \n"))
	print("Sum: " + str(num1 + num2))
    elif choice == 2:
        # subtracts them here
        num1 = int(input("Enter the first number: \n"))
	num2 = int(input("Enter the second number: \n"))
        print("Difference: " + str(num1 - num2))
    elif choice == 3:
        # multiply them here
        num1 = int(input("Enter the first number: \n"))
	num2 = int(input("Enter the second number: \n"))
        print("Product: " + str(num1 * num2))
    elif  choice == 4:
    	# finds the value of a number raised to an index
        num1 = int(input("Enter the first number: \n"))
	num2 = int(input("Enter the second number: \n"))
	print("The result of ",num1,"raised by ",num2," = ",num1**num2)


	# main function in python
if __name__ == "__main__":
    start()
