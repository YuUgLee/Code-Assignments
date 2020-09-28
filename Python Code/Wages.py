hours=float(input('How many hours did you work this week? '))
rate=float(input('How much are you paid per hour? $'))
if hours <= 40:
    earned=hours*rate
    print('You earned $','%0.2f' %(earned))
elif (hours > 40) and (hours < 60):
    overhour=hours-40
    earned=rate*40+((rate*1.5)*overhour)
    print('You earned $'+'%0.2f' %(earned))
elif hours > 60:
    overhour=hours-60
    earned=(rate*40)+(((1.5*rate)*20) +(2*rate) * overhour)
    print('You earned $','%0.2f' %(earned))


