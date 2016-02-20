__author__ = 'javon'


def start():
    choice = input("Press 1 to add\nPress 2 to find product\n")
    if choice == 1:
        #accept numbers and add them here
        num1 = input("Enter the first number\n")
        num2 = input("Enter the second number\n")
        print ("Sum:"+str(num1+num2))

    if choice == 2:
    	num1 = input("Enter the first number\n")
    	num2 = input("Enter the second number\n")
    	print("Product: "str(num1*num2))


#main function in python
if __name__ == "__main__":
    start()

