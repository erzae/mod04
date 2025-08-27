# tehtävä 1
from random import random
from selectors import SelectSelector

pituus = float(input("Mikä on kuhan pituus senttimetreinä?: "))
if pituus>=37:
    print("Kuha on normaalimittainen!")

else:
    puuttuu = 37 - pituus
    print("Kuha on alimittainen, laske kuha takaisin järveen!")
    print(f"kuha on {puuttuu:} cm liian lyhyt!")


# tehtävä 2.

hyttiluokka = input("Mikä on hyttiluokkasi?:")
if hyttiluokka == "LUX":
    print("Hytti on parvekkeellinen ja yläkannella")
elif hyttiluokka == "A":
    print("Hytti on ikkunallinen ja autokannen yläpuolella")
elif hyttiluokka == "B":
    print("Hytti on ikkunaton ja autokannen yläpuolella")
elif hyttiluokka == "C":
    print("hytti on ikkunaton ja autokannen alapuolella")

elif hyttiluokka < "LUX" or "A" or "B" or "C":
    print("Virheellinen hyttiluokka!")


# tehtävä 3.

import math

sukupuoli = input("Mikä on sukupuolesi?:")
if sukupuoli == "nainen":
    hemoglobiiniarvo = float(input("Mikä on hemoglobiiniarvosi?:"))
    if hemoglobiiniarvo < 117 :
        print("Arvot ovat matalat!")
    if hemoglobiiniarvo > 175 :
        print("Arvot ovat liian korkeat!")
    elif hemoglobiiniarvo >= 117 or hemoglobiiniarvo > 175 :
        print("Arvot ovat normaalit!")

elif sukupuoli == "mies":
    hemoglobiiniarvo = float(input("Mikä on hemoglobiiniarvosi?:"))
    if hemoglobiiniarvo < 134:
        print("Arvot ovat matalat!")
    if hemoglobiiniarvo > 195:
        print("Arvot ovat liian korkeat!")
    elif hemoglobiiniarvo >= 134 or hemoglobiiniarvo >= 195:
        print("Arvot ovat normaalit!")

# tehtävä 4.

import math

vuosi = int(input("Mikä on vuosiluku?: "))
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi!")
else:
    print(f"{vuosi} ei ole karkausvuosi!")



























