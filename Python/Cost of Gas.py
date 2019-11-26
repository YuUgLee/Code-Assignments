car1=int(input("Enter car 1's mileage:"))
car2=int(input("Enter car 2's mileage:"))
gas1=float(input("Enter car 1's average gas cost per gallon:"))
gas2=float(input("Enter car 2's average gas cost per gallon:"))
mile=int(input('How many miles do you drive a month:'))
cost1=((mile*12)*gas1)/car1
cost2=((mile*12)*gas2)/car2
if cost1>cost2:
    save=cost1-cost2
    print('Car 1 will save','%0.2f' %(save),'in a year')
elif cost2>cost1:
    save=cost2-cost1
    print('Car 2 will save','%0.2f' %(save),'in a year')
elif cost2==cost1:
    print('The two cars cost the same')
