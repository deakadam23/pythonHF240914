import math
import beolvas

szam1 = beolvas.egeszSzamBeolvas()
hibauzenet = "A számnak pozitiv egesz szamnak kell lennie"
# ellenorizzuk hogy pozitiv, egesz szam
if szam1 > 0:

    terulet = (math.pi * szam1 ** 2)  / 4
    kerulet = math.pi * szam1
    print("A kör területe: ",terulet)
    print("A kör kerülete: ", kerulet)

else: print(hibauzenet)