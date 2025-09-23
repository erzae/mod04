#tehtävä-1

import random

def noppa():
    return random.randint(1, 6)

silmaluku = noppa()

if silmaluku == 6:
    print("Saavutit tavoitteen! Sait silmäluvuksi 6!")
else:
    print(f"silmäluku on {silmaluku}")

#tehtävä-2
def noppa2(tahkot):
    return random.randint(1, tahkot)

tahkojen_maara = int(input("Anna tahkojen määrä:"))

silmäluku = noppa2(tahkojen_maara)

while silmäluku != tahkojen_maara:
    print(f"Nopasta tuli {silmäluku}")
    silmäluku = noppa2(tahkojen_maara)

print(f"Nopasta tuli arvo {silmäluku}")
print("Saavutit tavoitteen!")

#tehtävä-3

def muunna(nestegallonit):
    laske = nestegallonit * 3.785
    return laske

yhdysvallan_nestegallonit = float(input("Anna nestegallonit:"))
tulos = muunna(yhdysvallan_nestegallonit)
print(f"Nestegallonit litroina on : {tulos}")

#tehtävä-4

def lukujen_summa(kokonaisluvut):
    for k in kokonaisluvut:
        print(k)

lista = [2, 4, 5, 1]
lukujen_summa(lista)
summa = sum(lista)
print(f"Lukujen summa on: {summa}")

# tehtävä-5

def poista_parittomat(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

alkuperainen_lista = [3, 4, 2, 8]
karsittu_lista = poista_parittomat(alkuperainen_lista)
print(f"Alkuperäinen lista on: {alkuperainen_lista}")
print(f"...ja karsittu lista (vain parilliset luvut) on: {karsittu_lista}")

#tehtävä-6

import math

def yksikköhinta(halk_cm, hinta_euro):
    halkasija_m = halk_cm / 100

    sade = halkasija_m / 2
    pinta_ala = math.pi * sade ** 2

    return hinta_euro / pinta_ala

halk1 = float(input("Anna ensimmäisen pizzan halkasija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
yks1 = yksikköhinta(halk1, hinta1)

halk2 = float(input("Anna toisen pizzan halkasija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))
yks2 = yksikköhinta(halk2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta on: {yks1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta on: {yks2:.2f} €/m²")

if yks1 > yks2:
    print("Toinen pizza antaa paremman vastineen rahalle")
elif yks1 < yks2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
else:
    print("Molemmat pizzat ovat yhtä kattavia")






















