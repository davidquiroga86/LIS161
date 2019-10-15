while True:
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        continue
    break

count = 0

for line in fhand:
    if line.startswith('From'):
        words = line.split()
        print(words[1])
        count += 1

print('There were', count, 'lines with From as the first word')