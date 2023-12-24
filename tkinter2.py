import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text='0', bg='white', width=10)
button.pack(padx=100, pady=100)
clickCount = 0
def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    button.configure(text=clickCount)
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()