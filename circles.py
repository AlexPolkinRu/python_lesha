from tkinter import *

window = Tk()
window.title('Работа с canvas')

canvas = Canvas(window,width=600,height=600,bg="gray",
          cursor="pencil")

canvas.pack()
window.mainloop()