'''
CECS 100
Project 4
Name: Newton Bao
I.D.#:018286708
Start Date: 4-16-19
End Date:
Topic: Pareto Chart
'''

import matplotlib.pyplot as pareto
import numpy as ny

x=[1,2,3,4]
y=[100,75,53,42]
l = ny.arange(0., 5., 0.2)

width=1
pareto.bar(x,y,width, color=['y','0','C','b'])
pareto.xlabel('Causes')
pareto.ylabel('Frequency')
pareto.title('Pareto chart of -----')
pareto.ylim(0,200)
pareto.plot(l, l, 'r--', l, l**4, 'C', l, l**3, 'bs', l, l**5, 'g^')

xc=[0,1,2,3,4,5,6]
yc=[0,60,100,130,150,170,181]
pareto.plot(xc,yc,marker ='o')
pareto.plot(xc, yc, label='Original Line')
pareto.legend()


'''
CECS 100
Project 4
Name: Newton Bao
I.D.#:018286708
Start Date: 4-16-19
End Date:
Topic: Pareto Chart
'''

import matplotlib.pyplot as pareto
import numpy as ny

x=[1,2,3,4]
y=[100,75,53,42]
l = ny.arange(0., 5., 0.2)

width=1
pareto.bar(x,y,width, color=['y','0','C','b'])
pareto.xlabel('Causes')
pareto.ylabel('Frequency')
pareto.title('Pareto chart of -----')
pareto.ylim(0,200)
pareto.plot(l, l, 'r--', l, l**4, 'C', l, l**3, 'bs', l, l**5, 'g^')

xc=[0,1,2,3,4,5,6]
yc=[0,60,100,130,150,170,181]
pareto.plot(xc,yc,marker ='o')
pareto.plot(xc, yc, label='Original Line')
pareto.legend()
