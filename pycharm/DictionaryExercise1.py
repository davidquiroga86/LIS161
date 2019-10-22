while True:
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        continue
    break

counts = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        try:
            day = words[2]
        except:
            continue
        counts[day] = counts.get(day,0) + 1

print(counts)