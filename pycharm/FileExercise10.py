while True:
    fname = input('Enter a file name: ')
    if fname == 'na na boo boo':
        print("NA NA BOO BOO - You have been punk'd!")
        break
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        continue
    break