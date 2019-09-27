pts=int(input('How many points did you earn in the class? '))
total=int(input('How many points is the class out of? '))
grade=pts/total
if grade >= 0.9:
    print('You earned an A.')
elif grade >= 0.8:
    print('You earned a B.')
elif grade >= 0.7:
    print('You earned a C.')
elif grade >= 0.6:
    print('You earned a D.')
elif grade >= 0:
    print('You earned a F.')
