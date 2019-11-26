from math import *
t=format(pi, '.81f')
list = [pi]
for i in range(1,6):
    value=pi**i
    if value == (pi**5):
        print('%0.13f' %(value))
    else:
        print('%0.17f' %(value),end='')
print()
for z in range(3):
    print('*'*16, end='                       ')
print()
for i in range(2,6):
    value=pi**i
    print('%0.6f' %(value),end='                  ')
print()
for i in range(2,6):
    value=pi*i
    print('%0.6f' %(value),end='                   ')

