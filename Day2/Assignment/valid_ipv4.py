import re

def match_valid_ipv4(str1) :
    pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.findall(pattern,str1)

def main() :
    while True :
        ch = input("Enter 'exit' to exit ")
        
        if ch == "exit" :
            return
        
        str1 = input("Enter string : ")
        ipv4_addresses = match_valid_ipv4(str1)
        print("Matched ipv4 addresses : ")
        for ipv4 in ipv4_addresses :
            print(ipv4)
            
#Valid IPs: 192.168.1.1, 10.0.0.1, 255.255.255.255. Invalid: 256.0.0.1, 192.168.0.256           
           
if __name__ == "__main__" :
    main()