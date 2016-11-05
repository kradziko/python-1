'''
SITO ERASTOTENESA
'''

class SitoErastotenesa:
    '''
    Sito Erastotenesa
    sluzy do wyszukiwania wszystkich liczb
    pierwszych z zakresu [2 ... n]
    '''

    def __init__(self, n):
        self.n = n                                      #zakres wyszukiwania liczb pierwszych
        self.tablica = [0 for i in range(0, n + 1)]     #lista wypelniona zerami
        self.przesiej()

    def przesiej(self):
        '''
        Metoda wyszukujaca liczby pierwsze
        Umowa:
        1 - indeks jest liczba pierwsza,
        0 - indeks nie jest liczba pierwsza
        '''
        for i in range(2, self.n):
            if self.tablica[i] is 0:
                for j in range(i * i, self.n + 1, i):
                    self.tablica[j] = 1

    def wyswietl(self):
        '''Wyswietla liczby pierwsze'''
        for i in range(2, self.n + 1):
            if self.tablica[i] is 0:
                print i,

sito = SitoErastotenesa(50)
sito.wyswietl()
