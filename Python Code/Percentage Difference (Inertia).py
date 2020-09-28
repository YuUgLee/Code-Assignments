exp=float(input('Enter experimental inertia:'))
the=float(input('Enter theoretical inertia:'))

deviation=((the-exp)/.5*(the+exp))*100
print('The deviation is','%2E' %(deviation))
