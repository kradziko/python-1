'''
kolo fortuny
'''
import random

random.seed()  # ziarno

class Haslo(object):
    def __init__(self, tekst):
        self.tekst =  tekst
        self.doZgadniecia = self.wygwiazdkuj_haslo(tekst)

    def wygwiazdkuj_haslo(self, haslo):
        napis = ""
        for t in haslo:
            if t != " ":
                napis += '*'
            else:
                napis += " "
        return napis

    def sprawdz_litere(self, litera):
        if litera in self.tekst:
            indeks = self.tekst.index(litera)
#            self.doZgadniecia.replace() self.tekst[indeks] #*******************




class Zgadywanie(object):
    def __init__(self, nazwaPliku):
        self.plik = open(nazwaPliku, "r+w")
        self.kategorie = [line.split()[0] for line in self.plik.readlines()]
        self.plik.seek(0)
        self.hasla = [line.split()[1:] for line in self.plik.readlines()]
        self.plik.close()

    def losuj_kategorie(self):
        return self.kategorie[random.randint(0, len(self.kategorie) - 1)]

    def losuj_haslo(self, kategoria):
        kat_index = self.kategorie.index(kategoria)
        return self.hasla[kat_index][random.randint(0, len(self.hasla[kat_index]) - 1)]


class Gracz(object):
    def __init__(self, numerGracza):
        self.numerGracza = numerGracza
        self.punkty = 0
        self.wylosowanaLiczba = 0
        self.jestBankrutem = False

    def krec_kolem(self):
        self.wylosowanaLiczba = random.randint(-10, 10)
        if self.wylosowanaLiczba == 0:
            self.jestBankrutem = True
        else:
            self.jestBankrutem = False

    def przedstaw_sie(self):
        return "Gracz nr %d" % self.numerGracza

    def zgaduj(self, haslo):
        pass


class KoloFortuny(object):
    def __init__(self):
        self.liczbaGraczy = None
        self.uczestnicy = []
        self.liczbaTur = None
        self.graj()

    def jednaTura(self):
        for uczestnik in self.uczestnicy:
            print uczestnik.przedstaw_sie()
            uczestnik.krec_kolem()
            print "Wylosowalem liczbe: %d" % uczestnik.wylosowanaLiczba
            if uczestnik.jestBankrutem is False:
                z = Zgadywanie("hasla")
                kategoria = z.losuj_kategorie()
                print "Kategoria %s" % kategoria
                haslo = z.losuj_haslo(kategoria)
                uczestnik.zgaduj(haslo)


            else:
                print "Jestem bankrutem..."

    def pobierz_liczbe_graczy(self):
        self.liczbaGraczy = int(raw_input("Podaj liczbe graczy: "))
        self.liczbaTur = self.liczbaGraczy

    def mieszaj_kolejnosc_graczy(self):
        self.uczestnicy = [Gracz(x) for x in range(1, self.liczbaGraczy + 1)]
        random.shuffle(self.uczestnicy)

    def graj(self):
        self.pobierz_liczbe_graczy()
        self.mieszaj_kolejnosc_graczy()
        for tura in range(0, self.liczbaTur):
            self.jednaTura()

haslo = Haslo("krowa mleko")
print haslo.doZgadniecia
haslo.sprawdz_litere('k')
print haslo.doZgadniecia


#KoloFortuny()
