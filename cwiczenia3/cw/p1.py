#zbiory zmienne
A = set([1,2,3])
print A
#dodawanie i usuwanie elementow zbioru
A.discard(3) # usuwanie elementu 3
print A

A.add(8) #dodanie elementu 8
print A

#zbiory niezmienne
B=frozenset([3,5,6])
print B

#klucze w slownikach
slownik = {B: 9}
print "slownik: ", slownik

#elementy innych zbiorow
C=set([5, 4, 9])
C.add(B)
print C

#zbior pusty
D =set()
print D

#Operacje na zbiorach

#liczba elementow
print len(A), len(B), len(C), len(D)

#sprawedzenie czy dany obiekt jest elementem zbioru

print 5 in A, 5 in B, 5 in C, 5 in D

#sprawedzenie czy dany obiekt nie jest elementem zbioru
print 8 not in A, 8 not in B, 8 not in C, 8 not in  D

#sprawdzenie czy dany zbior jest podzbiorem innego zbioru
print set([1,2])<=A
print set([3,4])<=B
print set([5])<=B
print set([1,3,5])<=A

print A.issubset(B)
print '\n'

#sprawedzenie czy dany zbior jest nadzbiorem innego zbioru
print A>=set([1,2])
print B>=set([3,4])

print A.issuperset(B)
print '\n'

#laczenie zbiorow
E=A | B
print E
print '\n'


