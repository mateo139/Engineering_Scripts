#-*-coding: utf-8-*-

str = 'Phyton dla inżynierów'

print(str.upper())

print(str.lower())

#błąd gdy nie znajdzie
#print(str.index('x'))

#wartośc -1 gdy nie znajdzie
print(str.find('x'))

#cudzysłów - zastosowanie
print(
        'napis 1'
        "napis 2"
     )

#cudzysłów - użycie w wyświetlanym tekście
print(
        "TO jest 'tekst' poprawny"

        'TO też jest "tekst" poprawny'
     )
     
     
     
#tekst wielolniowy """...""" lub '''...'''
print(
'''Ten napis
ma 
wiele
wierszy''')

#tekst wielolniowy z zastosowaniem \n
print("\nSą różne \nmetody \ndo osiągnięcia \ntego samego \ncelu")
print("\nFajne ?\n")


#wyświetlanie kilku napisów naraz
print (1,2,3)
print ('a','b','c')

#samodzielny wybór separatora
print(1, 2, 3, sep='#')
print("ą", "ę", "ć", sep="")

