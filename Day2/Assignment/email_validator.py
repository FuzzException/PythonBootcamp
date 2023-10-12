import re

def is_valid(email) :
    pattern = "\w*.?\w*@(?!hotmail|yahoo)\w*.*[com|org|in]"
    return re.match(pattern,email) is not None

def main ():
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        email = input("Enter a mail ID : ")
        
        if is_valid(email):
            print(f"{email} is valid")
        else :
            print(f"{email} is not valid")
        
if __name__ == "__main__" :
    main()