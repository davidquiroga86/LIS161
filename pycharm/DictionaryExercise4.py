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
        sender = words[1]
        at = sender.find('@')
        sender = sender[at+1:len(sender)]
        counts[sender] = counts.get(sender,0) + 1

print(counts)