import re

def remove_tags(str1):
    #used to perform the substitution, and it replaces all occurrences of HTML tags with nothing, effectively removing them from the input text. 
    removed = re.sub(r'<.*?>','',str1)
    return removed

def main() :
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        str1 = input("Enter string : ")
        print(f"String without HTML tags : {remove_tags(str1)}")

if __name__ == "__main__" :
    main()