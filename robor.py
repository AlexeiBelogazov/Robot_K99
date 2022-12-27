class Robot:
    x = 0
    y = 0
    napr = 1

    def __init__(self, pos_x, pos_y, napr):
        self.y = self.cor_pos(pos_y)
        self.x = self.cor_pos(pos_x)
        self.napr = self.cor_napr(napr)
        self.x = pos_x
        self.y = pos_y
        self.napr = napr

    def cor_pos(self, pos):
        if pos > 30:
            pos = 30
        elif pos < 0:
            pos = 0
            return pos

    def cor_napr(self, napr):
        if napr > 4:
            napr = 4
        elif napr < 1:
            napr = 1
            return napr

    def step(self):
        if self.napr == 1:
            if self.y < 30:
                self.y += 1
        if self.napr == 2:
            if self.x < 30:
                self.x += 1
        if self.napr == 3:
            if self.y > 0:
                self.y -= 1
        if self.napr == 1:
            if self.x > 0:
                self.x -= 1

    def left(self):
        if self.napr < 4:
            self.napr += 1

    def rait(self):
        if self.napr > 1:
            self.napr -= 1

