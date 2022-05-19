#METODY WBUDOWANE SŁOWNIKÓW
#ustalanie ile par klucz-wartość ma słownik używamy
# FUNKCJI len()
# METODY .items()
# METODY .keys()
# METODY .values()

dict1 = {'k1':'w1',
         'k2':'w2'}
         
print('sprawdzenie liczby kluczy FUNKCJĄ len()')
d1 = len(dict1)
print(d1, '\n') #'\n' przejście do nowego wiersza

print('zwracanie listy elementów słownika METODĄ .items()')
d2 = dict1.items()
print(d2, '\n') #'\n' przejście do nowego wiersza

print('wyświetlanie wszystkich kluczy METODĄ .keys()')
d3 = dict1.keys()
print(d3, '\n') #'\n' przejście do nowego wiersza

print('wyświetlanie wszystkich wartości METODĄ .values')
d4 = dict1.values()
print(d4, '\n')

#AKTUALIZOWANIE SŁOWNIKA W OPACIU O INNY SŁOWNIK
dict2 = {'k10': 10}
print(dict2)

print(dict1)
dict1.update(dict2)
print(dict1)

#DOSTĘPNE OPARACJE DLA SŁOWNIKÓW - FUNKCJA dir()
#print(dir(dict1))

#ZAGNIEŻDŻANIE SŁOWNIKÓW
slownik_zagniezdzony = {'klucz1':{'pod_klucz':{'pod_pod_klucz':'wartosc1'}}}
print(slownik_zagniezdzony)

#wywołanie wartości słownika zagnieżdzonego
d5= slownik_zagniezdzony['klucz1']['pod_klucz']['pod_pod_klucz']
print (d5)


