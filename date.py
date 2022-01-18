date = '2022-01-18'

def compute_tomorrow(date):
    year = date[0:4]
    month = date[5:7]
    day = int(date[-2:])
    return year + '-' + month + '-' + str(day + 1)

print('Next class is on ', compute_tomorrow(date))

def convert_to_meters(number):
    return number * 0.3048

print('200 feet in meters =', convert_to_meters(200.0))