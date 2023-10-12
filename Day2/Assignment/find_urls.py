import re

def find_url(str1) :
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(pattern, str1)
    return urls

def main ():
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        str1 = input("Enter a String : ")
        
        urls = find_url(str1)
        print("URLs : ")
        
        for u in urls:
            print(u)
        
if __name__ == "__main__" :
    main()