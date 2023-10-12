import re

def is_strong(pswd):
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.match(pattern,pswd) is not None

def main() :
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        password = input("Enter a password : ")
        
        if is_strong(password):
            print(f"{password} is strong")
        else :
            print(f"{password} is not strong")
        
if __name__ == "__main__" :
    main()