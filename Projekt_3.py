"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lucie Matějková
email: luciematejko@seznam.cz
discord: kuroel1369
"""

# python Projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302" vysledky_voleb.csv

import csv
import requests
import bs4 
import sys


volici = []
obalky = []
platne_hlasy = []


url_hlavni_stazeno = False

def hlavni_url(link): # uložení adresy z argumentu
    global url_hlavni_stazeno
    if not url_hlavni_stazeno:
        print("Stahuji data z hlavní url:", link)
        url_hlavni_stazeno = True
    geter = requests.get(link)
    html = bs4.BeautifulSoup(geter.text, "html.parser")
    return html


if len(sys.argv) == 3:
    hlavni_html = hlavni_url(sys.argv[1])  # uložení html do proměnné pro opakované využití
else:
    print("Nesprávný počet argumentů. Argumenty musí být 2. "
          "Zadej název souboru, který zpouštíš, url adresu, ze které získáváš data, v uvozovkách a libovolný název výstupního .csv.")
    quit()



def get_id(): # Vrací kódy obcí
    city_id = []
    ids = hlavni_html.find_all("td", "cislo")
    for id in ids:
        city_id.append(id.text)
    return city_id

def get_city(): # Vrací seznam měst v daném okrese
    cities = []
    cities_search = hlavni_html.find_all("td", "overflow_name")
    for t in cities_search:
        cities.append(t.text)
    return cities

def get_links(): # Vrací URL jednotlivých obcí
    urls = []
    link_search = hlavni_html.find_all("td", "center", "href")
    for link_town in link_search:
        link_town = link_town.a["href"]
        urls.append(f"https://volby.cz/pls/ps2017nss/{link_town}")
    return urls

def collect_parties(): # Vrací seznam kandidujících stran v daném okresu
    parties = []
    town_link = get_links()
    html = requests.get(town_link[0])
    html_villages = bs4.BeautifulSoup(html.text, "html.parser")
    party = html_villages.find_all("td", "overflow_name")
    for p in party:
        parties.append(p.text)
    return parties

def get_voters_sum():
    path = get_links()
    for p in path:
        html_path = requests.get(p)
        html_village = bs4.BeautifulSoup(html_path.text, "html.parser")
        voter = html_village.find_all("td", headers="sa2")
        for v in voter:
            v = v.text
            volici.append(v.replace('\xa0', ' '))
        attend = html_village.find_all("td", headers="sa3")
        for a in attend:
            a = a.text
            obalky.append(a.replace('\xa0', ' '))
        correct = html_village.find_all("td", headers="sa6")
        for c in correct:
            c = c.text
            platne_hlasy.append(c.replace('\xa0', ' '))

def collect_votes():
    links = get_links()
    votes = []
    for li in links:
        html = hlavni_url(li)
        votes_search = html.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])
        temporary = []
        for v in votes_search:
            temporary.append(v.text)
        votes.append(temporary)
    return votes

def whiterows_creator():
    rows = []
    get_voters_sum()
    towns = get_city()
    ids = get_id()
    votes = collect_votes()
    zipped = zip(ids, towns, volici, obalky, platne_hlasy)
    aux_var = []
    for i, t, v, a, vo in zipped:
        aux_var.append([i, t, v, a, vo])
    zip_all = zip(aux_var, votes)
    for av, vs in zip_all:
        rows.append(av + vs)
    return rows

def election_results(link, file): # Hlavní část funkce
    try:
        header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
        content = whiterows_creator()
        parties = collect_parties()
        print("Ukládám data do .csv souboru:", file)
        for party in parties:
            header.append(party)
        with open(file, 'w', newline='') as f:
            f_writer = csv.writer(f, delimiter= ",")
            f_writer.writerow(header)
            f_writer.writerows(content)
        print("Ukončuji program:", sys.argv[0])
    except IndexError:
        print("Nastala chyba. Nejspíš máte špatný odkaz nebo jste jej zapomněli dát do uvozovek.")
        quit()


if __name__ == '__main__':
    URL_adresa = sys.argv[1]
    nazev_souboru = sys.argv[2]
    election_results(URL_adresa, nazev_souboru)