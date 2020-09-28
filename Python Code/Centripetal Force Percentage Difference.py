val1=float(input("Enter theoretical centripetal: "))
val2=float(input("Enter experimental centripetal: "))
totalval=abs(val1-val2)
deviation=(totalval/((0.5)*(val1+val2)))*100
print(deviation)
