import pole
import tkinter
from tkinter import *


class Robot:
    x = 0
    y = 0
    napr = 1
    move_x = 0
    move_y = 0


    def __init__(self, pos_, napr, color,canvas, master=None):


        self.master = master
        self.napr = self.cor_napr(napr)
        self.pos = self.cor_pos(pos_)
        self.napr = napr
        self.x = self.pos[0]
        self.y = self.pos[1]

        self.canvas = canvas
        #creating rectangle
        self.rectangle = self.canvas.create_rectangle(
            self.x-5, self.y-5, self.x+5, self.y+5, fill=color)
        self.canvas.pack()


        self.movement()

    def cor_pos(self, posi):
        pos_r = []
        for pos in posi:
            if pos > 300:
                pos = 300
            elif pos < 20:
                pos = 20
            pos_r.append(pos)

        return pos_r

    def cor_napr(self, napr):
        if napr > 4:
            napr = 1
        elif napr < 1:
            napr = 4
            return napr

    def step(self):
        if self.napr == 1:
            if self.move_x < 3:
                self.move_x += 1
        elif self.napr == 2:
            if self.move_y < 3:
                self.move_y += 1
        elif self.napr == 3:
            if self.move_x > -3:
                self.move_x -= 1
        elif self.napr == 4:
            if self.move_y > -3:
                self.move_y -= 1

    def stop(self):
        if self.move_x > 0:
            self.move_x -= 1
        elif self.move_x < 0:
            self.move_x += 1
        if self.move_y > 0:
            self.move_y -= 1
        elif self.move_y < 0:
            self.move_y += 1



    def left(self):
        if self.napr < 4:
            self.napr += 1
        else:
            self.napr = 1

    def rait(self):
        if self.napr > 1:
            self.napr -= 1
        else:
            self.napr = 4

    def movement(self):

        if self.x >= 300:
            self.canvas.move(self.rectangle, -2, self.move_y)
            self.x += -2
            self.y += self.move_y
        elif self.x <= 20:
            self.canvas.move(self.rectangle, 2, self.move_y)
            self.x += 2
            self.y += self.move_y
        elif self.y >= 250 :
            self.canvas.move(self.rectangle, self.move_x, -2)
            self.x += self.move_x
            self.y += -2
        elif self.y <= 20:
            self.canvas.move(self.rectangle, self.move_x, 2)
            self.x += self.move_x
            self.y += 2
        else:
            self.canvas.move(self.rectangle, self.move_x, self.move_y)
            self.x += self.move_x
            self.y += self.move_y
        self.canvas.after(30, self.movement)

class Bot(Robot):

    def __init__(self, pos_, napr, color,canvas, master=None):
        super().__init__(pos_, napr, color,canvas, master)

    def movement(self):
        if self.x >= 300:
            self.canvas.move(self.rectangle, -2, self.move_y)
            self.x += -2
            self.move_x += -2
            self.y += self.move_y

        elif self.x <= 20:
            self.canvas.move(self.rectangle, 2, self.move_y)
            self.x += 2
            self.move_x += 2
            self.y += self.move_y
        elif self.y >= 250 :
            self.canvas.move(self.rectangle, self.move_x, -2)
            self.x += self.move_x
            self.y += -2
            self.move_y += -2
        elif self.y <= 20:
            self.canvas.move(self.rectangle, self.move_x, 2)
            self.x += self.move_x
            self.y += 2
            self.move_y += 2
        else:
            self.canvas.move(self.rectangle, self.move_x, self.move_y)
            self.x += self.move_x
            self.y += self.move_y
        self.canvas.after(30, self.movement)


def mas2():
    master2 = tkinter.Tk()
    master2.geometry(f"600x600")
    text = Text(master2)
    text.insert(INSERT, "Бабах")

pole_war = pole.Pole(320,380)
master = tkinter.Tk()
master.geometry(f"{pole_war.pole[0]}x{pole_war.pole[1]}")
canvas = Canvas(master)
plyer = Robot([150, 150], 3, "red", canvas, master)
bot1 = Bot([30, 50], 2, "blue", canvas, master)
bot2 = Bot([250, 50], 1, "white", canvas, master)
bot3 = Bot([200, 180], 4, "black", canvas, master)
bot1.step()
bot1.left()
bot1.step()
bot2.step()
bot2.rait()
bot2.step()
bot3.step()
bot3.left()
bot3.step()

if plyer.x == bot1.x:
    if plyer.y == bot1.y:
        mas2()
if plyer.x == bot2.x:
    if plyer.y == bot2.y:
        mas2()
if plyer.x == bot3.x:
    if plyer.y == bot3.y:
        mas2()

master.bind("<KeyPress-Left>", lambda e: plyer.rait())
master.bind("<KeyPress-Right>", lambda e: plyer.left())
master.bind("<KeyPress-Up>", lambda e: plyer.step())
master.bind("<KeyPress-Down>", lambda e: plyer.stop())
master.mainloop()









