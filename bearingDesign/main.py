#Now it is a very simple tool for calculation of technical parameters of unreinforced elastomeric bearings.
#In the future this program will be a part of more complex calculation tool (also for reinforced bearing, as well as sliding bearings)

import S65
import S70
import CR2000

#https://pythontutor.com/

while True: #while warunek (jeżeli jest spełniony to wykonuje blok kodu )

    podkładka = input("Wybierz typ podkładki (S65/S70/CR2000) ")
    if podkładka == "S65": #jeżeli "podkładka" jest równa "S65" to...
        S65.funkcja_S65()  #moduł S65.wywołanie funkcj funkcja_S65()
    elif podkładka == "S70":
        S70.funkcja_S70()
    elif podkładka == "CR2000":
        CR2000.funkcja_CR2000()
    else:
        print("Nie znam tego typu podkładki")
