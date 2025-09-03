# tehtävä-1

import random
n = int(input('Anna arpakuution määrä:'))
heitot = []
#total = 0

for i in range(n):
    heitto= (random.randint(1,6))
    print(heitto)
    #total = total + heitto
   # total += heitto
    heitot.append(heitto)


yhteissumma = sum(heitot)
print(f'Arpakuutioiden yhteissumma on: {yhteissumma}')


print("''''''''''''''''''''''''''''''''''''")


# tehtävä-2

luvut = []

n = input("Anna luku (tyhjä lopettaa:")

while n!='':
    print(n)
    luvut.append(int(n))
    n = input('Anna luku tyhjä lopettaa:')

luvut.sort(reverse=True)
print(luvut)

#for m in range(5):
    #print(m)

viisi_suurinta = luvut[:5]

for v in viisi_suurinta:
    print(v)


#while True:
    #luku = input("Anna luku:")
    #if luku == "":
        #break
    #luvut.append(luku)

print("''''''''''''''''''''''''''''''''''''")

#tehtävä-3

luku = int(input("Anna kokonaisluku ja tarkistan, onko se alkuluku!:"))
#if luku < 2:
    #print("Luku ei ole alkuluku.")

jaollinen = []

#oletusarvo on että luku on alkuluku, todennetaan tämä jakamalla

oikea_alkuluku = True

for i in range(2,luku):
    print(i)
    if luku % i == 0:
        oikea_alkuluku = False
        jaollinen.append(i)

if oikea_alkuluku:
    print(f'{luku} on alkuluku!')
else:
    print(f'{luku} ei ole alkuluku.')


#tehtävä-4
n= 5
kaupungit = []

for i  in range(n):
    nimi = input(f'Anna {i+1}. kaupungin nimi:')
    kaupungit.append(nimi)

for k in kaupungit:
    print(k)









