
favorite_color = input('Enter favorite color:\n')
pet=input("Enter pet's name:\n")
num=input('Enter a number:\n')
print('You entered:',favorite_color, pet, num)

password1 = favorite_color+'_'+pet
password2 = str(num)+favorite_color+str(num)
print('\nFirst password: %s_%s' %(favorite_color, pet))
print('Second password: %s' %(password2))



length1=len(password1)
length2=len(password2)
print('\nNumber of characters in %s: %d' %(password1,length1))
print('Number of characters in %s: %d' %(password2,length2))
