str = 'X-DSPAM-Confidence:0.8475'

index = str.find(':')

number = float(str[index+1:len(str)])

print(number)