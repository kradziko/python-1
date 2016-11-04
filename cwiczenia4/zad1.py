'''
Losowanie sie 6 niepowtarzajacych sie liczb od 1 do 49
'''
import random

random.seed() # ziarno
liczby = []
for x in range(0, 6):
    x = random.randint(1,49)
    while x in liczby:
        x = random.randint(1,49)
    liczby.append(x)

print liczby



