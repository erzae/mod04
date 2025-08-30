#tehtävä-1
from ctypes import pythonapi

kolmella_jaolliset_numerot = int(input("Numerot väliltä 1-1000: "))
while kolmella_jaolliset_numerot != 1000:
    if kolmella_jaolliset_numerot % 3 == 0:
        print(kolmella_jaolliset_numerot)
    kolmella_jaolliset_numerot += 1

#tehtävä-2
negatiivinen_tuuma = 2.54
tuumat = float(input("Mikä on tuumamäärä?: "))
while tuumat != 0:
    cm = tuumat * negatiivinen_tuuma
    print(f"{tuumat} tuumaa on {cm:.2f} cm")
    tuumat = float(input("Mikä on tuumamäärä?:"))

print("Ohjelma päättyi!")

#tehtävä-3

pienin = None
suurin = None

while True:
    syöte = input("Anna numero:")
    if syöte == "":
        break
    try:
        luku = float(syöte)
        if pienin is None or luku < pienin:
            pienin = luku
        if suurin is None or luku > suurin:
            suurin = luku
    except ValueError:
        print("Syötteen täytyy olla numero tai tyhjä merkkijono")

if pienin is not None and suurin is not None:
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")

else:
    print("Et antanut lukua.")

#tehtävä-4

import random

arvottu_luku = random.randint(1, 10)

arvaus= float(input("Arvaa tietokoneen arpomaa lukua!:"))

while True:
    try:
        arvaus = int(input("Arvaa tietokoneen arpomaa lukua!:"))
        if arvaus < arvottu_luku:
            print("Liian pieni arvaus!")
        elif arvaus > arvottu_luku:
            print("Liian suuri arvaus!")
        else:
            print("Oikein!!")
            break

    except ValueError:
        print("Anna kokonaisluku välillä 1-10")

# tehtävä-5

oikea_käyttäjätunnus ="python"
oikea_salasana ="rules"

yritykset = 0

while yritykset < 5:
    annettu_käyttäjätunnus = input("Mikä on käyttäjätunnus?:")
    annettu_salasana = input("Mikä on salasana?:")

    if annettu_käyttäjätunnus == oikea_käyttäjätunnus and annettu_salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana!")
        yritykset += 1
if yritykset == 5:
    print("Kokeilukerrat loppu!")

import random

# kaikkien pisteiden määrä N

N = 10

print("Mikä on N: arvo):")

n = 0
i = 0
while i < N:
    i = i + 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")





