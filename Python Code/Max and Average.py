user = [int(num) for num in input().split()]
max=user[0]
for i in user:
    if max <=i:
        max=i
avg=0
for z in user:
    avg+=z
n=len(user)
avg=avg/n
print(round(avg),max)
