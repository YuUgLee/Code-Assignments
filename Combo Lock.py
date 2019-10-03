first=int(input('What is the first number in the combination?' ))
second=int(input('What is the second number in the combination?' ))
third=int(input('What is the third number in the combination? '))
i=2
oneans=40 - first
twoans=second-first
threeans=second+(40-third)
while i < 4:
    one_lock=int(input('Turn the lock clockwise by how much?'))
    two_lock=int(input('Turn the lock counterclockwise by how much?'))
    third_lock=int(input('Turn the lock clockwise by how much?'))
    if (one_lock==oneans)and(two_lock==twoans)and(third_lock==threeans):
        print('Correct! You have won an A in CECS 174.')
        i=6
    else:
        print('Sorry, that sequence was incorrect.')
        i=2



