 '''
CECS 100
Project 5
Name: Newton Bao
I.D.#:018286708
Date: May 2, 2019
'''
import numpy as base
x=base.array([[1,3],[-2,4]])

print(x)
a=base.array([[2,1,0,3],[-1,0,2,4],[4,-2,7,0]])
print(a)
b=base.array([[-4,3,5,1],[2,2,0,-1],[3,2,-4,5]])
r=a+b
print(r)
A=base.array([[1,2,4],[2,6,0]])
print(A)
B=base.array([[4,1,4,3],[0,-1,3,1],[2,7,5,2]])
print(B)
C=base.dot(A,B)
print("A times B with multiplication is", C)


