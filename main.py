import robor
import pole
import keyboard


pole_war = pole.Pole()
plyer = robor.Robot(15, 15, 1)

print(pole_war.pole[15][15])
pole_war.pole[15][15] = 1
pole_war.pole[16][15] = 1
pole_war.pole[15][16] = 1
print(pole_war.pole[15][15])

#while True:
#    print(pole_war.pole)







