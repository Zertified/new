import random

home = "home"

infectionRate = 0.3

minPeople = 50
maxPeople = 200
amountOfPeople = random.randint(minPeople,maxPeople)
infectedPeople = 0

prob_infected_someone = 1
min_prob_masks = 1
max_prob_masks = 2

minDistance = 1
maxDistance = 3
actualDistance = random.randint(minDistance,maxDistance)

days = 30
hours = 24


places = [
    "home","club","office","school","doctor","cinema","market"
]

random.shuffle(places)

class Person():
    def __init__(self):
        self.state = 0
        self.name = name
        self.age = age
        self.position = home
        self.infected = infected

    def moved(self):
        random.shuffle(places)
        self.position = places[0]

    
    def isInfected(self):
        if infected == True:
            infectedPeople +=1
        
        elif self.state == 1:
            infectedPeople += 1
        
        return infectedPeople  # Amount of infected people


class Place():
    pass



    
    
        
