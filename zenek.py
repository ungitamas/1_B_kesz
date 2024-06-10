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
