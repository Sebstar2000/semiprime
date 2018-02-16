minVal = int(input("Minimum Value:"))
maxVal = int(input("Maximum Value:"))
               
primeNumbers = []
semiprime = []

def checkNumber(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
    if isPrime == True:
        global primeNumbers
        primeNumbers.append(str(num))

def timesNumbers():
    for i in primeNumbers:
        for x in primeNumbers:
            outNum = int(i)*int(x)
            # print("For1:",i,"For2",x,"OutNum:",outNum)
            if outNum <= maxVal and outNum >= minVal:
                semiprime.append(outNum)
                
def removeDup(inputArray):
    outputArray = []
    for element in inputArray:
        if element not in outputArray:
            outputArray.append(element)
    return outputArray
        
for i in range(1,maxVal):
    checkNumber(i)

# print(primeNumbers)
primeNumbers.pop(0)
timesNumbers()
output = removeDup(semiprime)
print(sorted(output))