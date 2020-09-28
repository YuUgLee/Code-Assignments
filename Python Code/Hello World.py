name=input('Enter your full name:\n')
bat=int(input('Enter the number of at bats:\n'))
single=int(input('Enter the number of singles:\n'))
double=int(input('Enter the number of doubles:\n'))
triple=int(input('Enter the number of triples:\n'))
run=int(input('Enter the number of home runs:\n'))
total=single+double+triple+run
avg=total/bat
singlee=single
doublee=double*2
triplee=triple*3
runn=run*4
slug=(singlee+doublee+triplee+runn)/bat
print('The player',name,'had:',total)
print(single,'singles,',double,'doubles,',triple,'triples,',run,'homeruns,')
print('his batting average was','%0.3f' %(avg))
print('his slugging percentage was','%0.3f' %(slug))
