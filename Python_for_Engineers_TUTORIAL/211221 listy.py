# Tworzenie list
pusta_lista=[]
print(pusta_lista)

x=3
moja_lista = [1, 'dwa', 3.45, x]
print(moja_lista)

moja_lista = [1,2,3]
print(moja_lista)

moja_lista = moja_lista + ['dodatkowy element']

print(moja_lista)

#powielanie listy (nie mnożenie)
moja_lista=moja_lista*2
print(moja_lista)

#zastępowanie elementów listy
moja_lista=[1,2,3,4]
print(moja_lista)

moja_lista[0]=0
moja_lista[1]=0
moja_lista[2]=0
moja_lista[3]=0
print(moja_lista)

#Dodawanie elementów do listy
moja_lista=[1,2,3]
print(moja_lista)

#długość listy
print('Długość mojej_listy to ',len(moja_lista))

#dodawanie elementów na KONIEC listy
str= 'dodatkowy_element'
moja_lista.append(str)
print(moja_lista)

#WSTAWIENIE elementu w MIEJSCE INDEKSU, reszta przesuwa się w prawo o 1
moja_lista.insert(0,'pierwszy element')
print(moja_lista)

#USUWANIE elementów listy
nowa_lista = ['a','b','c','d']
print(nowa_lista)

#usunięcie ostatniego elementu z listy, odwrotność funkcji .append
nowa_lista.pop()
print(nowa_lista)

#usunięcie wybranego elementu, wg podanego indexu
nowa_lista.pop(0)
print(nowa_lista)

#usuwanie funkcją .remove
nowa_lista.remove('c')
print(nowa_lista)

#przeszukiwanie list
nowa_lista = ['a','b','c','a']
print(nowa_lista)

# Prawda (True) jeśli element występuje w liście, w przeciwnym przypadku fałsz (False)
print('a' in nowa_lista)

# Zwraca indeks pierwszego wystąpienia szukanego elementu w liście
print(nowa_lista.index('a'))

# Jak wyżej tylko przeszukuje listę w zakresie indeksów od 1 do 10
print(nowa_lista.index('a',1,10))

# Zwraca liczbę wystąpień elementu listy
print(nowa_lista.count('a'))

# Zwraca największy element listy
print(max(nowa_lista))

# Najmniejszy element listy
print(min(nowa_lista))
