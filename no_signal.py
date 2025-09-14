from tkinter import *
import random

WIDTH, HEIGHT = 900, 500


root = Tk()
while True:
    try:
        speed = int(input('how much speed : '))
        if speed>30 or speed<=0:
            print('chill man ')
        else:
            break
    except ValueError:
        exit('not a number')
dx, dy = speed, speed

colors = ["lime", "cyan", "magenta", "yellow", "orange", "deep pink", "red"]

can = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
can.pack()

txt = can.create_text(110, 30, text='No signal',
                      fill='lime', font=('Consolas', 32, 'bold'))

def move_txt():
    global dx, dy

    x1, y1, x2, y2 = can.bbox(txt)

    if x2 >= WIDTH or x1 <= 0:
        dx = -dx
        can.itemconfig(txt, fill=random.choice(colors))

    if y2 >= HEIGHT or y1 <= 0:
        dy = -dy
        can.itemconfig(txt, fill=random.choice(colors))

    can.move(txt, dx, dy)
    root.after(30, move_txt)

move_txt()
root.mainloop()
