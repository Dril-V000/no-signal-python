from tkinter import *

import random

WIDTH, HEIGHT = 900, 500
print('for normal mode : 1 , for crazy mode : 2')


root = Tk()


colors = ["lime", "cyan", "magenta", "yellow", "orange", "deep pink", "red"]
can = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
can.pack()

txt = can.create_text(110, 30, text='No signal',
                      fill='lime', font=('Consolas', 32, 'bold'))

def move_txt2():
    global dx, dy

    x1, y1, x2, y2 = can.bbox(txt)

    if x2 >= WIDTH or x1 <= 0:
        dx = -dx
        can.itemconfig(txt, fill=random.choice(colors))

    if y2 >= HEIGHT or y1 <= 0:
        dy = -dy
        can.itemconfig(txt, fill=random.choice(colors))

    can.move(txt, dx, dy)
    root.after(30, move_txt2)

def move_txt():

    x1, y1, x2, y2 = can.bbox(txt)


    dx = random.randint(-100, 100)
    dy = random.randint(-100, 100)


    if x1 + dx < 0: dx = abs(dx)
    if x2 + dx > WIDTH: dx = -abs(dx)
    if y1 + dy < 0: dy = abs(dy)
    if y2 + dy > HEIGHT: dy = -abs(dy)


    if random.random() < 0.5:  #
        can.itemconfig(txt, fill=random.choice(colors))

    can.move(txt, dx, dy)

    root.after(10, move_txt)
try:
    ansr=int(input('so 1 or 2 ?? : '))
    if ansr==1:

        while True:
            try:
                speed = int(input('how much speed : '))
                if speed > 30 or speed <= 0:
                    print('chill man ')
                else:
                    break
            except ValueError:
                exit('not a number')
        dx, dy = speed, speed
        move_txt2()
    elif ansr==2:
        move_txt()
    else:
        exit('why man')
except ValueError:
    exit('@#$%!&*?!')



root.mainloop()

