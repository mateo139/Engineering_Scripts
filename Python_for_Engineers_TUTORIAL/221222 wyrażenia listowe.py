lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = [7,8,9]

tablica = [lista_1, lista_2, lista_3]

print(tablica)

#Przykład: Weźmy zdefiniowaną wyżej tablica i za pomocą wyrażenia listowego
#stworzę listę, która będzie zawierać pierwszą kolumnę tej macierzy
#(mówiąc ściśle: pierwszy element każdego wiersza).

kolumna_1 = [wiersz[0] for wiersz in tablica]
print(kolumna_1)

