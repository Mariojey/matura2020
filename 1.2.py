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

#ZMIENNE
tab5_first = [1,2,3,4,5]
tab5_second = [3,4,5,1,2]
tab7_first = [4,2,4,4,2,6]
tab7_second = [4,4,2,6,4,2]
tab5_n = 5
tab5_k = 2
tab7_n = 6
tab7_k = 1


#WYWOŁANIE FUNKCJI
if_is_similar_tab5 = is_similar(tab5_n, tab5_first, tab5_second, tab5_k)
if_is_similar_tab7 = is_similar(tab7_n, tab7_first, tab7_second, tab7_k)
print(str(if_is_similar_tab5))
print(str(if_is_similar_tab7))
        