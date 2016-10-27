'''
Praca domowa
napisz skrypt ktory wyszukuje liczby pierwsze za pomoca sita erastotenesa
obiektowo
podajac granice gorna
termin: 2 tygodnie
'''

class SitoErastotenesa:
    def __init__(self, n):
        self.n = n
        self.tablica = [0 for i in range(0,n+1)]

    def wyszukaj_pierwsze(self):
        i = 2
        while(i*i<=self.n):
            if self.tablica[i] is 0:
                for j in range(i*i,self.n+1):
                    self.tablica[j]=1
            i+=1

    def wyswietl_pierwsze(self):
        for i in range(2, self.n+1):
            if self.tablica[i] is 0:
                print i

sito = SitoErastotenesa(20)
sito.wyszukaj_pierwsze()
print sito.tablica
sito.wyswietl_pierwsze()
