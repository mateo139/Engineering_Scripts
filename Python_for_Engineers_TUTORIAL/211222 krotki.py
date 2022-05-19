#Tuples... czyli krotki
#uwaga, krotki to nie listy...
#krotki używają nawiasów okrągłych () 
#listy używają nawiasów kwadratowych []

#Tworzymy pierwszą krotkę (tupl)
tup = ('jeden', 'dwa', 'trzy')

#krotki możemy tworzyć również BEZ NAWIASÓW
tup2 = 'cztery', 'pięć' , 'sześć '

# krotku (jak również listy) mogą zawierać elementy różnego typu np.
tup_mix = (1, "dwa", [3,4.1])
print(tup_mix)

#PODSTAWOWE OPERACJE NA KROTKACH
#odwołania do indeksu
print(tup[0])  #odwołanie do 1szego elementu krotki
print(tup[-1]) #odwołanie do ostatniego elementu krotki
print(tup[1:]) #odwołanie od 2giego do ostatniego elementu krotki

#różnice między krotkami a listami (krotki są niemodyfikowalne !!!)
#tup[1]='zmieniamy drugi element krotki'


