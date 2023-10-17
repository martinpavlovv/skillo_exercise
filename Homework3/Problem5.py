number = int(input('Enter the result of 5 + 17: '))

while number != 22:
    if number < 0:
        print('The number should not be negative!')
        number = int(input('Try again:'))
    elif number >= 0 and number < 22:
        print('The number is lower')
        number = int(input('Try again:'))
    elif number > 22:
        print('The number is bigger')
        number = int(input('Try again:'))



print('Correct!')