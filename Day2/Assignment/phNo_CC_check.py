import re

def country_code(no) :
    cc = {'+1' : 'USA',
          '+971' : 'UAE',
          '+44' : 'UK',
          '+52' : 'Mexico',
          '+91' : 'India',
          '+86' : 'China'
          }
    if no in cc.keys() :
        print(f"Country code valid!! {cc[no]}")
    
    else :
        print("Invalid Country code!!")

def is_valid(ph_no) :
    pattern = "[(]?\d{3}[)]?\s?[-]?\d{3}[-]?\d{4}"
    return re.match(pattern,ph_no) is not None

def main ():
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        ph_no = input("Enter a phone number : ")
        l = 0
        if ord(ph_no[0]) == 43 :
                l+=1
        for i in range(len(ph_no)) :
            #if char.isnumeric == true
            char = ph_no[i]
            if ord(char)>=48 and ord(char)<=57 :
                l+=1
        
        if l<10 :
            print("Invalid Number")
        
        elif l == 10 :
            if is_valid(ph_no):
                print(f"{ph_no} is valid")
            else :
                print(f"{ph_no} is not valid")
        else :
            con_code = ph_no[0:(l-10)]
            no = ph_no[(l-10):l]
            
            if is_valid(ph_no):
                print(f"{ph_no} is valid")
            else :
                print(f"{ph_no} is not valid")
                
            country_code(ph_no)
        
if __name__ == "__main__" :
    main()