#obliczanie modułu sprężystości betonu

#Dane
fck = 30                    #Wartość w [MPa]

#Obliczenia wg EC2
fcm = fck +8                #Średnia wytrzymałośc betonu na ściskanie [MPa]

Ecm = 22*(0.1*fcm)**0.3      #Sieczna modułu sprężystości betonu [GPa]

#Wyniki
print(round(Ecm,1))
