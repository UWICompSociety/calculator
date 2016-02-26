def start():
<<<<<<< HEAD
	message = """\nCalculator menu:\n 
\t1 - Add\n
\t2 - Divide\n
Chose an option: """

	choice = input(message)

	if choice == 1:
		#accept numbers and add them here
		num1 = input("Enter the first number\n")
		num2 = input("Enter the second number\n")
		print ("Sum:"+str(num1+num2))
	elif choice == 2:
		#accept numbers and divide them here
		num1 = input("Enter the first number\n")
		num2 = input("Enter the second number\n")
		print ("Divide:"+str(num1/num2))
		
#main function in python
if __name__ == "__main__":
	start()

=======
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
    elif choice == 3:
        # accepts numbers and multiply them here
        num1 = int(input("Enter the first number\n"))
        num2 = int(input("Enter the second number\n"))
        print("Product: " + str(num1 * num2))
# main function in python
if __name__ == "__main__":
    start()
>>>>>>> 1e8ad4f34fe4d0bc4d3ee79f18e48a74a4efa4c9
