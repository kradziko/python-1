'''
1. Napisac skrypt ktory wykona nastepujace czynnosci:
    a) utworzy liste o rozmiarach podanych przez uzytkownika
    b) uzupelni liste losowymi wartosciami z zakresu podanego przez uzytkownika
    c) wyswietli liste
    d) wyszuka wielokrotnosci liczby 2, 3, 5 i zapisze kazda do nowej listy
    e) wyszuka duplikaty z kazdej listy i utworzy z nich nowa liste
    f) zastapi duplikaty znakiem 'X'
    g) usunie duplikaty z listy a)
    h) obliczy wartosc srednia i podniesie kazda wartosc do potegi 3
    i) zastapi weilokrotnosci liczby 2 litera A, 3 litera E, 5 litera L
    j) wyszuka liczy pierwsze i zastapi je litera Z
    k) wyszuka litery w liscie i utworzy z nich losowe napisy
'''
import random


class Wytworniki:
    def __init__(self):
        self.list_obj = None
        self.multiples = None
        pass

    def make_list(self, start, end, step=1):
        return [x for x in range(start, end, step)]

    def random_list(self, start, end, list_obj):
        random.seed()
        for x in range(0, len(list_obj)):
            list_obj[x] = random.randint(start, end)

    def find_multiple(self, list_obj, numbers=(2, 3, 5)):
        return [[y for y in list_obj if not (y % x)] for x in numbers]

    def find_duplicate(self, list_obj):
        return [y for x in list_obj for y in list_obj if y in list_obj[list_obj.index(y) + 1:]]

    def X_letter_duplicates(self, list_obj):
        duplicates = self.find_duplicate(list_obj)
        print duplicates
#        list_obj = ['X' for x in list_obj if x in duplicates]
        for x in list_obj:
            if x in duplicates:
                list_obj[list_obj.index(x)] = 'X'
        return list_obj


w = Wytworniki()
lista = w.make_list(1, 50)
w.random_list(1, 99, lista)
multiple = w.find_multiple(lista)
duplikaty = w.find_duplicate(multiple)
print w.X_letter_duplicates([10, 20, 20, 30, 312])
