from itertools import count

nimi = "Erza"
nimi2 = "Matti"
num1 = 20
num2= 40

print(f'Hei {nimi} ikäsi on {num1}')

# tyhjä lista
lista = []

nimet = ['Anna', 'Liisa', nimi, nimi2]
print(nimet)

ikälista = [23, 34, 50, [98, 4, 17]]
print(ikälista)


print(len(nimet))

nimet_2 = ['Sofia', 'Ella', 'Miina', 'Alisa']
print(nimet_2)
print(len(nimet_2))


# listasta voidaan hakea tietoa alkion indeksin avulla tai
# alkioon viitataan indeksi numerolla, alkaen numerosta 0

print(f'Hei {nimet[0]} ja terve myös {nimet[3]}')

print(ikälista[3][1])
print(len(ikälista))

print("'''''''''''''''''")

nimet_3 = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", "Rasmus", "Kalle"]
print(nimet_3[3])
print(nimet_3[1])
print(nimet_3[1:5]) #(alkupiste mukaan lukien) ja indeksiin 3 päättyen (päätepiste pois lukien)
print(nimet_3[1:-1])

print("''''''''''''''''''")

uusi_lista = nimet_3[2:4]
print(nimet_3)
print(uusi_lista)


print("'''''''''''''''''''")

kaupungit = ['Helsinki', 'Pariisi', 'Madrid', 'Tukholma', 'Tokyo' ]

# lista, jossa 5 kaupunkia
# tulosta niistä 3 ensimmäistä ja viimeinen

print(kaupungit[:3])
print(kaupungit[-1])

#viittaus listan ulkopuolelle aiheuttaa virheen.

kaupungit.append('uusi kaupunki')
print(kaupungit)
kaupungit.remove('Helsinki')
print(kaupungit)

if 'Madrid' in kaupungit:
    print("Madrid löytyi ja poistetaan listasta!")
    # poistetaan kaupunki
    kaupungit.remove('Madrid')
    print(kaupungit)


kaupungit.insert(0, 'Madrid')
print(kaupungit)

monesko = kaupungit.index('Tukholma')
print(monesko)

lisää_kaupunkeja = ['Porvoo', 'Kotka', 'Sipöö']

kaupungit.extend(lisää_kaupunkeja)
print(kaupungit)

# muokataan olemassa olevaa alkiota indeksin(monesko) avulla

kaupungit[7] = 'Sipoo'
print(kaupungit)

hedelmiä = ['Appelsiini', 'Banaani', 'greippi', 'omena']
numerolista = [100, 5, 45, 75]

hedelmiä.sort()
print(hedelmiä)

# sorttaus toistepäin
numerolista.sort(reverse=True)
print(numerolista)

print("'''''''''''''''''")
print("Muutamia funktioita tulevaisuutta varten")
print("''''''''''''''''''")


luvut = (1, 1, 4, 2, 5, 5, 3, 2)
print(len(luvut)) #pituus
print(sum(luvut)) #summa
print(min(luvut)) #pienin luku
print(max(luvut)) #suurin luku
print(luvut.count(5)) #määrä
print(luvut.count(1))

print("'''''''''''''''''")
print("Miten käydään lista läpi iteroimalla")
print("''''''''''''''''''")

#luvut = (1, 1, 4, 2, 5, 5, 3, 2)

i = 0  # i on nolla!
while i < len(luvut):
    #print(i)
    print(luvut[i])
    i += 1

print("''''''''''''''''''")

#käydään lista läpi alkio alkiolta
for luku in luvut:
    print(luku)

print("''''''''''''''''''")

for kirjain in "abcdefg":
    print(kirjain)
print("''''''''''''''''''")
for alkio in [1, 2, 3, 4, 5]:
    print(alkio)

for kaikki in kaupungit:
    print(kaikki)

print("''''''''''''''''''")

for numero in range(5):
    print(numero)

for n in range(4, 81):
    print(n)

print("''''''''''''''''''")
for n in range(50, 8 , -2):
    print(n)


print("''''''''''''''''''")
#luvut = (1, 1, 4, 2, 5, 5, 3, 2)
pituus = len(luvut)
for n in range(pituus):
    print(n)

print("''''''''''''''''''")
# printataan vain kolme

for n in range(3):
    print(kaupungit[n])

