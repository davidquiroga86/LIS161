hours = input('Enter Hours: ')
try:
    hours = float(hours)
    rate = input('Enter Rate: ')
    try:
        rate = float(rate)
        pay = hours * rate
        print('Pay: ', pay)
    except:
        print('Error, please enter numeric input')
except:
    print('Error, please enter numeric input')
1