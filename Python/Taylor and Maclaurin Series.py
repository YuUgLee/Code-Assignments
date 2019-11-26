from math import *
import math
user=input('Do you want sin or cos?\n')
def sine():
    n=1
    global angle
    angle=float(input('What angle do you want?\n'))
    angle=angle*(pi/180)
    sin=0
    for i in range(5):
        n=(2*i+1)
        sin+=((-1)**i/math.factorial(n))*angle**(2*i+1)
    return sin
def cosine():
    n=1
    global angle
    angle=float(input('What angle do you want?\n'))
    dangle=angle
    angle=angle*(pi/180)
    cos=0
    for k in range(5):
        cos+=((((-1)**k)*(angle**(2*k)))/math.factorial(2*k))
    return cos
if user == 'sin':
    t=sine()
    z=math.sin(angle)
    print(t,'Theirs',z)
elif user == 'cos':
    t=cosine()
    z=math.cos(angle)
    print(t,'Theirs',z)
