"""
pliki
"""

# utworzenie i otwarcie do zapisu pliku "plik1.txt"
f1 = open("plik1.txt", "wb")

# 3 podstawowe atrybuty obiektow plikowych

# name - nazwa plku
print f1.name

# mode - okresla tryb w jakim otwarto plik
print f1.mode

# closed - okresla czy plik jest zamkniety
print f1.closed

# metody do obslugi pliku

# write - zapisuje do pliku napis
f1.write("Pierwszy plik")

# flush - zapisuje dane z bufora do pliku
# (przydatne w przypadku systemu Win...
f1.flush()

# \n - nowa linia w pliku
f1.write("\nNowa linia")

# close - zapisuje dane z bufora do pliku i zamyka plik
f1.close()

# otwarcie pliku do modyfikacji
f1 = open("plik1.txt", "r+b")

# read - odczytuje z pliku napis
print f1.read()

# tell - podaje aktualna pozycje w pliku
print f1.tell()

# seek - ustawia pozycje w pliku na podana
f1.seek(0)

# nadpisanie zawartosci pliku
f1.write("Nowy poczatek")

f1.seek(-13, 1)
try:
    # przesuniecie na wzgledna pozycje pliku (od aktualnej pozycji)
    f1.seek(-14, 1)
except:
    print "seek"

# wczytanie fragmentu zawartosci pliku o okreslonej dlugosci
print f1.read(14)

# wczytanie fragmentu zawartosci pliku o okreslonej dlugosci
print f1.read(14)

# writelines - zapisuje do pliku sekwencje napisow
# (bez dodawania automatycznie separatorow)
f1.writelines(["\n3 linia", "\n4 linia", "\n5 linia"])

# readlines - wczytuje z pliku sekwencje napisow
f1.seek(0)
print f1.readlines()

# truncate - skraca plik na podanej pozycji
f1.truncate(20)
f1.seek(0)
print f1.read()

# isatty - zwraca True jezeli plik jest dolaczony do urzedzenia terminalowego
print f1.isatty()

# przyklad strumienie sys.stdout i sys.stdin

import sys
print sys.stdout.isatty()

# przyklad przekierowania wewnatrz programu
import sys
ekran = sys.stdout
sys.stdout = open("wyjscie.txt", "w")
print "Jestem tutaj"
print "Gdzie Ty poszedles?"
sys.stdout = ekran
print open("wyjscie.txt", "r").read()
