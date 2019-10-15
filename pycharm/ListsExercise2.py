fhand = open('romeo.txt')
masterlist = list()

for line in fhand:
    line = line.split()
    for word in line:
        if word not in masterlist:
            masterlist.append(word)

masterlist.sort()
print(masterlist)