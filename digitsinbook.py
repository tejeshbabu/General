def getDigitsInBook(n):
    digits={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in range(1,n+1):
        x = list(str(i))
        for j in x:
            if j=='0':
                digits[j] += 1
            elif j=='1':
                digits[j] += 1
            elif j=='2':
                digits[j] += 1
            elif j=='3':
                digits[j] += 1
            elif j=='4':
                digits[j] += 1
            elif j=='5':
                digits[j] += 1
            elif j=='6':
                digits[j] += 1
            elif j=='7':
                digits[j] += 1
            elif j=='8':
                digits[j] += 1
            elif j=='9':
                digits[j] += 1

    return digits

h = input()
l = getDigitsInBook(h)
for m in range(10):
    print l[str(m)]