# sem repetição, nem função

fatorialManual = (5*4*3*2*1)

print ('\nO fatorial de 5 é:', fatorialManual)


# com comando de repetição while
n = int (input ('\nDigite um número: '));

i = n
f = n
fatorial = 1;

while (i != 0):
    
    fatorial = fatorial * n;
    i = i - 1;
    n = n -1

print ('\nO fatorial de', f, 'é:', fatorial)

# com a função
from math import factorial

print ('\nO fatorial de', f, 'é:', factorial(f))
