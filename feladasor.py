# 1,a feladat
egeszSzam = 6
# 1,a feladat ellenörzése
print(egeszSzam)
print(type(egeszSzam))
print("Egész szám: "+str(egeszSzam)+".")

# 1,b feladat
tortSzam = 2.5
# ellenörzés
print(tortSzam)
print(type(tortSzam))
print("Tört szám: "+str(tortSzam)+".")

# 1,c feladat
szin = "zöld"  # kedvenc szinem
print(szin)
print(type(szin))
print("A kendvenc szinem a(z)", szin, ".")
print("A kendvenc szinem a(z) "+szin+".")

# 1,d
betu = 'a'
print(betu)
print(type(betu))
print("Az ABC első betűje: "+betu+".")

# 1,e
szunetvanE = True  # igaz érték
print(szunetvanE)
print(type(szunetvanE))

# 1,f
szunetvanE = False  # hamis érték
print(szunetvanE)
print(type(szunetvanE))

# 2 feladat
szam = 4
# fele = int(szam/2) # egész számmá alakítom a szám felét
fele = szam/2
print("A(z) "+str(szam)+" szám fel "+str(int(fele))+".")

# 3 feladat
szam1 = int(input("Adj meg egy egész számot!"))
print(type(szam1))
szam2 = int(input("Adj meg egy másik egész számot!"))
szam3 = int(input("Adj meg egy harmadik egész számot!"))
"""
print("1. szám: "+str(szam1))
print("2. szám: "+str(szam2))
print("3. szám: "+str(szam3))
"""
print("1. szám: "+str(szam1)+"\n2. szám: "+str(szam2)+"\n3. szám: "+str(szam3))

# 4 feladat
# első megoldás
print("1. szám: "+str(szam1)+"2. szám: "+str(szam2)+"3. szám: "+str(szam3))

# második megoldás
print("1. szám: "+str(szam1), end="")
print("2. szám: "+str(szam2), end="")
print("3. szám: "+str(szam3))
