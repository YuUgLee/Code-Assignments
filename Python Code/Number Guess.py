import random
r=random.randint(1,10)
print('You have 3 tries to guess my number')
user_input=int(input('Input your guess:'))
if user_input<0:
    print('Make sure your number is positive')
if user_input > r:
    print('Lower')
    input2=int(input('Input your second guess:'))
    if input2 > r:
        print('Lower')
        input3=int(input('Input your last guess:'))
        if input3==r:
            print('Hooray')
        if (input3>r) or (input3<r):
            print('Sorry you lose')
    if input2 < r:
        print('Higher')
        input3=int(input('Input your last guess:'))
        if input3==r:
            print('Hooray')
        if (input3>r) or (input3<r):
            print('Sorry you lose')
    if input2 == r:
        print('Hooray')
if user_input < r:
    print('Higher')
    input2=int(input('Input your second guess:'))
    if input2 > r:
        print('Lower')
        input3=int(input('Input your last guess:'))
        if input3==r:
            print('Hooray')
        if (input3>r) or (input3<r):
            print('Sorry you lose')
    if input2 < r:
        print('Higher')
        input3=int(input('Input your last guess:'))
        if input3==r:
            print('Hooray')
        if (input3>r) or (input3<r):
            print('Sorry you lose')
    if input2 == r:
        print('Hooray')
if user_input == r:
    print('Hooray')
