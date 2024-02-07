import random
import time


def main():
    while True:
        visMeny()


def lesInnFraFil(filnavn):
    try:
        f = open(filnavn, 'r')
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
    print("\nStokker om på listen over deltakere...")
    time.sleep(1)
    random.shuffle(liste)


def trekkVinner(liste):
    print("\nTrekker en vinner...")
    antall = len(liste) - 1
    vinnerrad = random.randint(0, antall)
    print("\nVinneren er... \n")
    time.sleep(1)
    print("\t", liste[vinnerrad], "\n")


def visDeltakere(liste):
    print("\nHer er listen over deltakere:")
    print(liste)
    print("\n")


def visMeny():
    menyvalg = input("[D]eltakere, [T]rekning, [A]vslutt: ")
    if menyvalg.upper() == "D":
        visDeltakere(deltakerliste)
    elif menyvalg.upper() == "T":
        omrokkerListe(deltakerliste)
        trekkVinner(deltakerliste)
    elif menyvalg.upper() == "A":
        exit()


if __name__=="__main__": 
    deltakerliste = lesInnFraFil("deltakere.txt")
    main()
