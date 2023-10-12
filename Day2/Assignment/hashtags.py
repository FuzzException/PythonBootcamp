import re

def extract_hashtag(str1):
    pattern = r'#\w+'
    hashtags = re.findall(pattern, str1)
    return hashtags

def main ():
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        str1 = input("Enter a String : ")
        
        hstgs = extract_hashtag(str1)
        print("Hashtags : ")
        
        for ht in hstgs:
            print(ht)
        
if __name__ == "__main__" :
    main()