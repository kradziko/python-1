'''
Ksiazka Adresowa
'''

class Kontakt(object):
    id = 0
    def __init__(self, imie=None, nazwisko=None, telefon=None, mail=None, wiek=None, plec=None):
        self.dane = {}
        Kontakt.id += 1
        self.dane['id'] = Kontakt.id
        self.dane['imie'] = imie
        self.dane['nazwisko'] = nazwisko
        self.dane['telefon'] = telefon
        self.dane['mail'] = mail
        self.dane['wiek'] = wiek
        self.dane['plec'] = plec
    def pobierz_z_klawiatury(self):
        self.dane['imie'] = raw_input("Podaj imie: ")
        self.dane['nazwisko'] = raw_input("Podaj nazwisko: ")
        self.dane['telefon'] = raw_input("Podaj telefon: ")
        self.dane['mail'] = raw_input("Podaj adres e-mail: ")
        self.dane['wiek'] = raw_input("Podaj wiek: ")
        self.dane['plec'] = raw_input("Podaj plec: ")

    def wyswietl_kontakt(self):
        print "|%s|%s|%s|%s|%s|%s|%s|" % (str(self.dane['id']).ljust(5),
                                       self.dane['imie'].ljust(20),
                                       self.dane['nazwisko'].ljust(20),
                                       self.dane['telefon'].ljust(20),
                                       self.dane['mail'].ljust(30),
                                       self.dane['wiek'].ljust(5),
                                       self.dane['plec'].ljust(15))
class KsiazkaAdresowa(object):
    def __init__(self):
        self.kontakty = []

    def dodaj(self, k):
        self.kontakty.append(k)

    def usun(self, id):
        doUsuniecia = self.znajdzKontakt(id)
        if doUsuniecia is not None:
            self.kontakty.remove(doUsuniecia)
            return True
        return False

    def znajdzKontakt(self, id):
        for i in self.kontakty:
            if i.dane['id'] == id:
                return i
        return None

    def edytuj(self, id):
        doEdycji = self.znajdzKontakt(id)
        if doEdycji is not None:
            doEdycji.pobierz_z_klawiatury()
            return True
        return False


    def wyswietl(self):
        print '-'*123
        print "|%s|%s|%s|%s|%s|%s|%s|" %("Id".ljust(5),
                                         "Imie".ljust(20),
                                         "Nazwisko".ljust(20),
                                         "Telefon".ljust(20),
                                         "Adres e-mail".ljust(30),
                                         "Wiek".ljust(5),
                                         "Plec".ljust(15))
        print '-'*123
        if len(self.kontakty) == 0:
            print "%s" % "AKTUALNIE BRAK KONTAKTOW NA LISCIE, DODAJ NOWY KONTAKT ABY WYPELNIC TA TABELE".center(130)
            print '-'*123
        else:
            for i in self.kontakty:
                i.wyswietl_kontakt()
                print '-'*123


class KsiazkaAdresowaUI(KsiazkaAdresowa):
    def __init__(self, tytul):
        super(KsiazkaAdresowaUI,self).__init__()
        self.tytul = tytul
        self.petla = True
        while self.petla:
            self.wyswietl()
            self.menu_opcji()


    def start(self):
        print self.tytul.upper().center(64)
        self.wyswietl()

    def dodaj_kontakt(self):
        k = Kontakt()
        k.pobierz_z_klawiatury()
        self.dodaj(k)

    def usun_kontakt(self):
        id = int(raw_input("Podaj id kontaktu ktory chcesz usunac: "))
        wybor = raw_input("Jestes pewien ze chcesz usunac kontakt? t/n: ")

        if wybor == 't':
            usuniecie = self.usun(id)
            if usuniecie is True:
                print "Usunieto kontakt!"
            else:
                print "Nie ma kontaktu o takim id!"


    def edytuj_kontakt(self):
        id = int(raw_input("Podaj id kontaktu ktory chcesz edytowac: "))
        edycja = self.edytuj(id)
        if edycja is True:
            print "Zapisano zmiany!"
        else:
            print "Nie ma kontaktu o takim id!"

    def menu_opcji(self):
        print '''Wybierz czynnosc ktora chcesz wykonac:\n
        1 - Dodaj nowy kontakt\n
        2 - Modyfikuj istniejacy kontakt\n
        3 - Usun kontakt\n
        4 - Wyjdz z programu\n'''
        opcja = int(raw_input("Podaj opcje, ktora chcesz wykonac: "))
        self.wybierz_opcje(opcja)

    def wybierz_opcje(self, opcja):
        if opcja is 1:
            self.dodaj_kontakt()
        elif opcja is 2:
            self.edytuj_kontakt()
        elif opcja is 3:
            self.usun_kontakt()
        elif opcja is 4:
            self.wyjscie()
        else:
            pass

    def wyjscie(self):
        x = raw_input("Na pewno chcesz wyjsc z programu? t/n: ")
        if x == 't':
            self.petla = False
            print "Do widzenia!"

KsiazkaAdresowaUI('program ksiazka adresowa')
