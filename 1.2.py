#Zadanie 1.2

def is_similar(n, A, B, k):
    for i in range(k):  #Pętla sprawdzająca dane liczby w tablicy (czy są podobne) A[1....k] (od zerowego elementu to elementu nr k)       
        if A[i] != B[i+n-k]:
            return False
    for i in range(n-k):
        if A[k+i] != B[i]:
            return False
    return True


#Przykłady podane w arkuszu

A = [
    [5,7,9],
    [4,7,1,4,5],
    [10,9,12,10,9],
    [3,6,5,1,8],
    [1,2,3,4,5],
    [1,1,1,1,3,1,1,1,1],
    [4,2,4,4,2,6]
]

B = [
    [5,7,9],
    [1,4,5,4,7],
    [10,10,9,9,12],
    [5,1,8,3,6],
    [3,4,5,1,2],
    [3,1,1,1,1,1,1,1,1],
    [4,4,2,6,4,2]
]


N = [3,5,5,5,5,9,6]
K = [0,2,3,4,2,4,1]

for i in range(7):
    print(is_similar(N[i], A[i], B[i], K[i]))