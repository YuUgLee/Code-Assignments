phone_number = int(input())

phone_number3=phone_number%10000
phone_number2=phone_number//10000%1000
phone_number1=phone_number//10000000
print('%d-%d-%d'%(phone_number1,phone_number2,phone_number3))

