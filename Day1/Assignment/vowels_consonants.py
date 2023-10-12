str1 = input("Enter a string : ")
vowels = 0
consonants = 0
temp = str1.lower()

for char in temp:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
        vowels+=1
    else :
        consonants+=1
        
print(f"Input string : {str1}\nOccurances of vowels : {vowels}\nOccurances of Consonants : {consonants}")
