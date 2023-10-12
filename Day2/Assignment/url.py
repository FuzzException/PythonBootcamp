import re

def extract_domain(url):
    pattern = r'^https?://(www\.)?([^/]+)'
    check = re.search(pattern, url)
    if check:
        print(f"Domain : {check.group(2)}")

    else:
        print("No domain found")


def main():
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        url = input("Enter the url :")
        extract_domain(url)
    
if __name__ == "__main__" :
    main()