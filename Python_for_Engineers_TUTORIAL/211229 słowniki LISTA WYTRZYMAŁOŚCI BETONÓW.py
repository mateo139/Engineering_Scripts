#PRZYKŁAD - LISTA WYTRZYMAŁOŚCI BETONÓW
#klasy betonu wg EC2
concrete_fck = {'C20/25':20,
                'C25/30':25,
                'C30/37':30,
                'C35/45':35,
                'C40/50':40,
                'C45/55':45,
                'C50/60':50,
                'C55/67':55,
                'C60/75':60,
                'C70/85':70,
                'C80/95':80,
                'C90/105':90}
print(concrete_fck)

klasa = input('Podaj klasę betonu\n')

print('fck=', concrete_fck[klasa], 'MPa')

 