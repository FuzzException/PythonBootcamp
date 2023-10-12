num = int(input("Enter a number : "))
print(f"Multiplication table of {num}")
for i in range (10) :
    print(f"{num}\tx\t{i+1}\t=\t{num*(i+1)}")