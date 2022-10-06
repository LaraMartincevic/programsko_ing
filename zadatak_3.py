from fractions import Fraction         #import funkcija koje su potrebne za rad
import statistics
import itertools

segment_1 = [[Fraction(1,2), Fraction(3,2), Fraction(5,2), Fraction(7,2), Fraction(9,2)], [Fraction(8,3), Fraction(10,3), Fraction(13,3)], [Fraction(-2,5),Fraction(3,5)]]  #definiranje prvog segmenta
print("1.SEGMENT: ", segment_1)                    #ispis prvog segmenta

def srednja_vrijednost(segment_1):                 #definiranje funkcije koja vraca srednju vrijednost za segmenat 1
    return statistics.mean(segment_1)

srednja_seg1 = [srednja_vrijednost(x) for x in segment_1]         #pozivanje funkcije
print("SREDNJE VRIJEDNOSTI SEGMENTA 1: ", srednja_seg1)           #ispis rezultata

def srednja_vrijednost(srednja_seg1):                            #ponovno pozivanje funkcije
    return statistics.mean(srednja_seg1)

f_srednja_seg1 = srednja_vrijednost(srednja_seg1)
print("SREDNJA VRIJEDNOST SEGMENTA 1: ", f_srednja_seg1)         #ispis rezultata

grupe_seg1 = len(segment_1)                                      #definiranje kolicina grupe unutar segmenta
print("KVANTITETA GRUPA U SEG1: ", grupe_seg1)                   #ispis rezultata

brojac = 0
for listElem in segment_1:                                       #for petlja unutar koje pomocu brojaca dobivamo broj elemenata unutar segmenta
    brojac += len(listElem)
print('UKUPAN BROJ ELEMENATA U SEG1: ', brojac)                  #ispis rezultata
print("\n")
#
#
#
#
segment_2 = [[Fraction(1), Fraction(2), Fraction(3)], [Fraction(4), Fraction(5), Fraction(6), Fraction(7)], [Fraction(8), Fraction(9)], [Fraction(10), Fraction(11), Fraction(12)]]
print("2.SEGMENT: ", segment_2)

def srednja_vrijednost(segment_2):
    return statistics.mean(segment_2)

srednja_seg2 = [srednja_vrijednost(x) for x in segment_2]
print("SREDNJE VRIJEDNOSTI SEGMENTA 2: ", srednja_seg2)

def srednja_vrijednost(srednja_seg2):
    return statistics.mean(srednja_seg2)

f_srednja_seg2 = srednja_vrijednost(srednja_seg2)
print("SREDNJA VRIJEDNOST SEGMENTA 2: ", f_srednja_seg2)

grupe_seg2 = len(segment_2)
print("KVANTITETA GRUPA U SEG2: ", grupe_seg2)

brojac = 0
for listElem in segment_2:
    brojac += len(listElem)
print('UKUPAN BROJ ELEMENATA U SEG2: ', brojac)
print("\n")
#
#
#
#
segment_3 = [[Fraction(17), Fraction(18)], [Fraction(19), Fraction(20)]]
print("3.SEGMENT: ", segment_3)

def srednja_vrijednost(segment_3):
    return statistics.mean(segment_3)

srednja_seg3 = [srednja_vrijednost(x) for x in segment_3]
print("SREDNJE VRIJEDNOSTI SEGMENTA 3: ", srednja_seg3)

def srednja_vrijednost(srednja_seg3):
    return statistics.mean(srednja_seg3)

f_srednja_seg3 = srednja_vrijednost(srednja_seg3)
print("SREDNJA VRIJEDNOST SEGMENTA 3: ", f_srednja_seg3)

grupe_seg3 = len(segment_3)
print("KVANTITETA GRUPA U SEG3: ", grupe_seg3)

brojac = 0
for listElem in segment_3:
    brojac += len(listElem)
print('UKUPAN BROJ ELEMENATA U SEG3: ', brojac)
print("\n")
#
#
#
#
a = f_srednja_seg1
b = f_srednja_seg3
konacna_srednja_vrijednost = (a+b)/2                      #definiranje kako dobiti konacnu srednju vrijednost

print("KONACNA SREDNJA VRIJEDNOST JE: ", konacna_srednja_vrijednost)        #ispis rezultata
print("\n")
#
#
#
#
sort_1 = sorted(srednja_seg1, reverse = True)                       #sortiranje prve srednje vrijednost
print("SORTIRANE SR_VR PRVOG SEGMENTA: ", sort_1)                   #ispis rezultata

sort_2 = sorted(srednja_seg2, reverse = True)
print("SORTIRANE SR_VR DRUGOG SEGMENTA: ", sort_2)

sort_3 = sorted(srednja_seg3, reverse = True)
print("SORTIRANE SR_VR TRECEG SEGMENTA: ", sort_3)
print("\n")

sort_1.extend(sort_2)                                      #spajanja svih sortova u jedan
sort_1.extend(sort_3)

ultimativni_sort = sorted(sort_1, reverse = True)            #sortiranje segmenata svih skupa
print("SORT SVIH SEGMENATA: ", ultimativni_sort)             #ispis rezultata
print("\n")
#
#
#
#
def oneDArray(x):                               #definicija funkcije koja spaja sve nested liste u normalnu
    return list(itertools.chain(*x))

jednodim_1 = oneDArray(segment_1)               #spajanje svake liste
print("SPOJEN SEGMENT 1: ", jednodim_1)

jednodim_2 = oneDArray(segment_2)
print("SPOJEN SEGMENT 2: ", jednodim_2)

jednodim_3 = oneDArray(segment_3)
print("SPOJEN SEGMENT 3: ", jednodim_3)

jednodim_1.extend(jednodim_2)                   #sve liste u jednu
jednodim_1.extend(jednodim_3)
print("SVI SEGMENTI SPOJENI: ", jednodim_1)

def parcijalna_suma(b):                     #def funkcije za parcijalnu
    total = 0
    for i in b:
        total += i
        yield total

for i in range(0, len(jednodim_1)):            # ovo da se ispisuju kao razlomci
    jednodim_1[i] = Fraction(jednodim_1[i])

suma = list(parcijalna_suma(jednodim_1))
print("PARCIJALNA SUMA SEGMENATA: ", suma)                                #ispis










