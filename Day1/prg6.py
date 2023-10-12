my_list =[98,99,83,77,49,62,33]
max = my_list[0]

def S():
    s=0.0
    for i in range(len(my_list)):
       s+=my_list[i]
    return s

def avg():
    av=0.0
    av = S()/len(my_list)
    return av

def per():
    p = 0.0
    p = (S()/(len(my_list)*100))*100
    return p

for i in range(len(my_list)):
    if my_list[i] >= max :
        max = my_list[i]

print(f"Max marks : {max}")
print(f"Sum : {S()}")
print(f"Average : {avg()}")
print(f"Percentage : {per()}")