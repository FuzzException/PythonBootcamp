import re

def match_dates(date):
    #MM/DD/YYYY
    #pattern = r'\b(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])\/(?:\d{1,3}|202[0-3])$\b'
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, date)

def main():
    while True :
        ch = input("Enter 'exit' to exit : ")
        
        if ch == "exit" :
            return
        
        txt = input("Enter :")
        dates = match_dates(txt)
        
        for date in dates :
            print(date)
    
if __name__ == "__main__" :
    main()