#są trzy listy
lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = [7,8,9]

#połączmy je w jedną macierz
tablica = [lista_1,lista_2,lista_3]

#sprawdźmy jak wygląda CAŁA nasza macierz
print(tablica)

#sprawdźmy jak wygląda pierwszy wiersz
print(tablica[0])

#uwaga - wywołanie 1szego elementu z 1szego wiersza...
print(tablica[0][0])

#uwaga - wywołanie 2go elementu z 2go wiersza...
print(tablica[1][1])

#uwaga - wywołanie 3szego elementu z 3szego wiersza...
print(tablica[2][2])

sum(tablica)

## Należy tylko pamiętać, że pierwszy indeks dotyczy numeru wiersza macierzy (czyli w poziomie), a drugi numeru elementu w tym wierszu
