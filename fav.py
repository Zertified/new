import Variables as v 
import time
import warnings
import random

warnings.filterwarnings('ignore')

deadcount = 0
recovered_count = 0
check_wear_masks = random.randint(v.min_prob_masks,v.max_prob_masks)


population = []

for i in range(v.amountOfPeople):
    person = v.Person()
    population.append(person)

population[0].state = 1
population[0].infected = True


for day in range(v.days):
    for hour in range(v.hours):
        if hour <= 8:
            person.position = v.places[0]
        
        else:
            for person in population:
                if check_wear_masks == 1:
                    v.infectionRate * 5
                    if person.position == v.home:
                        v.infectionRate = 0
            
            for place in v.places[1:]:
                for person in person.places:
                    if population[0] in person.places:
                        if v.actualDistance < 2 and check_wear_masks == 1:
                            person.infected = True
                            person.state = 1
                            v.infectedPeople +=1
                        elif v.actualDistance >=2 and check_wear_masks == 2:
                            if person.age <= 13:
                                v.infectionRate = 0.1
                            



        
        

