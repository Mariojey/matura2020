def is_similar(n, A, B, k):
    for i in range(k):  #Pętla sprawdzająca dane liczby w tablicy (czy są podobne) A[1....k] (od zerowego elementu to elementu nr k)       
        if A[i] != B[i]:
            return False
    return True

#Przykłady podane w arkuszu
tab1 = [10,9,12,10,9]
tab2 = [10,10,9,9,12]
n_wielkosc = 5
k_podobne = 3
if_is_similar = is_similar(n_wielkosc, tab1, tab2, k_podobne)
print(str(if_is_similar))
        