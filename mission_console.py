class Robot:
    def __init__(self, name):
        self.name = name
        self.speed = 5

r = Robot("Nova")

print("Robot data:", r.__dict__)

del r.speed

print("After deleting speed:", r.__dict__)

#----------------------------------

class Sensor:
    def __init__(self, sid):
        self.sid = sid
        print("Sensor created:", self.sid)

s1 = Sensor(10)
s2 = s1

del s1

print("Sensor still works:", s2.sid)

del s2

print("Program ended")
