n=int(input())
if (n<20) or (n>98):
    print('Input must be 20-98')
else:
    print(n)
    while n%11!=0:
        n=(n-1)
        print(n)
