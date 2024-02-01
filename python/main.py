from bs4 import BeautifulSoup
import requests

wetterWildau = requests.get("https://www.wetter.com/deutschland/wildau/DE0011610.html#wetter")
soup = BeautifulSoup(wetterWildau.text, features="html.parser")
navGrid = soup.find("div", {"class": "[ forecast-navigation-grid ]"})
days = navGrid.findChildren("a" , recursive=False)

for day in days:
    if day.find("span", {"class": "[ forecast-navigation-temperature-max ]"}) == None:
        continue
    print(day.find("div").getText().strip())
    print("Maximal-Temperatur: " + day.find("span", {"class": "[ forecast-navigation-temperature-max ]"}).getText())
    print("Minimum-Temperatur: "+ day.find("span", {"class": "[ forecast-navigation-temperature-min ]"}).getText())
    print("Regen-Warscheinlichkeit: "+ day.find("span", {"class": "[ forecast-navigation-precipitation-probability ]"}).getText())
    print("-------------------------------")

wetter24Wildau = requests.get("http://www.wetter24.de/vorhersage/7tage/deutschland/wildau/18228508/")
soup2 = BeautifulSoup(wetter24Wildau.text, features="html.parser")
tableRows = soup2.find("tbody")
for row in tableRows:
    print(row.getText().strip())
    days = navGrid.findChildren("td" , recursive=False)

    for day in days:
        print(day.getText())
        if day.find("td.tempvx") == None:
            continue
        print(day.find("span", {"class": "date"}).getText().strip())
        print("Maximal-Temperatur: " + day.find("td", {"class": "tempvx"}).getText())
        print("Minimum-Temperatur: "+ day.find("td", {"class": "tempvn"}).getText())
        ("Regen-Warscheinlichkeit: "+ day.find("td").getText())
        print("-------------------------------")