def swap_values(x,y):
    z=''
    t=x
    x=y
    y=t
    z=z+str(x)+' '
    z=z+str(y)
    return z

if __name__ == '__main__':
    val1=int(input())
    val2=int(input())
    print(swap_values(val1,val2))
