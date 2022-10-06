import math
import numpy as np
from fractions import Fraction
from array import *
import statistics

'''
n = int(input())
m = int(input())

ar = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        k = int(input())
        ar[i][j] = k

for i in range(m):
    for j in range(n):
        print(ar[i][j])
'''

'''
  n, m = map(int, input("Enter row and column : ").split())
  matrix = []
  for i in range(0, n):
      matrix.append(list(map(int, input().strip().split()))[:m])
'''
'''
segment_1 = [[Fraction(1/2), Fraction(3/2), Fraction(5/2), Fraction(7/2), Fraction(9/2)], [Fraction(8,3), Fraction(10,3), Fraction(13,3)], [Fraction(-2,5),Fraction(3,5)]]
print(segment_1)
'''

#segment_1 = [[1/2, 3/2, 5/2, 7/2, 9/2], [8/3, 10/3,13/3], [-2/5,3/5]]
#print(segment_1)

'''
segment_2 = [[Fraction(1), Fraction(2), Fraction(3)], [Fraction(4), Fraction(5), Fraction(6), Fraction(7)], [Fraction(8), Fraction(9)], [Fraction(10), Fraction(11), Fraction(12)]]
print(segment_2)
'''
segment_3 = [[Fraction(17), Fraction(18)], [Fraction(19), Fraction(20)]]
print(segment_3)

'''
segment_1 = np.array(
    [[1/2, 3/2, 5/2, 7/2, 9/2], [8/3, 10/3,13/3], [-2/5,3/5]],
    dtype = object,
)

np.mean(segment_1, 0)
'''

#new_l = list(map(Fraction(segment_1)))

def srednja_vrijednost(segment_3):
    #a = [0][0]
    #b = [-1][-1]
    return statistics.mean(segment_3)

print([srednja_vrijednost(x) for x in segment_3])
#print(list(map(srednja_vrijednost, segment_3)))

#print (srednja_vrijednost(item) for item in segment_3)







'''
a = [0][0]
b = [-1][-1]

srednja_vrijednost = (a+b)/2


for sublist in segment_1:
    print(srednja_vrijednost)
'''



'''
a = [Fraction(3/8), Fraction(12,7)]
print(a)

b = [Fraction(3,5), Fraction(3/5)]
print(b)
'''






'''
broj_segmenata = int(input("Unesite koliko segmenata želite imati : "))
for i in range (0, broj_segmenata):
    segment = []

    broj_grupa = int(input("Enter number of elements : "))

    for i in range(0, broj_grupa):
        element = [Fraction(input()), Fraction(input()), Fraction(input())]
        segment.append(element)

    print(segment)

a = element[0]
b = element[-1]
srednja_vrijednost = (a+b)/2
print(srednja_vrijednost)

'''

'''
rows = int(input())
cols = int(input())

matrix = []
for i in range(rows):
  row = []
  for j in range(cols):
    row.append(0)
  matrix.append(row)

print(matrix)
'''

#srednja_seg1, srednja_seg2, srednja_seg3 = map(list, zip(*sorted(zip(srednja_seg1, srednja_seg2, srednja_seg3), reverse=True)))
#print(srednja_seg1, srednja_seg2, srednja_seg3)
'''
sort_srednja_seg1 = srednja_seg1.sort()
print(sort_srednja_seg1)

sort_srednja_seg2 = srednja_seg2.sort()
print(sort_srednja_seg2)

sort_srednja_seg3 = srednja_seg3.sort()
print(sort_srednja_seg3)
'''

#output_1 = cumsum.segment_1
#print(output_1)
'''
zippana = zip(segment_1, segment_2, segment_3)
print(sum(x) for x in zippana)

for x in zippana:
    print(x)
'''
'''
def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i
        yield total

sums = list(partial_sums(segment_1))
'''



#parcijala = segment_1
#parcijala_1 = list(itertools.accumulate(parcijala))
#print(parcijala_1)

#segment_1.extend(segment_2)                                 #spajanje svih segmenata u jedan
#segment_1.extend(segment_3)
'''
partial_sum = lambda a, b: a + [a[-1] + b]                 #racunanje parcijalne sume
sums =  (partial_sum, segment_1[1:], segment_1[0:1])        
print("PARCIJALNA SUMA: ", sums)                            #ispis rezultata
'''

#for x in segment_1:
#    new_seg =list(itertools.accumulate(segment_1))
#print(new_seg)
'''
def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i
        yield total

#sega_1 = [[Fraction(1,2), Fraction(3,2), Fraction(5,2), Fraction(7,2), Fraction(9,2)], [Fraction(8,3), Fraction(10,3), Fraction(13,3)], [Fraction(-2,5),Fraction(3,5)]]
sums = list(partial_sums(int(segment_1)))
print(sums)
'''














