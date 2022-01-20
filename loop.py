# compute the squared sum of the numbers 0,...,99
squared_sum = 0
for number in range(100):
    squared_sum = squared_sum + number**2
    print(number, squared_sum)
print('Result is', squared_sum)