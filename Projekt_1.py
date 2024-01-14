"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Matějková
email: luciematejko@seznam.cz
discord: kuroel1369
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
] 
registered_users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"}

oddelovac = ("-" * 40)
pocet_textu = str(len(TEXTS))

name = input("Enter username: ")
password = input("Enter password: ")
print("Username:", name)
print("Password:", password)

print(oddelovac)

if name in registered_users and registered_users[name] == password:
    print("Welcome " + name + "! \nWe have " + pocet_textu + " texts to be analyzed.")
    print(oddelovac)
else:
    print("You are not registered user, " + name + "! Terminating program.")
    exit()

number = input("Enter a number between 1 and " + pocet_textu + " to select: ")

print(oddelovac)

if not number.isdigit() or not 1 <= int(number) <= len(TEXTS):
     print("Invalid input. You must enter a number between 1 and " + pocet_textu + ". Terminating program.")
     exit()

else:
     vybrany_text = TEXTS[int(number) - 1].split()

     velka_pismena = 0
     velka_slova = 0
     mala_slova = 0
     cisla = 0
     soucet_cisel = 0

     for pismeno in vybrany_text:
         if pismeno.istitle():
              velka_pismena += 1
         if pismeno.isupper():
              velka_slova += 1
         if pismeno.islower():
              mala_slova += 1
         if pismeno.isnumeric():
              cisla += 1
         if pismeno.isdigit():
              soucet_cisel += int(pismeno)

     print("There are",len(vybrany_text), "words in the selected text.")
     print("There are", velka_pismena, "titlecase words.")
     print("There are", velka_slova, "uppercase words.")
     print("There are", mala_slova, "lowercase words.")
     print("There are", cisla, "numeric strings.")
     print("The sum of all the numbers is", soucet_cisel, ".")

print(oddelovac)

print("LEN|" + (" " * 7) + "OCCURENCES" + (" " * 7) + "|NR.")

print(oddelovac)

if int(number) in range(1, len(TEXTS) + 1):
    vybrany_text = TEXTS[int(number) - 1].split()
    
    jedno_slovo = 0
    dve_slova = 0
    tri_slova = 0
    ctyri_slova = 0
    pet_slov = 0
    sest_slov = 0
    sedm_slov = 0
    osm_slov = 0
    devet_slov = 0
    deset_slov = 0
    jedenact_slov = 0
    dvanact_slov = 0
    trinact_slov = 0

    for slovo in vybrany_text:
         if len(slovo.strip(", . ! ?")) == 1:
              jedno_slovo += 1
         if len(slovo.strip(", . ! ?")) == 2:
              dve_slova += 1
         if len(slovo.strip(", . ! ?")) == 3:
              tri_slova += 1
         if len(slovo.strip(", . ! ?")) == 4:
              ctyri_slova += 1
         if len(slovo.strip(", . ! ?")) == 5:
              pet_slov += 1
         if len(slovo.strip(", . ! ?")) == 6:
              sest_slov += 1
         if len(slovo.strip(", . ! ?")) == 7:
              sedm_slov += 1
         if len(slovo.strip(", . ! ?")) == 8:
              osm_slov += 1
         if len(slovo.strip(", . ! ?")) == 9:
              devet_slov += 1
         if len(slovo.strip(", . ! ?")) == 10:
              deset_slov += 1
         if len(slovo.strip(", . ! ?")) == 11:
              jedenact_slov += 1
         if len(slovo.strip(", . ! ?")) == 12:
              dvanact_slov += 1
         if len(slovo.strip(", . ! ?")) == 13:
              trinact_slov += 1

    print(" 1 |", "*" * jedno_slovo, len("*" * jedno_slovo))   
    print(" 2 |", "*" * dve_slova, len("*" * dve_slova))    
    print(" 3 |", "*" * tri_slova, len("*" * tri_slova))   
    print(" 4 |", "*" * ctyri_slova, len("*" * ctyri_slova)) 
    print(" 5 |", "*" * pet_slov, len("*" * pet_slov))
    print(" 6 |", "*" * sest_slov, len("*" * sest_slov)) 
    print(" 7 |", "*" * sedm_slov, len("*" * sedm_slov)) 
    print(" 8 |", "*" * osm_slov, len("*" * osm_slov))
    print(" 9 |", "*" * devet_slov, len("*" * devet_slov))
    print("10 |", "*" * deset_slov, len("*" * deset_slov))
    print("11 |", "*" * jedenact_slov, len("*" * jedenact_slov))
    print("12 |", "*" * dvanact_slov, len("*" * dvanact_slov))
    print("13 |", "*" * trinact_slov, len("*" * trinact_slov))


     





