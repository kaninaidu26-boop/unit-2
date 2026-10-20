class bot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery
        self.log = []

    def status(self):
        print(self.name, "Battery:", self.battery)

    def record(self, event):
        self.log.append(event)


r1 = bot("Nova", 90)
r2 = bot("Bolt", 70)

r1.status()
r2.status()

r1.record("Started")
r2.record("Moving")

print("Nova log:", r1.log)
print("Bolt log:", r2.log)
