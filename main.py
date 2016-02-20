__author__ = 'javon'


def start():
    choice = input("Press 1 to add\nPress 2 to find product\nPress 3 to find result\nPress 4 to find the exponent a**b\nChoice: ")
    if choice == 1:
        print add()

    elif choice == 2:
    	print multiply()
    
    elif choice == 3:
        print division()
    else:
        print "Invalid choice"

def add():
	num1 =  input("Enter first number: ")
	num2 = input("Enter second number: ")
	return "Sum: "+str(num1+num2)

def multiply():
    num1 =  input("Enter first number: ")
    num2 = input("Enter second number: ")
    return "Product: "+str(num1*num2)

def division():
    num1 =  input("Enter first number: ")
    num2 = input("Enter second number: ")
    if isinstance(num1, float):
        return "Result: "+str(num1/float(num2))
    return "Result: "+str(num1/num2)

def nthpower():
    num1 =  input("Enter first number")
    num2 = input("Enter number to raise by")
    return "Power of "+num1+"and "+num2+": "+str(num1**num2)
    

#main function in python
if __name__ == "__main__":
    start()

