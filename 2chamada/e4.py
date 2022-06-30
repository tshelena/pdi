from binascii import b2a_base64
import numpy as np 
import math
   
img = np.random.randint(1, 10, size=(5, 5)) 
print(img);

ga = np.empty((5, 5))
gb = np.empty((5,5))
gc = np.empty((5,5))

#a g = c * f + b
print ("\nLetra a)")
ga = (2* img) + 5
print ("\n Para c = 2, b = 5, o resultado de g = [(c*f) + b] é: \n", ga)
#-------------------------------------------------------------------------------

ga = (3 * img) + 7
print ("\n Para c = 3, b = 7, o resultado de g = [(c*f) + b] é: \n", ga)

#-------------------------------------------------------------------------------

print ("\nLetra b)")
#b g = c * log 2 (f + 1)
img = img + 1
for l in range(0, 5):
    for c in range(0, 5):
        ga[l][c] = math.log2(img[l][c])
gb = gb * 2
print ("\n Para c = 2, o resultado de g = c*log2(f + 1) é:\n ", gb)

#-------------------------------------------------------------------------------

gb = np.empty((5,5))
for l in range(0, 5):
    for c in range(0, 5):
        gb[l][c] = math.log2(img[l][c])
gb = gb * 3
print ("\n Para c = 3, o resultado de g = c*log2(f + 1) é:\n ", gb)

#-------------------------------------------------------------------------------

#c g = c * exp(f + 1)
print ("\nLetra c)")

for l in range(0, 5):
    for c in range(0, 5):
        gc[l][c] = math.exp(img[l][c])     
gc = 2* gc
print ("\n Para c = 2, o resultado de g = c*exp(f + 1) é: \n ", gc)

#-------------------------------------------------------------------------------

gc = np.empty((5,5))
for l in range(0, 5):
    for c in range(0, 5):
        gc[l][c] = math.exp(img[l][c])      
gc = 3* gc
print ("\n Para c = 3, o resultado de g = c*exp(f + 1) é: \n ", gc)