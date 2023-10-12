class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2

    def subtract(self, num1, num2):
        self.result = num1 - num2

    def multiply(self, num1, num2):
        self.result = num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            self.result = num1 / num2
        else:
            print("Error: Division by zero")

def main():
    calculator = Calculator()

    while True:
        print("Options:")
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        print("Enter 5 to quit the calculator")

        user_input = int(input("Your choice : "))

        if user_input == 5:
            break
        elif user_input in [1,2,3,4]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if user_input == "add":
                calculator.add(num1, num2)
                print("Result:", calculator.result)
                
            elif user_input == "subtract":
                calculator.subtract(num1, num2)
                print("Result:", calculator.result)
                
            elif user_input == "multiply":
                calculator.multiply(num1, num2)
                print("Result:", calculator.result)
                
            elif user_input == "divide":
                calculator.divide(num1, num2)
                print("Result:", calculator.result)
                
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
