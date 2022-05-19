#Słowniki

moj_slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}
print(moj_slownik)

moj_slownik = {}
print(moj_slownik)

moj_slownik ['klucz1'] = 'wartosc1'
moj_slownik ['klucz2'] = 'wartosc2'
print(moj_slownik)

          #klucze musza mieć ten sam typ (np. string, float)
          #wartości mogą mieć różne typy
dict1 = {'key1': 'napis1',
         'key2': 123,
         'key3': ['i1', 'i2', 'i3']}
print(dict1)

#wartości słownika wywołujemy przez odwołanie się do jego klucza
d1 = dict1['key2']
print (d1)

#odwołanie się do elementu zagnieżdżonego
d2 = dict1['key3'][2]
print (d2)

#dodanie nowego klucza i odpowiadającej mu wartości
dict1['key3'] = 'nowa wartość'
print(dict1)

#modyfukujemy wartość wybranego klucza
dict1['key3'] = 'PODMIANKA'
print(dict1)

#DZIAŁANIA NA SŁOWNIKACH
#Wartości w słowniku można modyfikować poprzez:
#dodawanie +, odejmowanie -, mnożenie/powielanie *, dzielenie /. 
# Zasada jest taka sama jak np. działania na liczbach lub napisach.

dict1['key2'] = dict1['key2'] - 100
d3 = dict1['key2']
print (d3)
print(dict1)

#przykłady modyfikacj
dict1['key1'] = dict1['key1'] + ' nowy'
print(dict1['key1'])

dict1['key3'] = dict['key3'* 2] 
print(dict1['key3'])

#usuwanie elemenu słownika
print(dict1)

del dict1['key3']
print (dict1)

dict1.pop('key1')
print(dict1)

#czyszczenie całego słownika przy użyciu METODY clear()
dict1.clear()
print(dict1)