import beolvas
szam1 = beolvas.egeszSzamBeolvas()
szam2 = beolvas.egeszSzamBeolvas()
szam3 = beolvas.egeszSzamBeolvas()

szamok = [szam1,szam2,szam3]
kozepso = szamok[1]

print('A középső szám:',kozepso)

szamok.sort()


print("Összehasonlítás:")
if szam1 == szam2 == szam3:
    print("A számok egyenlők")
else:
    if szam1 < szam2:
        print(f"{szam1} kisebb mint {szam2}")
    else:
        print(f"{szam1} nagyobb mint {szam2}")

    if szam2 < szam3:
        print(f"{szam2} kisebb mint {szam3}")
    else:
        print(f"{szam2} nagyobb mint {szam3}")

    if szam1 < szam3:
        print(f"{szam1} kisebb mint {szam3}")
    else:
        print(f"{szam1} nagyobb mint {szam3}")
