#moduł wylicza parametry podkładek, w przypadku nie spełnienia warunku nośności, uruchamia się ponowie 

from math import pi

def funkcja_S65():  #zdefiniowanie funkcji

    a1 = int(input("Podaj a1 [mm]: "))
    b1 = int(input("Podaj b1 [mm]: "))
    t = int(input("Podaj t [mm]: "))
        
    if min(a1,b1) < t*5:
        print("Należy zachować proporcję min(a1,b1) >= tx5")
        print("Podaj parametry a1, b1, t ponownie")
        a1 = int(input("Podaj a1 [mm]: "))
        b1 = int(input("Podaj b1 [mm]: "))
        t = int(input("Podaj t [mm]: "))

    else:
        print("Parametry podano poprawinie")
            
        n = int(input("Podaj liczbę otworów: "))  # liczba otworów
        d = int(input("Podaj średnice otworu [mm]: "))  # średnica otworu
        Fd = int(input("Podaj siłę działającą na podkładkę [kN]: "))
        u = int(input("Podaj przemieszczenia [mm]: "))
        alfa = int(input("Podaj kąt obrotu [o/oo]: "))

        S = (a1 * b1 - n * pi * (d ** 2) / 4) / (t * (a1 * 2 + b1 * 2 + 2 * pi * d))

        sigma_rd = min([4.05 * S**1.16 , 14])
        Rd = sigma_rd * (a1 * b1 - n * pi * (d ** 2) / 4) / 1000
        
        print("\nWYNIKI:\n")


    ### chcę ościągnąć zwiększanie parametru a1 do zwiększenia Rd
    if Fd > Rd:
        wiadomosc = f"Rd= {Rd:.1f} [kN] Nośność nie jest wystarczająca. Zwiększ szerokość a1\n" #f umożliwienie formatowania zmiennych w środku #{} klamry pozwalają wstawienie zmiennej #https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
        print(wiadomosc)
    else:
        iteracja = False
        wiadomosc = f"Rd={Rd:.1f} [kN] Nośność jest wystarczająca. \n"
        print(wiadomosc)

iteracja = True

while iteracja:
    funkcja_S65()
wiadomosc = f"Rd={Rd:.1f} [kN] Nośność jest wystarczająca. \n"
print(wiadomosc)