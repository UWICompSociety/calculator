__author__ = 'javon'


def start():
    choice = input("Press 1 to add\nPress 2 to find product\nPress 3 to find result\nPress 4 to find the exponent a**b\nChoice: ")
    if choice == 1:
        num1 =  input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("Sum: "+ str(add(num1, num2)))

    elif choice == 2:
        num1 =  input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("Product: "+ str(multiply(num1, num2)))
    	
    elif choice == 3:
        num1 =  input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("Quotient: "+ str(division(num1, num2)))
        
    elif choice == 4:
        num1 =  input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("Power: "+ str(nthpower(num1, num2)))
    else:
        print "Invalid choice"

def add(num1, num2):
    return num1+num2

def multiply(num1, num2):
    return num1*num2

def division(num1, num2):
    if isinstance(num1, float):
        return num1/float(num2)
    return num1/num2

def nthpower(num1, num2):  
    return num1**num2
    

#main function in python
if __name__ == "__main__":
    start()

