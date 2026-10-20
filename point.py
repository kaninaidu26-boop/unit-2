class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Position:", self.x, self.y)


p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()
p2.show()

#------------------------------------

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def status(self):
        if self.battery < 20:
            print(self.name, "Battery low")
        else:
            print(self.name, "Ready")

r1 = Robot("Nova", 10)
r2 = Robot("Bolt", 80)

r1.status()
r2.status()
