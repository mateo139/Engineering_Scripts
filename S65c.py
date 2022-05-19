# moduł z definicją funkcji (nie wykonuje tej funkcji)

from math import pi  # https://docs.python.org/3/library/math.html#math.pi


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
    
    if Fd <= Rd:
        print(f"Rd= {Rd:.1f},[kN] Nośność jest wystarczająca\n")
    else:
        print(f"Rd= {Rd:.1f},[kN] Nośność nie jest wystarczająca\n")
##########



    # czy_zwiekszac = True
    # while czy_zwiekszac:
        # if Fd <= Rd:
            #wiadomosc = f"Rd= {Rd:.1f} [kN] Nośność jest wystarczająca\n" #f umożliwienie formatowania zmiennych w środku #{} klamry pozwalają wstawienie zmiennej #https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
            # czy_zwiekszac = False
        # else:
            # wiadomosc = f"Rd={Rd:.1f} [kN] Nośność jest niewystarczająca. Zwiększ szerokość a1 \n"
            # print(wiadomosc)
        
##########
    # u_dop = 0.6 * (t - 2)

    # if u <= u_dop:
        # print(f"u_dop={u_dop:.1f}[mm] Podkładka zapewni przemieszczenie\n")
    # else:
        # print(f"u_dop={u_dop:.1f}[mm] Podkładka niezapewni przemieszczenia\n")

    # alfa_dop = max([(450 * t) / a1 - 10 - 625 / a1, 0])

    # if alfa <= alfa_dop:
        # print(f"alfa_dop={alfa_dop:.1f} [o.oo] Podkładka zapewni obrót\n")
    # else:
        # print(f"alfa_dop={alfa_dop:.1f} [o.oo] Podkładka niezapewni obrotu\n")