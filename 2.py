def sym(a,b):
    if a != 0:
        sym(a-1, b+1)
        print( a * b)
        sym(a-1, b+1)

A = [3,4,3,4]
B = [1,2,3,1]

for i in range(4):
    print (sym(A[i], B[i]))
    print('\n')