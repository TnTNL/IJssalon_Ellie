from algemene_functies import mijn_functie_2

def aanbieding_1():
    smaak = "aardbei"
    prijs = 4
    korting = 0.1
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - (prijs*korting)} euro.")

def inkomsten_totaal():
    btw = 0.09
    inkomsten = {
        "maandag": 220,
        "dinsdag" : 430,
        "woensdag" : 125,
        "donderdag" : 160,
        "vrijdag" : 205,
        "zaterdag" : 90,
        "zondag" : 345
    }   
    return (f'Het totaal van alle inkomsten van deze week is {sum(inkomsten.values())} euro, waarover {sum(inkomsten.values()) * btw} btw betaald dient te worden.')

def laag_en_hoog():
    mijn_lijst = {
        "maandag": 220,
        "dinsdag" : 430,
        "woensdag" : 125,
        "donderdag" : 160,
        "vrijdag" : 205,
        "zaterdag" : 90,
        "zondag" : 345
    }   
    return (f'{max(mijn_lijst)} {min(mijn_lijst)}')

def gemiddelde() :
    mijn_lijst = {
        "maandag": 220,
        "dinsdag" : 430,
        "woensdag" : 125,
        "donderdag" : 160,
        "vrijdag" : 205,
        "zaterdag" : 90,
        "zondag" : 345
    }   
    return (f'De gemiddelde inkomsten deze week zijn {sum(mijn_lijst)/7} euro.')

def meervoudig():
    invoer_lijst = {
        "1" : 10,
        "2" : 5,
        "3" : 3,
        "4" : 2,
        "5" : 1,
        "6" : 2,
        "7" : 9
    }
    return meervoudig(laag_en_hoog)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)