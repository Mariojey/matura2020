#Zadanie 1.3


def is_k_similar(n, A, B, k):
    for i in range(k):  #Pętla sprawdzająca dane liczby w tablicy (czy są podobne) A[1....k] (od zerowego elementu to elementu nr k)       
        if A[i] != B[i+n-k]:
            return False
    for i in range(n-k):
        if A[k+i] != B[i]:
            return False
    return True

def is_similar(n, A, B):
    for k in range(n):
        if is_k_similar(n, A, B, k):
            return True
    return False

#=================
#ZMIENNE
#=================


tab1_first = [5,7,9]
tab1_second = [5,7,9]
tab2_first = [4,7,1,4,5]
tab2_second = [1,4,5,4,7]
tab3_first = [10,9,12,10,9]
tab3_second = [10,10,9,9,12]
tab4_first = [3,6,5,1,8]
tab4_second = [5,1,8,3,6]
tab5_first = [1,2,3,4,5]
tab5_second = [3,4,5,1,2]
tab6_first = [1,1,1,1,3,1,1,1,1]
tab6_second = [3,1,1,1,1,1,1,1,1]
tab7_first = [4,2,4,4,2,6]
tab7_second = [4,4,2,6,4,2]

tab1_n = 3
tab2_n = 5
tab3_n = 5
tab4_n = 5
tab5_n = 5
tab6_n = 9
tab7_n = 6

tab5_k = 2
tab7_k = 1

#============================================
#ZMIENNE Z WARTOŚCIĄ TEGO CO ZWRÓCIŁA FUNKCJA
#============================================

if_is_similar_tab1 = is_similar(tab1_n, tab1_first, tab1_second)
if_is_similar_tab2 = is_similar(tab2_n, tab2_first, tab2_second)
if_is_similar_tab3 = is_similar(tab3_n, tab3_first, tab3_second)
if_is_similar_tab4 = is_similar(tab4_n, tab4_first, tab4_second)
if_is_similar_tab5 = is_similar(tab5_n, tab5_first, tab5_second)
if_is_similar_tab6 = is_similar(tab6_n, tab6_first, tab6_second)
if_is_similar_tab7 = is_similar(tab7_n, tab7_first, tab7_second)


#===================
#WYPISANIE WYNIKU
#====================
for i in range(1,7):
    print(str(if_is_similar_tab))
