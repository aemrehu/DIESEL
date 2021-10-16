from selenium import webdriver
from selenium.webdriver.firefox.options import Options as ffopt
import time

kulutus = 6.2

def scrapy():
    options = ffopt()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    driver.get("https://www.polttoaine.net/")
    time.sleep(1)
    search = driver.find_element_by_css_selector(
    "#Halvin_Kallein > tbody > tr:nth-child(2) > td:nth-child(5)"
    )
    keskih = search.get_attribute("innerText")
    driver.quit()
    return keskih

def laske_hinta(kilsat):
    summa = (kulutus / 100) * kilsat * keskihinta
    return summa

def kysy_matka():
    while True:
        try:
            luku = float(input("     Anna matkan pituus (km): "))
        except ValueError:
            print("     Arvon tulee olla pelkkä luku")
            print("")
        else:
            return luku

def kysy_kulutus():
    while True:
        try:
            luku = float(input("     Anna kulutus (l/km): "))
        except ValueError:
            print("     Arvon tulee olla pelkkä luku")
            print("")
        else:
            return luku

if __name__ == "__main__":
    print("")
    print("  Initializing..")

    keskihinta = float(scrapy())

    print("")
    print("  Loading..")
    time.sleep(1)
    print("")
    kulutus = kysy_kulutus()
    print("")
    print("    Tämä ohjelma laskee matkan hinnan Volvo S80 D5 automaatilla")
    print("    ajettuna käyttäen ajantasaista dieselin keskihintaa:")
    print("    (Syötä 0km lopettaaksesi.)")
    print("")
    print("    Diesel: {}€/L".format(keskihinta))
    print("    Kulutus {}L/100km".format(kulutus))
    print("")
    while True:
        matka = kysy_matka()
        if matka == 0:
            break
        else:
            hinta = float(laske_hinta(matka))
            time.sleep(1)
            print("")
            print("      Matkasi hinta on noin {:.2f}€".format(hinta))
            print("")