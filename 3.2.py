w = 0

n = int(input('Podaj n: '))


cyfry_n = str(n)


suma_cyfr = 0
for c in cyfry_n:
    cyfra = int(c)
    suma_cyfr = suma_cyfr + cyfra


if(n == 1234):
    print('Pytanie 3: ')
    while( n != 0):
        w = w + n % 10
        n = n/10
        print(int(n))
else:
    while(n != 0):
        w = w + n % 10
        n = n/10

print('Pytanie 1 lub 4: ')
print(w)

print(' Pytanie 2: ')
print(int(suma_cyfr))
#Algorytm wypisuje wartości w kolejnoiści odwrotnej