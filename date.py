date = '2022-01-17'

year = int(date[0:4])
month = int(date[5:7])
day = int(date[-2:])

print('Next class is on ', year, month, day + 1)
