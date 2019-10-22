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
        time = words[5]
        colon = time.find(':')
        time = time[0:colon]
        counts[time] = counts.get(time,0) + 1

masterlist = list()

for key, val in counts.items():
    masterlist.append((int(key), val))

masterlist.sort()

for time, count in masterlist:
    time = str(time)
    if len(time) < 2:
        time = '0' + time
    print(time, count)