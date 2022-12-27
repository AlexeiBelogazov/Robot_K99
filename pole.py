class Pole:
    pole = []
    def __init__(self):
        i = 0
        j = 0
        lis = []
        while i < 30:
            while j < 30:
                lis.append(0)
                j += 1
            self.pole.append(lis)
            i += 1
