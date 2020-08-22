import random

home = "home"

infectionRate = 0.3

minPeople = 50
maxPeople = 200
amountOfPeople = random.randint(minPeople,maxPeople)


minDistance = 1
maxDistance = 3
actualDistance = random.randint(minDistance,maxDistance)

time = 16


places = [
    "market","home","club","office","school","doctor","cinema"
]

random.shuffle(places)

class Person():
    def __init__(self,name,age):
        self.state = 0
        self.name = name
        self.age = age
        self.position = home
        self.infected = False
        self.wears_masks = True

    def moved(self):
        random.shuffle(places)
        self.position = places[0]

    def check_at_home(self):
        if position is home:
            infectionRate = 0
        else:
            infectionRate = 0.3
    
        
