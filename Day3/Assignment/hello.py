import tkinter as tk
    
window = tk.Tk()
window.minsize(400,200)
window.title("Greeting")

result = tk.Label(text = "Hello, World",font = ("Comic Sans Ms",20))
result.place(relx = 0.5,rely = 0.5, anchor = tk.CENTER)
result.pack()

window.mainloop()
    