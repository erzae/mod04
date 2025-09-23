#tehtävä-1

talvi = (12, 1, 2)
kevät = (3, 4, 5)
kesä = (6, 7, 8)
syksy = (9, 10, 11)

numero = int(input("Anna kuukauden numero (1-12): "))

if numero in talvi:
    print("Kuukaudenaika on talvi!")
elif numero in kevät:
    print("Kuukaudenaika on kevät!")
elif numero in syksy:
    print("Kuukaudenaika on syksy!")
elif numero in kesä:
    print("Kuukaudenaika on kesä!")

# tehtävä-2

nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet")
for n in nimet:
    print(n)


