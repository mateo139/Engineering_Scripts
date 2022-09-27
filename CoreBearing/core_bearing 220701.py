import math

print ("\nCOMPACT CORE BEARING CALCULATION TOOL:")
print ("\nCOMMENT:")
print ("This tool is designed for dimensioning of Calenberg Compact Core bearing ")
print ("in application to butt joint connection in steel structures.\n")

print ("ASSUMPTIONS FOR CALCULATIONS:")
print ("- Bearing is rectangular with dimensions of he x be")
print ("- In bearing are 4 holes with diameter of D, 2 per row.")
print ("- Please input characteristic loads.\n")

while True: #while warunek (jeżeli jest spełniony to wykonuje blok kodu )

    #DATA INPUT
    he  = float(input("Please input bearing height he [mm]: "))
    be  = float(input("Please input bearing length be [mm]: "))
    te  = float(input("Please input bearings thickness te [mm]: "))
    e   = float(input("Please input axial distance between rows of nuts e [mm]: "))
    d   = float(input("Please input hole diameter D [mm]: "))
    Mc  = float(input("Please input characteristic value of bending moment Mc [kNm]: "))
    Nc  = float(input("Please input characteristic value of normal force Nc [kN]: "))
    Fsc = float(input("Please input characteristic value of prestressing force (per 1 nut) Fsc [kN]: "))

    #COMPUTING OF "ZERO LINE" POSITION
    zo = ((4*Fsc - Nc)/(12*Mc))*(he*he)/1000
    zo = round(zo,1)
    print ("Zero line zo, is in position of ",zo,"mm")
    print ("he/2= ",he/2,"mm")
    print ("-he/2= ",-he/2,"mm")

    #CHECKING OF CASE 
    if zo > he/2 or zo <-he/2:                                                               #Only compression case.
        print("Only compression case.")                                 
        hm = he + (2*Mc*1000)/(Nc-4*Fsc)                                                     #zweryfikować
        hm = round (hm,1)
        print ("hm = ", hm, " mm")

        sigma_m = (Nc*1000-4*Fsc*1000)**2/(be*(he*(Nc*1000-4*Fsc*1000)+2*Mc*1000*1000))      #zweryfikować
        sigma_m = round(sigma_m,1)
        print("sigma_m = ", sigma_m, " MPa")
        if sigma_m < 0:
            print("Negative sign (-) means compression")
        else:
            print("Positive sign (+) means tension")

    else:
        print("Compression & tension case.")                                                 #Compression & tension case.
        F = ((Nc-4*Fsc)/2+(3*Mc*1000/he)) * (0.5 - zo/he)
        F = round (F,1)
        print("F = ", F, " kN")

        hm = he + (2*Mc*1000-F*e)/(Nc-4*Fsc-F)
        hm = round (hm,1)
        print ("hm = ", hm, " mm")

        sigma_m = (Nc*1000-4*Fsc*1000-F*1000)**2 /(be*(he*(Nc*1000-4*Fsc*1000-F*1000)+2*Mc*1000*1000-F*1000*e))
        sigma_m = round (sigma_m,1)
        print("sigma_m = ", sigma_m, " MPa")
        if sigma_m < 0:
            print("Negative sign (-) means compression")
        else:
            print("Positive sign (+) means tension")


