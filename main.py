import os

# Fargekode for fancy terminal-utskrift
class Farger:
    BLÅ = '\033[94m'
    GRØNN = '\033[92m'
    RØD = '\033[91m'
    SLUTT = '\033[0m'

# Funksjon for å rydde terminalen for et renere utseende
def rydd_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funksjon for å printe velkomstmeldingen og navnevalg
def velkomst():
    rydd_terminal()
    print(Farger.BLÅ + "Velkommen til 3 på rad!" + Farger.SLUTT)
    print("Husk, målet er å få 3 på rad horisontalt, vertikalt eller diagonalt.")
    print("Lykke til!" + "\n")
    spiller_1 = input("Hva er navn til spiller 1 (X)? ")
    spiller_2 = input("Hva er navn til spiller 2 (O)? ")
    return spiller_1, spiller_2

# Funksjon for å skrive ut brettet
def spillbrett(brett):
    # Header med kolonne nummer
    print(Farger.GRØNN + "  1   2   3" + Farger.SLUTT)
    # Gå gjennom hver rad og skriv ut med radnummer
    for indeks, rad in enumerate(brett, start=1):
        print(Farger.GRØNN + str(indeks) + Farger.SLUTT, " | ".join(rad))
        if indeks < len(brett):  # Ikke skriv linje under siste rad
            print("  ---------")

# Funksjon for å sjekke om det er en vinner
def sjekk_vinner(brett):
    # Sjekk rader
    for rad in brett:
        if rad[0] == rad[1] == rad[2] and rad[0] != " ":
            return rad[0]
    # Sjekk kolonner
    for kol in range(3):
        if brett[0][kol] == brett[1][kol] == brett[2][kol] and brett[0][kol] != " ":
            return brett[0][kol]
    # Sjekk diagonal fra venstre øverst til høyre nederst
    if brett[0][0] == brett[1][1] == brett[2][2] and brett[0][0] != " ":
        return brett[0][0]
    # Sjekk diagonal fra venstre nederst til høyre øverst
    if brett[2][0] == brett[1][1] == brett[0][2] and brett[2][0] != " ":
        return brett[2][0]
    return None

# Funksjon for å sjekke om input er innenfor grensen
def sjekk_lovlig_input(kor1, kor2):
    if not (1 <= kor1 <= 3 and 1 <= kor2 <= 3):
        print(Farger.RØD + "Feil input: koordinater må være mellom 1 og 3." + Farger.SLUTT)
        return False
    return True

# Funksjon for å sjekke om det er en uavgjort (fullt brett)
def sjekk_uavgjort(brett):
    for rad in brett:
        if " " in rad:
            return False
    return True

# Hovedspill-funksjon
def main():
    spiller_1, spiller_2 = velkomst()
    nåværende_spiller = spiller_1
    nåværende_symbol = "X"
    
    while True:
        # Opprett et nytt brett
        brett = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        rydd_terminal()
        spillbrett(brett)
        while True:
            try:
                # Be om trekk fra spilleren og konverter til listeindeks (0-2)
                trekk_rad = int(input(f"{nåværende_spiller} ({nåværende_symbol}), skriv inn raden (1-3): ")) - 1
                trekk_kol = int(input(f"{nåværende_spiller} ({nåværende_symbol}), skriv inn kolonnen (1-3): ")) - 1

                # Sjekk om trekket er lovlig
                if sjekk_lovlig_input(trekk_rad + 1, trekk_kol + 1) and brett[trekk_rad][trekk_kol] == " ":
                    brett[trekk_rad][trekk_kol] = nåværende_symbol
                    rydd_terminal()
                    spillbrett(brett)

                    # Sjekk om det er en vinner
                    vinner = sjekk_vinner(brett)
                    if vinner:
                        print(Farger.GRØNN + f"{nåværende_spiller} ({vinner}) har vunnet!" + Farger.SLUTT)
                        break

                    # Sjekk om det er uavgjort
                    if sjekk_uavgjort(brett):
                        print(Farger.RØD + "Det ble uavgjort!" + Farger.SLUTT)
                        break

                    # Bytt spiller
                    if nåværende_spiller == spiller_1:
                        nåværende_spiller = spiller_2
                        nåværende_symbol = "O"
                    else:
                        nåværende_spiller = spiller_1
                        nåværende_symbol = "X"
                else:
                    print(Farger.RØD + "Ugyldig trekk, prøv igjen." + Farger.SLUTT)
            except ValueError:
                print(Farger.RØD + "Ugyldig input, vennligst skriv inn tall mellom 1 og 3." + Farger.SLUTT)

        # Spør om spilleren vil spille igjen eller avslutte
        valg = input(Farger.BLÅ + "Vil dere spille igjen? (ja/nei): " + Farger.SLUTT).lower()
        if valg != "ja":
            print(Farger.GRØNN + "Takk for spillet! Ha en fin dag!" + Farger.SLUTT)
            break

# Start spillet
if __name__ == "__main__":
    main()
