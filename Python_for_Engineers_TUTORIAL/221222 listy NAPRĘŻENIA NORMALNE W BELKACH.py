#W przykładzie chodzi o to, że mamy 3 belki o zróżnicowanych przekrojach
#i siłach osiowych i należy obliczyć pole przekroju i naprężenie normalne dla każdej z tych belek.

#Dane przekroju [h, b]
belka1 = [0.2, 0.5]
belka2 = [0.3, 0.6]
belka3 = [0.4, 0.4]

#Siły podłużne w kolejnych belkach
F = [200, 300, 400]

#Obliczenia
belki = [belka1, belka2, belka3]    #zbiór belek jako macierz
pole = []                           #lista pól przekroju belek (jeszcze pusta)
sigma = []                          # lista naprężeń normalnych belek (jeszcze pusta)

print('ilość elementów w liście "belki", wynosi:',len(belki))

for i in range(len(belki)):
      pole.append(belki[i][0] * belki [i][1])
      sigma.append(F[i] / pole[i] / 1000)
      
print ('Naprężenia normalne w belkach:')
print(" - Pole przekroju belki 'i':             ", pole, 'm2')
print(" - Naprężenie normalne w belce 'i':      ", sigma, 'MPa') 
