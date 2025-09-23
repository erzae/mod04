import random
#monikko eli (tuple) on "kuin lista, jota ei voi muokata"

lista = [1, 2, 3, 4, 5 ]
print(lista)

monikko = (1, 2, 3, 4, 5)
monikko2 = 1, 2, 3, 4, 5
print(monikko)
print(monikko2)

# monikko voi sisältää erilaista tietoa
monikko3 = (1, 'abc', 23 )
print(monikko3)

print(lista[0])

#Toisin kuin lista, monikko on kuitenkin muuttumaton:
# siihen ei voi lisätä alkioita eikä siitä voi poistaa alkioita monikon luonnin jälkeen.

# monikon arvo muuttujiin

hedelmät = ('Lime', 'Sitruuna', 'Ananas')
#(eka, toka, kolmas) = ('Lime', 'Sitruuna', 'Ananas')
(eka, toka, kolmas) = hedelmät
print(hedelmät)
print("Monikko purettu muuttujiin, tässä eka", eka)

# monikon voi antaa funktiolle parametreinä

def tulosta_monikko(hedelmät):
    for h in hedelmät:
        print(h)
tulosta_monikko(hedelmät)

# perinteisesti
def heitä():
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    #toka = random.randint(1, 6)
    return eka, toka

noppa1, noppa2 = heitä()
print(f'Nopista tuli {noppa1} ja {noppa2}')


print('---------------------------------------')
print("JOUKKO!")

#joukko eli set {} on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.
# alkioihin ei voi myöskään viitata indeksillä
#Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen

# joukko merkataan aaltosulkeolla {}
joukko = {1, 2 , 3, 4, 5, 6}
print(joukko)


llista = [1, 2, 3, 4, 5, 6]
monikkolista = (1, 2, 3, 4, 5, 6)
print(f'numero 6 EI voi esiintyä joukossa useasti')
jjoukko = (1, 2, 3, 4, 5, 6)
print(jjoukko)




#tyhjän listan luominen

autolista = []
autolista.append('audi')
print(autolista)
print(type(autolista))

#tyhjä joukko
autojoukko = set()
autojoukko.add("mersu")
print(autojoukko)
print(type(autojoukko))