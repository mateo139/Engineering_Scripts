#łączenie i powielanie krotek
tup1 = (1,2,3)
tup2 = ('a', 'b', 'c')
tup3 = tup1 + tup2
print(tup3)

tup4 = tup2 + tup1
print(tup4)

tup = ('jeden', 'dwa', 'trzy')
print(len(tup))

print(tup.index('dwa'))

print(tup.count('jeden'))

print('trzy' in tup)

tup_numbers = (1,2,3)
print(sum(tup_numbers))

krotka1 = (1,2,3) #tworzymy 3 osobne krotki
krotka2 = (4,5,6)
krotka3 = (7,8,9)

krotka_duża = (krotka1, krotka2, krotka3) #łączymy krotki w jedną zbiorczą
print(krotka_duża)

s = krotka1 + krotka2 + krotka3 #dopiero taką dużą krotkę można zsumować
print(s)
print(sum(s))


