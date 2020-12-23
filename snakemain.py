import numpy as np
from tkinter import *
import keyboard
import time
import random

tk = Tk()
tk.overrideredirect(True)
web_message_buffer = []
tk.minsize(width=620, height=500)
tk.maxsize(width=620, height=500)
WIDTHSCREEN = tk.winfo_screenwidth()
HEIGHTSCREEN = tk.winfo_screenheight()
tk.wm_geometry("+%d+%d" % (int(WIDTHSCREEN / 2 - 310),int(HEIGHTSCREEN / 2 - 250)))
tk["bg"] = "light grey"

canvas = Canvas(tk, bg='black')
canvas.pack()
canvas.place(x=50, y=70, width=520, height=400)

labelrecord = Label(text="0", bg='light grey', font=("Arial", 20))
labelrecord.pack()
labelrecord.place(x=310, y=30)
labelrecord.update()


def close():
    tk.destroy()


butclose = Button(text='×', bg='red', command=close, bd=2, font=("Arial", 20))  # Кнопка закрытия программы
butclose.pack()
butclose.place(x=590, y=5, width=25, height=25)

coordsx = [260]
coordsy = [200]
canvas.create_rectangle(260, 200, 280, 220, fill='red', tag='sneak')

seedX = [0]
seedY = [0]


def randomseed():
    seedX[0] = random.uniform(0, 520)
    deltax = seedX[0] % 20
    seedX[0] = seedX[0] - deltax

    seedY[0] = random.uniform(0, 400)
    deltay = seedY[0] % 20
    seedY[0] = seedY[0] - deltay

    for i in range(len(coordsx)):
        if coordsx[i] == seedX[0] and coordsy[i] == seedY[0]:
            randomseed()
    canvas.delete('seed')
    canvas.create_oval(seedX[0], seedY[0], seedX[0] + 20, seedY[0] + 20, fill='green', tag='seed')


randomseed()
flag = [1]
record = [0]
timerhand = []
timerhand.insert(0, 0)


def move(side):
    flagcrash = False
    if len(coordsx) == 2:
        crashX = coordsx[1]
        crashY = coordsy[1]
    if side == 'a':
        for i in range(len(coordsx)-1):
            coordsx[len(coordsx)-1-i] = coordsx[len(coordsx)-2-i]
            coordsy[len(coordsy)-1-i] = coordsy[len(coordsy)-2-i]
        coordsx[0] = coordsx[0] - 20
        coordsy[0] = coordsy[0]
        if len(coordsx) == 2 and coordsx[0] == crashX and coordsy[0] == crashY:
            flag[0] = 0
            butagain.place(x=235, y=180, width=150, height=40)
    elif side == 'd':
        for i in range(len(coordsx)-1):
            coordsx[len(coordsx)-1-i] = coordsx[len(coordsx)-2-i]
            coordsy[len(coordsy)-1-i] = coordsy[len(coordsy)-2-i]
        coordsx[0] = coordsx[0] + 20
        coordsy[0] = coordsy[0]
        if len(coordsx) == 2 and coordsx[0] == crashX and coordsy[0] == crashY:
            flag[0] = 0
            butagain.place(x=235, y=180, width=150, height=40)
    elif side == 'w':
        for i in range(len(coordsx)-1):
            coordsx[len(coordsx)-1-i] = coordsx[len(coordsx)-2-i]
            coordsy[len(coordsy)-1-i] = coordsy[len(coordsy)-2-i]
        coordsx[0] = coordsx[0]
        coordsy[0] = coordsy[0] - 20
        if len(coordsx) == 2 and coordsx[0] == crashX and coordsy[0] == crashY:
            flag[0] = 0
            butagain.place(x=235, y=180, width=150, height=40)
    elif side == 's':
        for i in range(len(coordsx)-1):
            coordsx[len(coordsx)-1-i] = coordsx[len(coordsx)-2-i]
            coordsy[len(coordsy)-1-i] = coordsy[len(coordsy)-2-i]
        coordsx[0] = coordsx[0]
        coordsy[0] = coordsy[0] + 20
        if len(coordsx) == 2 and coordsx[0] == crashX and coordsy[0] == crashY:
            flag[0] = 0
            butagain.place(x=235, y=180, width=150, height=40)

    for i in range(len(coordsx)-1):
        if coordsx[0] == coordsx[i+1] and coordsy[0] == coordsy[i+1]:
            flag[0] = 0
            butagain.place(x=235, y=180, width=150, height=40)

    if coordsx[0] == seedX[0] and coordsy[0] == seedY[0]:
        coordsx.insert(0, seedX[0])
        coordsy.insert(0, seedY[0])
        randomseed()
        record[0] = record[0] + 1
        labelrecord['text'] = str(record[0])
        labelrecord.place(x=310 - labelrecord.winfo_width()/2, y=30)
        labelrecord.update()

    if coordsx[0] < 0:
        coordsx[0] = 500
    if coordsx[0] == 520:
        coordsx[0] = 0
    if coordsy[0] < 0:
        coordsy[0] = 380
    if coordsy[0] == 400:
        coordsy[0] = 0


def brain():
    side = ' '
    while flag[0] == 1:
        if keyboard.is_pressed('a'):
            side = 'a'
        elif keyboard.is_pressed('d'):
            side = 'd'
        elif keyboard.is_pressed('w'):
            side = 'w'
        elif keyboard.is_pressed('s'):
            side = 's'

        time.sleep(0.01)
        timerhand[0] = timerhand[0] + 1

        if timerhand[0] % 10 == 0:
            move(side)

            canvas.delete('sneak')
            for i in range(len(coordsx)):
                canvas.create_rectangle(coordsx[i], coordsy[i], coordsx[i] + 20, coordsy[i] + 20, fill='red',
                                        tag='sneak')
            canvas.update()



def againstart():
    butagain.place(x=0, y=0, width=0, height=0)
    flag[0] = 1
    record[0] = 0
    labelrecord['text'] = str(0)
    coordsx.clear()
    coordsy.clear()
    coordsx.insert(0, 260)
    coordsy.insert(0, 200)
    canvas.create_rectangle(260, 200, 280, 220, fill='red', tag='sneak')
    brain()


butagain = Button(text='TRY AGAIN', bg='blue', command=againstart, bd=2, font=("Arial", 14))
butagain.pack()
butagain.place(x=0, y=0, width=0, height=0)

brain()
tk.mainloop()
