#tehtävä-1
from ipaddress import summarize_address_range

käyttäjä = input("Anna nimesi: ")
print("Terve, " + käyttäjä + "!")

#tehtävä-2

import math
sade = float(input("Anna ympyrän säde: "))
pinta_ala= math.pi * sade ** 2

print(f"ympyrän pinta-ala on: {pinta_ala}")

#tehtävä-3
import math
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))
piiri = 2 * (kanta + korkeus)
pinta_ala = math.sqrt(kanta ** 2 * korkeus ** 2)
print(f"suorakulmion pinta-ala on: {pinta_ala}")
print(f"suorakulmion piiri  on: {piiri}")

# tehtävä-4

kokonaisluku_1 = float(input("Anna ensimmäinen kokonaisluku: "))
kokonaisluku_2 = float(input("Anna toinen kokonaisluku: "))
kokonaisluku_3 = float(input("Anna kolmas kokonaisluku: "))

import math

summa = kokonaisluku_1 + kokonaisluku_2 + kokonaisluku_3
tulo = kokonaisluku_1 * kokonaisluku_2 * kokonaisluku_3
keskiarvo = summa / 3
print(f"kokonaislukujen summa on: {summa}")
print(f"kokonaislukujen tulo on: {tulo}")
print(f"kokonaislukujen keskiarvo on: {keskiarvo}")

#tehtävä-5
luoti_grammoina= 13,3
luoteja_naulassa= 32
naulaa_lieviskässä= 20

lieviskät = float(input("Anna lieviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))





