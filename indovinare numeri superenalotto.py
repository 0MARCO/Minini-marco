from itertools import *
#combinazioni = list(combinations_with_replacement('123456789',6))
#print (combinazioni)
#comb = combinations([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90],6)
#print(comb)
import math
n = 90    
k = 6

numerocombinazioni = (n + k) - 1  #bisogna fare il coefficiente binomiale 

if k == 1 or k == n:
    print(1)

if k > n:
    print(0)        
else:
    a = math.factorial(n)
    b = math.factorial(l)
    div = a // (b*(x-y))
    print (list(div)) #devo trasformarlo in una lista
div.remove (#tutte le combinazioni uscite)
print(div)

