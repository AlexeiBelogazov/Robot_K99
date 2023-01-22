import Robot
class Bot(Robot.Robot):

    def __init__(self, pos_, napr, color, canvas, pole, master=None):
        super().__init__(pos_, napr, color, canvas, pole, master)

    def movement(self):
        if self.x >= (self.pole[0] - 20):
            self.canvas.move(self.rectangle, -5, self.move_y)
            self.x += -5
            #self.move_x += -2
            self.stop()
            self.left()
            self.step()
            self.step()

            self.y += self.move_y

        elif self.x <= 20:
            self.canvas.move(self.rectangle, 5, self.move_y)
            self.x += 5
            #self.move_x += 2
            self.stop()
            self.step()
            self.left()
            self.step()

            self.y += self.move_y
        elif self.y >= (self.pole[1] - 20) :
            self.canvas.move(self.rectangle, self.move_x, -5)
            self.x += self.move_x
            self.y += -5
            #self.move_y += -2
            self.stop()
            self.step()
            self.left()
            self.step()

        elif self.y <= 20:
            self.canvas.move(self.rectangle, self.move_x, 5)
            self.x += self.move_x
            self.y += 5
            #self.move_y += 2
            self.stop()
            self.step()
            self.left()
            self.step()

        else:
            self.canvas.move(self.rectangle, self.move_x, self.move_y)
            self.x += self.move_x
            self.y += self.move_y

            #print(self.x,self.y)
        self.canvas.after(50, self.movement)