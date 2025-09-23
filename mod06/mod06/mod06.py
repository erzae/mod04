# Funktio esimerkkejä

# funktio, joka ei ota parametrejä eikä palauta mitään
def say_hello():
    print("moi")
    print("sinä")


#funktio, joka ottaa vastaan parametriä
def say_hello_v2(username, age):
    #print("moi")
    #print(username)
    #print(f"ikäsi: {age}")
    username = username.capitalize() #muuttaa ensimmäisen kirjaimen isoksi.
    return f"{username}, age: {age}"  # < lopettaa funktion suorituksen
    #print() < ei ajeta, sillä käytettiin return.


#print(say_hello) < ei printtaa mitään
#say_hello()
#say_hello()
#print(say_hello()) < suorittaa funktion ja tulostaa paluuarvon None
print(say_hello_v2("erza", 20))
nimi = "maija"
return_value = say_hello_v2(nimi, 25)
print(return_value)
print(f"nimi muuttujan arvo: {nimi}")

print("---------------------------------------------")

# summa funktio

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  #built-in sum
print(sum([8, 9, 10]))

# oma toteutus
def my_sum(number_list):
    total = 0
    number_list.append(100) #lisää summaan aina 100 ylimääräisenä alkiona.
    for num in numbers:
        total = total + num
    return total


print(my_sum(numbers))
print(f"Alkuperäisen numbers-muuttujan arvo pääohjelmassa: {numbers}")
print(my_sum([8, 9, 10]))

print("----------------------------------------------------")

#listat ja muuttujat
list = [1, 2]
list2 = list.copy() # < listasta voidaan luoda kopio
list2.append(3)
print(f"Muuttujat list: {list} ja list2: {list2} viittaavat samaan listaan muistissa:")


