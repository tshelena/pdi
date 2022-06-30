import numpy as np 
   
array = np.random.randint(-10, 10, size=(5, 5)) 
print(array);

#a
negativos = 0

for l in range(0, 4):
    for c in range(0, 4):
        if array[l][c] < 0:
            negativos = negativos +1
            

print (negativos)

#b
for l in range(0, 5):
    for c in range(0, 5):
        if array[l][c] < 0:
            array[l][c] = 0
            
print (array)

#c

positivos = 0
media = 0
soma = 0

for l in range(0, 5):
    for c in range(0, 5):
        if array[l][c] > 0:
            positivos = positivos +1
            soma = soma + array [l][c]
            
media = soma/positivos
print ("\na média dos valores positivos é:", media)
