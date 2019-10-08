sum = 0
count = 0
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Invalid input')
        continue
    sum = sum + number
    count = count + 1

if count == 0:
    print('No input numbers')
else:
    average = sum / count
    print(sum, count, average)
