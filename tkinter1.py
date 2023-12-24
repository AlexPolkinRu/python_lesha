import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text='zero', bg='green', width=10)
button.pack(padx=100, pady=100)
clickCount = 0
def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text='one')
    elif clickCount == 2:
        button.configure(text='two')
    elif clickCount ==3:
        button.configure(text='three')
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()