def computepay(hours, rate):
    if hours>40:
        pay = (40*rate) + ((hours-40)*rate*1.5)
    else:
        pay = hours*rate
    return pay

x = float(input("Enter Hours: "))
y = float(input("Enter Rate: "))

print(computepay(x, y))




