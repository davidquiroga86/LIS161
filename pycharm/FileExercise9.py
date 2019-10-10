while True:
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        continue
    break

sum = 0
counter = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        sum = sum + float(line[line.find('0'):len(line)])
        counter += 1

average = sum / counter
print('Average spam confidence:', average)