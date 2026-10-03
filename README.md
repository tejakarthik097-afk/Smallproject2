#Small time game
import time
for n in range(10,0,-1):
    print(n)
    time.sleep(0.5)
print("Iam Doom!")


#Time Loop
import time
from itertools import cycle
Avengers = [
    ("Tony Father: Tony! I build this for you", 1),
    ("You will change the World", 1),
    ("What is and always be will,", 1),
    ("My Greatest Creation Is You", 1),
    ("Tony : Iam...Iam IronMan, Snap", 1),
]
Tony = cycle(Avengers)
while True:
    a,i = next(Tony)
    print(a)
    time.sleep(1)
