import tkinter
print('hold to draw')
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=750, height=500, bg='white')
canvas.pack()
lastx, lasty = 0,0
colour = 'black'
def store_position(event):
    global lastx, lasty
    lastx = event.x
    lasty = event.y
def on_click(event):
    store_position(event)
def on_drag(event):
    canvas.create_line(lastx, lasty, event.x, event.y, fill = colour, width = 3)
    store_position(event)
canvas.bind('<Button-1>', on_click)
canvas.bind('<B1-Motion>', on_drag)

window.mainloop()