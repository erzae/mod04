import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="erzae",
    password="aechei6o",
    autocommit=True
)

#tehtävä-1
def hae_lentokentta(icao):
    cursor = connection.cursor()
    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    result = cursor.fetchone()
    if result:
        print(f"Lentokenttä: {result[0]}, Sijainti: {result[1]}")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")

icao_koodi = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
hae_lentokentta(icao_koodi)

#tehtävä-2

def lentokenttien_lukumaarat(maakoodi):
    cursor = connection.cursor()
    query = """
        SELECT airport.type, COUNT(*) 
        FROM airport 
        JOIN country ON airport.iso_country = country.iso_country 
        WHERE country.iso_country = %s 
        GROUP BY airport.type
    """
    cursor.execute(query, (maakoodi,))
    results = cursor.fetchall()
    if results:
        print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
        for kenttatyyppi, maara in results:
            print(f"{kenttatyyppi}: {maara} kpl")
    else:
        print("Ei löytynyt lentokenttiä annetulla maakoodilla.")


maakoodi = input("Anna maakoodi: ").strip().upper()
lentokenttien_lukumaarat(maakoodi)

