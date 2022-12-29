import math

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
        if self.napr == 1:
            self.rectangle = canvas.create_polygon([self.x-5,self.y-5],[self.x-5,self.y+5],[self.x+5,self.y], fill=color)
            self.point=[[self.x-5,self.y-5],[self.x-5,self.y+5],[self.x+5,self.y]]


        if self.napr == 2:
            self.rectangle = canvas.create_polygon([self.x-5,self.y-5],[self.x+5,self.y-5],[self.x,self.y+5], fill=color)
            self.point=[[self.x-5,self.y-5],[self.x+5,self.y-5],[self.x,self.y+5]]
        if self.napr == 3:
            self.rectangle = canvas.create_polygon([self.x+5,self.y-5],[self.x+5,self.y+5],[self.x-5,self.y], fill=color)
            self.point = [[self.x+5,self.y-5],[self.x+5,self.y+5],[self.x-5,self.y]]
        if self.napr == 4:
            self.rectangle = canvas.create_polygon([self.x-5,self.y+5],[self.x+5,self.y+5],[self.x,self.y-5], fill=color)
            self.point = [[self.x-5,self.y+5],[self.x+5,self.y+5],[self.x,self.y-5]]
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
        if self.napr == 1:
            points=[[self.x-5,self.y-5],[self.x-5,self.y+5],[self.x+5,self.y]]
        if self.napr == 2:
            points=[[self.x-5,self.y-5],[self.x+5,self.y-5],[self.x,self.y+5]]
        if self.napr == 3:
            points = [[self.x+5,self.y-5],[self.x+5,self.y+5],[self.x-5,self.y]]
        if self.napr == 4:
            points = [[self.x-5,self.y+5],[self.x+5,self.y+5],[self.x,self.y-5]]
        if self.napr < 4:
            self.napr += 1
        else:
            self.napr = 1
        self.rotate(90,points, (self.x, self.y))

    def rait(self):
        if self.napr == 1:
            points=[[self.x-5,self.y-5],[self.x-5,self.y+5],[self.x+5,self.y]]
        if self.napr == 2:
            points=[[self.x-5,self.y-5],[self.x+5,self.y-5],[self.x,self.y+5]]
        if self.napr == 3:
            points = [[self.x+5,self.y-5],[self.x+5,self.y+5],[self.x-5,self.y]]
        if self.napr == 4:
            points = [[self.x-5,self.y+5],[self.x+5,self.y+5],[self.x,self.y-5]]
        if self.napr > 1:
            self.napr -= 1
        else:
            self.napr = 4
        print(self.point)
        self.rotate(-90,points, (self.x, self.y))

    def rotate(self, angle,points, center):

        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        print(points)
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
            print(new_points)
        self.canvas.coords(self.rectangle, int(new_points[0][0]),int(new_points[0][1]), int(new_points[1][0]),int(new_points[1][1]), int(new_points[2][0]),int(new_points[2][1]))
        #self.canvas.coords(self.rectangle, new_points[0], new_points[1],new_points[2])
        #self.canvas.coords(self.rectangle, new_points)
        self.point = new_points



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
        #print(self.x, self.y)
        self.canvas.after(50, self.movement)