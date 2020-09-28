n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))

small=min(l)
ans=[num-small for num in l]
for t in ans:
    print(t)
