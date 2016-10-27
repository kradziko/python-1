'''
Zadanie1
Napisz skrypt ktory znajdzie i wypisze na liscie pierwszego wystapienia okreslnoej liczby
'''

x = [1,0,0,0,0,0,0,1,1,0]
def find_position(lista, element):
    return lista.index(element)

print find_position(x, 1)
