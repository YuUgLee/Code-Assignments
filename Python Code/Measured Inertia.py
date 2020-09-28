
time=float(input('Enter average time of measured inertia:'))
h=70.5
r=0.00625
w=15.05
g=9.8
inertia=((w*(r**2))/g)*(((g*time**2)/(2*h))-1)
print('The measured inertia is','%2E' %(inertia))
