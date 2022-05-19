# moduł z definicją funkcji (nie wykonuje tej funkcji)

from math import pi  # https://docs.python.org/3/library/math.html#math.pi


def funkcja_CR2000():  #zdefiniowanie funkcji

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

    sigma_rd = min([(S**2+S+1)/0.7 , 20])
    Rd = sigma_rd * (a1 * b1 - n * pi * (d ** 2) / 4) / 1000
    

    if Fd <= Rd:
        print("Rd=",Rd,"[kN] Nośność jest wystarczająca\n")
    else:
        print("Rd=",Rd,"[kN] Nośność jest niewystarczająca\n")

    u_dop = 0.6 * (t - 3)

    if u <= u_dop:
        print("u_dop=",u_dop,"[mm] Podkładka zapewni przemieszczenie\n")
    else:
        print("u_dop=",u_dop,"[mm] Podkładka nie zapewni przemieszczenia\n")

    alfa_dop = min(max([(200*t)/a1, 0]),40)

    if alfa <= alfa_dop:
        print("alfa_dop=",alfa_dop, "[o.oo] Podkładka zapewni obrót\n")
    else:
        print("alfa_dop=",alfa_dop, "[o.oo] Podkładka nie zapewni obrotu\n")