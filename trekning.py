import random
import time

def lesInnFraFil():
    try:
        f = open('deltakere.txt', 'r')
        liste = f.readlines()
        antall = len(liste)
        print("\nImportert", antall, "deltakere fra fil.\n")
        f.close()
        # lager ryddig liste uten linjeskift
        i = 0
        while i < len(liste):
            liste[i] = liste[i].strip()
            i += 1
    except IOError:
        print("\nEn feil oppstod ved lesing av deltakere.txt\n")
        exit()
    return liste

def omrokkerListe(liste):
    omrokkertListe = random.shuffle(liste)
    return omrokkertListe

def trekkVinner():
    antall = len(deltakerliste) - 1
    vinnerrad = random.randint(0, antall)
    print("\nVinneren er... \n")
    time.sleep(1)
    print("\t", deltakerliste[vinnerrad], "\n")

def visMeny():
    menyvalg = input("[D]eltakere, [T]rekning, [A]vslutt: ")
    if menyvalg.upper() == "D":
        print("\nHer er listen over deltakere:")
        print(deltakerliste)
        print("\n")
    elif menyvalg.upper() == "T":
        print("\nStokker om på listen over deltakere og trekker en vinner...")
        omrokkerListe(deltakerliste)
        time.sleep(1)
        trekkVinner()
    elif menyvalg.upper() == "A":
        exit()


deltakerliste = lesInnFraFil()

start = True
while start:
    visMeny()
