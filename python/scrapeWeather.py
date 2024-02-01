from bs4 import BeautifulSoup
import requests
import os

# Step1: User nach PLZ fragen
input = input("Postleitzahl eingeben: ")

# Step2: PLZ überprüfen (5 lang, nur zahlen); wenn nicht ok nochmal fragen
inputLength = (len(input))

if not input.isdigit():
    print(input+" ist keine Zahl")
    os.abort()

if inputLength != 5:
    print(input +" entspricht nicht der PLZ Länge(5)")
    os.abort()

# Step3: https://www.wetter.com/suche/?q=PLZ nutzen um die Adresse zu kriegen
adresse = "https://www.wetter.com/suche/?q=" + input

# Step4: Seite anfragen
wetter = requests.get(adresse)

# Step5: scrape :)
soup = BeautifulSoup(wetter.text, features="html.parser")
navGrid = soup.find("div", {"class": "[ forecast-navigation-grid ]"})
# Step6: überprüfen ob die nächste Tage Reihe sichtbar ist
if navGrid == None:
    print("Ort konnte nicht gefunden werden")
    os.abort()
days = navGrid.findChildren("a" , recursive=False)

print(soup.find("div", {"id": "weather-headline"}).getText())

for day in days:
    if day.find("span", {"class": "[ forecast-navigation-temperature-max ]"}) == None:
        continue
    print(day.find("div").getText().strip())
    print("Maximal-Temperatur: " + day.find("span", {"class": "[ forecast-navigation-temperature-max ]"}).getText())
    print("Minimum-Temperatur: "+ day.find("span", {"class": "[ forecast-navigation-temperature-min ]"}).getText())
    print("Regen-Warscheinlichkeit: "+ day.find("span", {"class": "[ forecast-navigation-precipitation-probability ]"}).getText())
    print("-------------------------------")
