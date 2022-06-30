import numpy as np

A = np.array([[1, 0, 2, 0], 
                [2, 1, 1, 1], 
                [2, 3, 0, 1], 
                [-1, 1, 2, 2]])

D = np.array([[3, 1, -2, 1], 
                [5, 2, 2, 3], 
                [7, 4, -5, 0], 
                [1, -1, 11, 2]])

#a
soma = np.empty((4, 4))

for l in range(0, 4):
    for c in range(0, 4):
        soma[l][c] = A[l][c] + D[l][c] 
        

print ("\n A soma da matriz A com a D é:\n",soma)

#b 
sub = np.empty((4, 4))

for l in range(0, 4):
    for c in range(0, 4):
        sub[l][c] = A[l][c] - D[l][c] 
        

print ("\n A diferença da matriz A pela matriz D é:\n",sub)

#c 
transpA = np.empty((4, 4))
for l in range(0, 4):
    for c in range(0, 4):
        transpA[c][l] = A[l][c]

print ("\n A matriz transposta de A é:\n",transpA)

#d

transpD = np.empty((4, 4))
for l in range(0, 4):
    for c in range(0, 4):
        transpD[c][l] = D[l][c]

print ("\n A matriz transposta de D é:\n",transpD)

#e 

#f

#g
invA = np.linalg.inv(A)

print("\n A matriz inversa de A é: \n", invA)

#h
invD= np.linalg.inv(D)

print("\n A matriz inversa de D é: \n", invD)

#i


