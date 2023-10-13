import tkinter

def display() :
    miles = ent.get()
    km = float(miles)*1.609
    result.config(text = f"In Miles : {miles} miles\nIn Kilometers : {km: .2f} km(s)")
    #print(f"Hello, {name}")

window = tkinter.Tk()
window.minsize(400,200)
window.title("Miles to Km")

label1 = tkinter.Label(text = "Enter distance in miles : ",font = ("Comic Sans Ms",13))
label1.grid(row = 0, column = 0)

ent = tkinter.Entry(window)
ent.grid(row = 0, column = 1)

result = tkinter.Label(text = "",font = ("Comic Sans Ms",20))
result.place(relx = 0.5,rely = 0.5, anchor = tkinter.CENTER)
result.grid(row = 1, column = 0, columnspan = 2)

button = tkinter.Button(text = "Enter", command = display)
button.grid(row = 2, column = 0, columnspan = 2)

window.mainloop()
    

