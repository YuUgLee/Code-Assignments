"""
Name: Newton Bao
I.D. #:018286708
"""
i=2
while i < 4:
    option=(input('Would you like to convert into Fahrenheit or Celsius?: '))
    option.capitalize()
    if option.capitalize() == 'Fahrenheit':
        degreeone=(input('Please enter a degree in Celsius: '))
        F=((float(degreeone))*(9/5))+32
        print('It is' + ' ' +str(F) + ' ' + 'degrees in Fahrenheit.\n\nThank you!')
        i=6

    else:
        if option.capitalize() == 'Celsius':
            degreetwo=(input('Please enter a degree in Fahrenheit: '))
            C=(((float(degreetwo))-32)*5/9)
            print('It is' + ' ' + str(C) +  ' ' + 'degrees in Celsius.\n\nThank you!')
            i=6
        else:
            print('Please try again.')
            i=2
            
''' https://stackoverflow.com/questions/492860/python-restarting-a-loop'''
