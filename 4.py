file = open("pary.txt", "r")
lines = file.read().splitlines()
file.close()
for i in lines:
    print(i)