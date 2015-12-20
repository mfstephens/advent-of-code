class Reindeer(object):
    def __init__(self, name, speed, travelDuration, restDuration):
        self.name = name
        self.speed = speed
        self.travelDuration = travelDuration
        self.restDuration = restDuration

        self.distance = 0
        self.restTimeLeft = 0
        self.travelTimeLeft = travelDuration
        self.points = 0

    def advanceReindeer(self):
        if self.travelTimeLeft != 0:
            self.distance += self.speed
            self.travelTimeLeft -= 1
            if self.travelTimeLeft == 0:
                self.restTimeLeft = self.restDuration
            return

        if self.restTimeLeft != 0:
            self.restTimeLeft -= 1
            if self.restTimeLeft == 0:
                self.travelTimeLeft = self.travelDuration
            return

def day14():
    dancer = Reindeer('Dancer', 27, 5, 132)
    cupid = Reindeer('Cupid', 22, 2, 41)
    rudolph = Reindeer('Rudolph', 11, 5, 48)
    donner = Reindeer('Donner', 28, 5, 134)
    dasher = Reindeer('Dasher', 4, 16, 55)
    blitzen = Reindeer('Blitzen', 14, 3, 38)
    prancer = Reindeer('Prancer', 3, 21, 40)
    comet = Reindeer('Comet', 18, 6, 103)
    vixen = Reindeer('Vixen', 18, 5, 84)

    fleet = [dancer, cupid, rudolph, donner, dasher, blitzen, prancer, comet, vixen]

    maxDistance = 0
    for second in range(2503):
        for reindeer in fleet:
            reindeer.advanceReindeer()
            if reindeer.distance > maxDistance:
                maxDistance = reindeer.distance

        for reindeer in fleet:
            if reindeer.distance == maxDistance:
                reindeer.points += 1

    winner = max(fleet, key = lambda f: f.points)
    print winner.points

day14()
