one=input('Enter weight 1:\n')
two=input('Enter weight 2:\n')
three=input('Enter weight 3:\n')
four=input('Enter weight 4:\n')
l=[]
l.append(one)
l.append(two)
l.append(three)
l.append(four)
t=[float(i) for i in l]
print('Weights:',t)
n=len(t)
max=t[1]
avg=0
for i in t:
    avg+=i
avg=avg/n
print()
print('Average weight:', '%0.2f' %(avg))
for i in range(n):
    if max<t[i]:
        max=t[i]
print('Max weight:','%0.2f' %(max))
print()

user=int(input('Enter a list location (1 - 4):\n'))

for i in range(n):
    if user==i:
        print('Weight in pounds:','%0.2f' %(t[i-1]))
        z=t[i-1]/2.2
        print('Weight in kilograms:', '%0.2f' %(z))
print()
t.sort()
print('Sorted list:',t)
