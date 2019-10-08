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
    if count == 0:
        max = number
        min = number
    sum = sum + number
    count = count + 1
    if number > max:
        max = number
    if number < min:
        min = number

if count == 0:
    print(sum, count, "There is no maximum and minimum.")
else:
    print(sum, count, max,min)


