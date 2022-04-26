def sym(a,b):
    if a != 0:
        sym(a-1, b+1)
        print( a * b)
        sym(a-1, b+1)

A = [3,4,5,6,10]
B = [2,4,1,6,2020]

for i in range (5):
    print(2 ** A[i] - 1)