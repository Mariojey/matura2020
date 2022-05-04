import math

def isPrime(value):
    sqrtValue = int(math.sqrt(value))
    for i in range(2, sqrtValue+1):
        if value % i == 0:
            return False
        return True

def isGoldbach(a):
    if a % 2 != 0:
        return
    val1 = 0
    val2 = 0
    for i in range(3, a+1):
        subtr = a-i
        #walidacja liczb
        if subtr % 2 == 0 or i % 2 == 0:
            continue
        if not isPrime(subtr) or not isPrime(i):
            continue
        if val2 - val1 <= subtr - i:
            val2 = subtr
            val1 = i
    fileW.write(str(a) + " " + str(val1) + " " + str(val2) + "\n")
    #print(str(a) + " " + str(val1) + " " + str(val2))

#Pobieranie danych z pliku
file = open("pary.txt", "r")
fileW = open("wyniki4.txt","w")
text_lines = file.read().splitlines()
file.close()

for l in text_lines:
    numLines = int(l.split(" ")[0])
    isGoldbach(numLines)

fileW.close()