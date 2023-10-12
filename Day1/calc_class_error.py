class Calculator:
    def __init__(self):
        self.result = 0

    def add(num1, num2):
        self.result = num1 + num2
        print("Result:", self.result())

    def subtract(num1, num2):
        self.result = num1 - num2
        print("Result:", self.result())

    def multiply(num1, num2):
        self.result = num1 * num2
        print("Result:", self.result())

    def divide(self, num):
        if num == 0:
            print("Error: Division by zero")
        else:
            self.result = num1 / num2
            print("Result:", self.result())
            
def main():
    calculator = Calculator()

    while True:
        print("Options:")
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 to quit the calculator")

        ch = int(input("Your choice : "))
        num1 = float(input("Enter a number 1 : "))
        num2 = float(input("Enter a number 2 : "))
        if ch == 1 :
            calculator.add(num1,num2)
            
        elif ch == 2 :
            calculator.subtract(num1,num2)
    
        elif ch == 3:
            calculator.multiply(num1,num2)
            
        elif ch == 4:
            calculator.divide(num1,num2)
        
        elif ch == 5:
            return
            
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()