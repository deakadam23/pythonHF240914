import beolvas
szam1 = beolvas.egeszSzamBeolvas()
szamjegyosszeg = str(szam1)
osszeg = sum(int(szamjegy) for szamjegy in szamjegyosszeg)
print(osszeg)