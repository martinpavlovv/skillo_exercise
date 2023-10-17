import random

random_number = random.randint(1,10)

while True:
    user_number = int(input())
    if user_number > random_number:
        print('Too high')
    elif user_number < random_number:
        print('Too low')
    else:
        print('Congrats, you guess the number')
