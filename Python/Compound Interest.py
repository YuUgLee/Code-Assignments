rate=int(input('Enter in your rate:'))
years=int(input('Enter in the amount of years:'))
mi=int(input('Enter in your monthly investment:'))
periods=years*12
percent=rate/100
mr=rate/(1200)
fv=mi*(((1+mr)**(periods))-1)/(mr)
print('input annual rate without % sign:', rate)
print('Your monthly rate is', mr)
print('input years you plan on saving for:', years)
print('3 years converted to months =', periods)
print('input monthly investment:', mi)
print('The future value of your investment will be', format(fv,'.2f'))
