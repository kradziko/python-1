"""
pobierz od uzytkownika sciezke
wyswietl:
ilosc plikow
rozmiar plikow
ilosc folderow
rozmiar folderow
rozmiar calosciowy tego folderu
z przeliczeniem na kB i MB
"""

from os import *

user_path = raw_input("Podaj sciezke: ")
# user_path = r'/home/klipski/PycharmProjects/python/'

ilosc_plikow = 0
rozmiar_plikow = 0
ilosc_katalogow = 0
rozmiar_katalogow = 0

for sciezka, podkatalogi, pliki in walk(user_path):
    try:
        for x in pliki:
            print "plik %s o rozmiarze %f b, %f kB, %f MB" % (x, path.getsize(path.join(sciezka,x)),
                                                              path.getsize(path.join(sciezka,x))/1024.,
                                                              path.getsize(path.join(sciezka,x))/1024./1024.)

        for x in podkatalogi:
            print "katalog %s o rozmiarze %f b, %f kB, %f MB" % (x, path.getsize(path.join(sciezka,x)),
                                                              path.getsize(path.join(sciezka,x))/1024.,
                                                              path.getsize(path.join(sciezka,x))/1024./1024.)
        rozmiar_plikow += sum(path.getsize(path.join(sciezka, nazwa)) for nazwa in pliki)
        rozmiar_katalogow += sum(path.getsize(path.join(sciezka, nazwa)) for nazwa in podkatalogi)
        ilosc_plikow += len(pliki)
        ilosc_katalogow += len(podkatalogi)
    except:
        print "nie udalo sie pobrac rozmiaru w: ", sciezka

print "\n"
print "W katalogu %s znajduje sie:" % user_path
print "- %i plikow o rozmiarze %f b, %f kB, %f MB" % (ilosc_plikow, rozmiar_plikow,
                                                      rozmiar_plikow / 1024., rozmiar_plikow / 1024. / 1024.)
print "- %i folderow o rozmiarze %f b, %f kB, %f MB" % (ilosc_katalogow, rozmiar_katalogow,
                                                        rozmiar_katalogow / 1024, rozmiar_katalogow / 1024. / 1024.)
print "Calosciowy rozmiar tego folderu wynosi: %f b, %f kB, %f MB" % (rozmiar_katalogow + rozmiar_plikow,
                                                                      (rozmiar_katalogow + rozmiar_plikow) / 1024.,
                                                                      (
                                                                      rozmiar_katalogow + rozmiar_plikow) / 1024. / 1024.)
