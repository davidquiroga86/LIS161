while True:
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        continue
    break

for line in fhand:
    line = line.rstrip()
    print(line.upper())
