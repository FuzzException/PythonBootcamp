import tkinter

def display() :
    name = ent.get()
    result.config(text = f"Hello, {name}")
    #print(f"Hello, {name}")

window = tkinter.Tk()
window.minsize(400,200)
window.title("Submit Name")

label1 = tkinter.Label(text = "Enter your name : ",font = ("Comic Sans Ms",13))
label1.pack()

ent = tkinter.Entry(window)
ent.pack()

result = tkinter.Label(text = "",font = ("Comic Sans Ms",20))
result.place(relx = 0.5,rely = 0.5, anchor = tkinter.CENTER)
result.pack()

button = tkinter.Button(text = "Submit", command = display)
button.pack()

window.mainloop()
    
