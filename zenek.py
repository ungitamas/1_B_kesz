# 1/B/1. Írjon egy Python programot, amely bekér három számot a felhasználótól. Első lépésként írja a képernyőre, hogy mind a három páros szám-e. Második lépésként, abban az esetben, ha három különböző értéket kapott, akkor írja ki, hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal. Ha nem három különböző számot kapott, akkor írja a képernyőre a legkisebb értéket ezek közül!


def beker(sorszam):
    be_szam = int(input(f"Kérem a(z) {sorszam}. számot: ") or "3")
    return be_szam


lista = []
lista.append(beker(1))
lista.append(beker(2))
lista.append(beker(3))
lista.sort()


print("A három bekért szám: " + ", ".join(map(str, lista)))

if lista[0] % 2 == 0 and lista[1] % 2 == 0 and lista[2] % 2 == 0:
    print("Mindhárom szám páros!")
else:
    print("Van közöttük nem páros szám!")


if lista[0] != lista[1] and lista[0] != lista[2] and lista[1] != lista[2]:
    # print(", ".join(map(str,lista)))
    if lista[0] + lista[1] == lista[2]:
        print(f"{lista[0]}+{lista[1]}={lista[2]}")
else:
    print(f"A legkisebb szám: {lista[0]}")


# 1/B/2. Írjon egy Python programot, amely bekér egy dátumot három pozitív egész számként (év, hó, nap)! A program határozza meg, hogy az adott dátum az év hányadik napja!
# 31 napos hónapok: január, március, május, július, augusztus, október, december;
# 30 napos hónapok: április, június, szeptember, november;
# A február 28 (szökőév esetén 29) napos.
# Egy év két esetben lesz szökőév. Egyik lehetőség, ha az évszám maradék nélkül osztható 4-gyel, de 100-al nem. Másik lehetőség, ha az évszám maradék nélkül osztható 400-zal.


ev = int(input("Adja meg az évet: "))
honap = int(input("Adja meg a hónapot: "))
nap = int(input("Adja meg a napot: "))


def szoko_ev(ev):
    if (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0):
        return True
    else:
        return False


honap_napjai = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if szoko_ev(ev):
    honap_napjai[1] = 29

napok_szama = nap
for i in range(honap - 1):
    napok_szama += honap_napjai[i]

print(f"A(z) {ev}.{honap:02d}.{nap:02d} dátum a {napok_szama}. napja az évnek.")

# 1/B/3. A zenek.txt minden sora egy zene előadóját és címét tartalmazza, egymástól tabulátorral elválasztva. Írjon egy Python programot, ami beolvassa a zenek.txt szövegfájl adatait megfelelő adatszerkezetbe és a következő feladatokat oldja meg!
# a. Írja képernyőre, hogy hány zene adatait tartalmazza a szövegfájl!
# b. Kérje be egy előadó nevét és írassa ki az ő műveinek címét a képernyőre!
# c. Írja képernyőre a leghosszabb zene címét!
# d.	 Írja ki egy zene_statisztika.txt szövegfájlba az írók nevei mellett, hogy hány zenéjük van a listában!


zenek = []
zene = {}

with open("zenek.txt", "r", encoding="UTF-8") as bemenet:
    for sor in bemenet:
        adatok = sor.strip().split("\t")
        zene["eloado"] = adatok[0]
        zene["cim"] = adatok[1]
        zenek.append(zene)
        zene = {}

print(f"a. A fájl {len(zenek)} darab zene adatait tartalmazza.")

be_eloado = input("\nb. Kérem egy előadó nevét: ") or "Elvis Presley"
print(f"{be_eloado} zenéi:")
for zene in zenek:
    if zene["eloado"] == be_eloado:
        print(zene["cim"])


def maxkivalasztas(l):
    max_index = 0
    for i in range(1, len(l)):
        if len(l[i]["cim"]) > len(l[max_index]["cim"]):
            max_index = i
    return max_index


print(f"\nc. A leghosszabb zenecím: {zenek[maxkivalasztas(zenek)]['cim']}")

statisztika = {}
for zene in zenek:
    if zene["eloado"] in statisztika:
        statisztika[zene["eloado"]] += 1
    else:
        statisztika[zene["eloado"]] = 1

with open("zenek_statisztika.txt", "w", encoding="utf-8") as kimenet:
    for key in statisztika:
        print(f"{key} - {statisztika[key]}", file=kimenet)
