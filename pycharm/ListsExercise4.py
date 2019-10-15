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

print('Maximum:', max(masterlist))
print('Minimum:', min(masterlist))
