import string


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
    words = line.split()
    for word in words:
        for char in word:
            char = char.lower()
            if char.isalpha():
                counts[char] = counts.get(char, 0) + 1

masterlist = list()

for key, val in counts.items():
    masterlist.append((val, key))

masterlist.sort(reverse=True)

print(masterlist)