import tkinter
import random

def display() :
    
    n = int(ent.get())
    str1 = ""
    letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    for i in range(n) :
        temp = []
        temp.append(random.choice(letters))
        temp.append(random.choice(numbers))
        temp.append(random.choice(symbols))
        str1 = str1 + random.choice(temp)
            
    result.config(text = f"Suggested password : {str1}")
    #print(f"Hello, {name}")

window = tkinter.Tk()
window.minsize(400,200)
window.title("Password Generator")

label1 = tkinter.Label(text = "Enter length of password : ",font = ("Comic Sans Ms",13))
label1.pack()

ent = tkinter.Entry(window)
ent.pack()

result = tkinter.Label(text = "",font = ("Comic Sans Ms",20))
result.place(relx = 0.5,rely = 0.5, anchor = tkinter.CENTER)
result.pack()

button = tkinter.Button(text = "Enter", command = display)
button.pack()

window.mainloop()