__author__ = 'javon'


def start():
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

