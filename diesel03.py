from selenium import webdriver
from selenium.webdriver.firefox.options import Options as ffopt
import time
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear')
cmd = 'mode 70,20'

webAddress = "https://www.polttoaine.net/Oulu"
webElement = "#Hinnat > table > tbody > tr:nth-child(2) > td:nth-child(5)"

def scrapy(address, element):
    options = ffopt()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(address)
    time.sleep(1)
    search = driver.find_element_by_css_selector(element)
    result = search.get_attribute("innerText")
    driver.quit()
    return result

def laske_hinta(kilsat, kulutus, keskihinta):
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
            luku = float(input("     Anna keskikulutus (l/km): "))
        except ValueError:
            print("     Arvon tulee olla pelkkä luku")
            print("")
        else:
            return luku

if __name__ == "__main__":
    os.system(cmd)
    print("")
    print("  Haetaan dieselin hintaa..")
    keskihinta = float(scrapy(webAddress, webElement))
    clearConsole()
    print("")
    print("    Tämä ohjelma laskee matkan hinnan diesel-autolla")
    print("    ajettuna käyttäen ajantasaista dieselin keskihintaa:")
    print("")
    kulutus = kysy_kulutus()
    clearConsole()
    print("")
    print("    Tämä ohjelma laskee matkan hinnan diesel-autolla")
    print("    ajettuna käyttäen ajantasaista dieselin keskihintaa.")
    print("    (Syötä 0km lopettaaksesi ja 999km vaihtaaksesi kulutuksen.)")
    print("")
    print("    Diesel: {}€/L".format(keskihinta))
    print("    Keskikulutus {}L/100km".format(kulutus))
    print("")
    while True:
        matka = kysy_matka()
        if matka == 0:
            break
        elif matka == 999:
            print("")
            kulutus = kysy_kulutus()
            print("")
        else:
            hinta = float(laske_hinta(matka, kulutus, keskihinta))
            time.sleep(0.01)
            print("")
            print("      Matkasi hinta on noin {:.2f}€".format(hinta))
            print("")
    