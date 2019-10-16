masterlist = list()

while True:
    char = input('Enter a number: ')
    if char == 'done':
        break
    try:
        number = float(char)
    except:
        print('Invalid input')
        continue
    masterlist.append(number)

if len(masterlist) == 0:
    print('Empty, no maximum and minimum.')
else:
    print('Maximum:', max(masterlist))
    print('Minimum:', min(masterlist))
