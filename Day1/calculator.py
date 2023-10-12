def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return x / y
def calc():    
    while True:
        print("Enter\n\t\t1 - Add\n\t\t2 - Subtract\n\t\t3 - Multiply\n\t\t4 - Division\n\t\t5 - Quit\n")
        ch = int(input("Enter your choice : "))
        if ch == 5:
            break
        
        else :
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number :"))
            
            if ch == 1:
                print(f"Result : {add(num1,num2)}")
            elif ch == 2:
                print(f"Result : {sub(num1,num2)}")
            elif ch == 3:
                print(f"Result : {mul(num1,num2)}")
            elif ch == 4:
                print(f"Result : {div(num1,num2)}")
            else:
                printf("Invalid input")
                
calc()