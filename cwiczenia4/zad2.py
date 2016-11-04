'''
napisz skrypt ktory dziala jak gra w zgadywanie liczby
uzytkownik podaje zakres i losuje sie liczba a nastepnie nastepuje zgadywanie liczby
wyswietla sie za malo lub za duzo
ustala sie ilosc prob
'''

import random

random.seed()
class Gra:
    def __init__(self):
        print "Podaj dolny zakres losowania"
        od = int(raw_input())
        print "Podaj gorny zakres losowania"
        do = int(raw_input())
        while od > do:
            print "Podaj gorny zakres losowania"
            do = int(raw_input())
        self.liczba = random.randint(od, do)
        self.proba = 5
        while self.proba:
            print "Podaj liczbe:"
            x = int(raw_input())
            self.sprawdz(x)
        print "koniec gry"

    def sprawdz(self, x):
        if x > self.liczba:
            print "za duza"
            self.proba -= 1
        elif x < self.liczba:
            print "za mala"
            self.proba -= 1
        elif x == self.liczba:
            print "Zgadles!"
            self.proba = 0
Gra()
