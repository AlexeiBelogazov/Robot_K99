import pole
import tkinter
from tkinter import *
from threading import Thread
import time
import math
from Robot import Robot
from Bot import Bot







pole_war = pole.Pole(320,380)
master = tkinter.Tk()
#master.geometry(f"{pole_war.pole[0]}x{pole_war.pole[1]}")
canvas = Canvas(master,width=pole_war.pole[0],height=pole_war.pole[1],bg="gray",
          cursor="pencil")
all_bot = []
plyer = Robot([150, 150], 3, "red", canvas, master)
bot1 = Bot([30, 50], 2, "blue", canvas, master)
all_bot.append(bot1)
bot2 = Bot([250, 50], 1, "white", canvas, master)
all_bot.append(bot2)
bot3 = Bot([200, 180], 4, "black", canvas, master)
all_bot.append(bot3)

bot1.step()
bot1.left()
bot1.step()
bot2.step()
bot2.rait()
bot2.step()
bot3.step()
bot3.left()
bot3.step()
print("ok2")
def bax():
    while True:
        time.sleep(0.05)
        for bot in all_bot:
            if (plyer.x > (bot.x - 20) and plyer.x < (bot.x + 20)) and\
                    (plyer.y > (bot.y - 20) and plyer.y < (bot.y + 20)):
                print("БАХПа БАХ")
                canvas.create_text(150, 30,
                                        text="БАХПа БАХ")

print("ok3")
th = Thread(target=bax, args=())
th.start()
print("ok4")

master.bind("<KeyPress-Left>", lambda e: plyer.rait())
master.bind("<KeyPress-Right>", lambda e: plyer.left())
master.bind("<KeyPress-Up>", lambda e: plyer.step())
master.bind("<KeyPress-Down>", lambda e: plyer.stop())
master.mainloop()









