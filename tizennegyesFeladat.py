import beolvas
szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()
szam3 = beolvas.egeszSzamBeolvas()

szamok = szam1,szam2,szam3

if all(szamok):
    atlag = sum(szamok) / len(szamok)
    print("A számtani közép:",atlag)

else: print("Nincs beolvasott szám")