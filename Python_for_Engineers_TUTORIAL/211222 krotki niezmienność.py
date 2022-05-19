#NIEZMIENNOŚĆ KROTEK
#krotki, w odróżnieniu do list, są niemodyfikowalne (immutable). 

list = ['jeden', 'dwa', 'trzy']
list.append ('cztery')
print(list)

list.insert(4,'pięć')
print(list)

#krotki są niemodyfikowalne (immutable), zatem nie obsługują metod tj. .append lub .
#tup = ('jeden', 'dwa', 'trzy')
#tup.append ('cztery')

#KIEDY STOSOWAĆ KROTKI ?

    #1 krotki są znacznie szybsze podczas obliczeń niż listy. Różnica jest nawet 10-krotna (krótki test znajdziesz tutaj).
    #2 Krotki używamy wtedy, kiedy mamy do czynienia z elementami, które nie powinny być podatne na modyfikacje, jak np. spis dni tygodnia lub daty w kalendarzu. Krotki zapewniają bezpieczeństwo, że żaden z jej elementów jak i ona sama nie zmienią się podczas przeprowadzanych operacji. Listy tego nie zapewniają.
    #3 Zasada generalne jest też taka, że krotki używamy do przechowywania różnych typów danych (heterogeneous datatypes), natomiast listy do podobnych typów danych (homogeneous datatypes).
    #4 Dodatkowo, krotki możemy używać w tzw. słownikach jako ich klucze (o tym będzie w następnej lekcji).

#PRZYKŁAD

belka1 = ('C30/37', 0.3,  0.5)
         #klasa,  , szer, wys)
         
(klasa_bet, b, h) = belka1

#teraz można bezpośrednio odwoływać się do poszczególnych parametrów belki
print (klasa_bet)
print(b)
print(h)