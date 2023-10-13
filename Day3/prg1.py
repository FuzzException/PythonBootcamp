import tkinter

def button_click() :
    label1.config(text = "Welcome!!")

window = tkinter.Tk()
window.title("1st GUI application")
#adjust size of window - minimum size of window
window.minsize(400,200)
#label1 = tkinter.Label(window,text = "My first GUI Application").grid(column = 20, row = 0)#keyword arguments(text = )
#grid,pack - layout manager
label1 = tkinter.Label(window,text = "My first GUI Application")
label1["text"] = "Hey"
#label1.configure(text = "Hey there!")
label1.pack()

label2 = tkinter.Label(window,text = "Hello, world!!", font = ("Comic Sans Ms",20))
label2.pack()
#label2.configure(font = Font_tuple)

#label1.pack(side = 'bottom')
label1.place(relx = 0.5,rely = 0.5, anchor = tkinter.CENTER)

button = tkinter.Button(window, text = "Enter", command = button_click)
button.pack()


#creates windows
#window.mainloop() - keeps the window running
window.mainloop()