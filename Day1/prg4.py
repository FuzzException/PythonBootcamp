name =[]
age = []

for i in range(2) :
    name1 = input("Enter name : ")
    age1 = int(input("Enter age : "))
    name.append(name1)
    age.append(age1)

max_index = age.index(max(age))

print(f"My name is {name[max_index]} and age is {age[max_index]}")
