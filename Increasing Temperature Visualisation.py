user_input = input()
hourly_temperature = user_input.split()
for i in range(len(hourly_temperature)):
    if i==(len(hourly_temperature)-1):
        print(hourly_temperature[i], end=' \n')
    else:
        print(hourly_temperature[i], end=' -> ')
