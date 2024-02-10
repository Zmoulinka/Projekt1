Elections Scraper
Projekt 3 pro Engeto Python Akademii

Popis projektu
Projekt má za úkol extrahovat výsledky z parlamentních z roku 2017 z odkazu https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ.

Instalace knihoven
Knihovny použité v kódu jsou uložené v souboru requirements.txt.

Spuštění projektu
Soubor Projekt_3.py se spouští z příkazového řádku a požaduje dva argumenty. A to odkaz na územní celek a libovolný název .csv souboru.

python Projekt_3.py "odkaz_uzemniho_celku" vysledky_voleb.csv

Výstupem pak je soubor .csv s výsledky voleb.

Ukázka projektu
Výsledky pro okres Pardubice:

argument -> https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302
argument -> vysledky_voleb.csv

Spuštění programu
python Projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302" vysledky_voleb.csv

Část běhu programu
Stahuji data z hlavní url: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302  
Ukládám data do .csv souboru: vysledky_voleb.csv
Ukončuji program: Projekt_3.py


Částečný výstup
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,...
574724,Barchov,170,113,113,5,0,0,9,0,12,7,0,3,1,0,0,14,0,3,40,0,1,3,0,0,0,15,0
574741,Bezděkov,262,164,163,18,0,0,5,0,14,9,7,1,2,0,0,20,0,7,58,0,1,3,4,2,0,11,1
574783,Borek,226,161,159,30,0,1,12,1,12,9,2,1,3,2,0,11,0,6,34,0,0,8,1,0,1,25,0
574791,Brloh,193,149,149,8,0,0,10,0,17,11,0,4,1,0,0,17,0,5,43,0,0,9,1,1,0,19,3
574805,Břehy,833,576,573,65,1,0,43,0,30,66,9,4,0,0,0,58,0,18,198,0,2,17,4,0,2,53,3
574813,Bukovina nad Labem,187,139,138,23,1,0,6,0,6,15,0,1,1,0,0,9,0,5,49,0,0,16,0,0,0,6,0
