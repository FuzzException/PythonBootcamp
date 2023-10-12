import re

def is_valid(ph_no) :
    pattern = "[(]?\d{3}[)]?\s?[-]?\d{3}[-]?\d{4}"
    return re.match(pattern,ph_no) is not None

def main ():
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        ph_no = input("Enter a phone number : ")
        
        if is_valid(ph_no):
            print(f"{ph_no} is valid")
        else :
            print(f"{ph_no} is not valid")
        
if __name__ == "__main__" :
    main()