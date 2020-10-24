import random

def get_username():
    names1 = ['Brilliant','Amazing','Glad','Atrocious','Angry','Disgusted']
    names2 = ['Snake','Panda','Giraffe','Hen','Cat','Goat']

    names1_shuffle = random.shuffle(names1)
    name1 = random.choice(names1)
    names2_shuffle = random.shuffle(names2)
    name2 = random.choice(names2)

    username = name1+name2

    return username

print(get_username())
