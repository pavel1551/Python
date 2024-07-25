def say_hello():
    print("Hello")

say_hello()

def say_hello2(name):
    print("Привет", name)
say_hello2('Den')
say_hello2('Pavel')
# say_hello2(input("Введи имя "))

import random
def lottery():
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win = random.choice(tickets)
    return win

print(lottery())