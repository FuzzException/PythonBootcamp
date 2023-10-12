import re

def extract_nos(str1):
    pattern = r'\b\d+\b'
    nums = re.findall(pattern, str1)
    return nums

def main ():
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        str1 = input("Enter a String : ")
        
        numbers = extract_nos(str1)
        print("Numbers : ")
        
        for n in numbers:
            print(n)
        
if __name__ == "__main__" :
    main()