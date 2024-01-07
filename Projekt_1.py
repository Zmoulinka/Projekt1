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

name = input("Enter username: ")
password = input("Enter password: ")
print("Username:", name)
print("Password:", password)

print("-" * 40)

if name in registered_users and registered_users[name] == password:
    print("Welcome " + name + "! \nWe have 3 texts to be analyzed.")
    print("-" * 40)
else:
    print("You are not registered user, " + name + "! Terminating program.")
    exit()

number = input("Enter a number between 1 and 3 to select: ")
print("-" * 40)
if number.isdigit() == False:
     print("You must enter a number between 1 and 3. Terminating program.")
elif int(number) == 1:
    prvni_text = TEXTS[0].split()
    print("There are",len(prvni_text), "words in the selected text.")
    velka_pismena = 0
    for pismeno in prvni_text:
         if pismeno.istitle():
              velka_pismena += 1
    print("There are", velka_pismena, "titlecase words.")
    velka_slova = 0    
    for pismeno in prvni_text:
         if pismeno.isupper():
              velka_slova += 1
    print("There are", velka_slova, "uppercase words.")
    mala_slova = 0    
    for pismeno in prvni_text:
         if pismeno.islower():
              mala_slova += 1
    print("There are", mala_slova, "lowercase words.")
    cisla = 0    
    for cislo in prvni_text:
         if cislo.isnumeric():
              cisla += 1
    print("There are", cisla, "numeric strings.")
    soucet_cisel = 0
    for soucet in prvni_text:
         if soucet.isdigit():
              soucet_cisel += int(soucet)
    print("The sum of all the numbers is", soucet_cisel, ".")
elif int(number) == 2:
    druhy_text = TEXTS[1].split()
    print("There are",len(druhy_text), "words in the selected text.")
    velka_pismena = 0
    for pismeno in druhy_text:
         if pismeno.istitle():
              velka_pismena += 1
    print("There are", velka_pismena, "titlecase words.")
    velka_slova = 0    
    for pismeno in druhy_text:
         if pismeno.isupper():
              velka_slova += 1
    print("There are", velka_slova, "uppercase words.")
    mala_slova = 0    
    for pismeno in druhy_text:
         if pismeno.islower():
              mala_slova += 1
    print("There are", mala_slova, "lowercase words.")
    cisla = 0    
    for cislo in druhy_text:
         if cislo.isnumeric():
              cisla += 1
    print("There are", cisla, "numeric strings.")
    soucet_cisel = 0
    for soucet in druhy_text:
         if soucet.isdigit():
              soucet_cisel += int(soucet)
    print("The sum of all the numbers is", soucet_cisel, ".")
elif int(number) == 3:
    treti_text = TEXTS[2].split()
    print("There are",len(treti_text), "words in the selected text.")
    velka_pismena = 0
    for pismeno in treti_text:
         if pismeno.istitle():
              velka_pismena += 1
    print("There are", velka_pismena, "titlecase words.")
    velka_slova = 0    
    for pismeno in treti_text:
         if pismeno.isupper():
              velka_slova += 1
    print("There are", velka_slova, "uppercase words.")
    mala_slova = 0    
    for pismeno in treti_text:
         if pismeno.islower():
              mala_slova += 1
    print("There are", mala_slova, "lowercase words.")
    cisla = 0    
    for cislo in treti_text:
         if cislo.isnumeric():
              cisla += 1
    print("There are", cisla, "numeric strings.")
    soucet_cisel = 0
    for soucet in treti_text:
         if soucet.isdigit():
              soucet_cisel += int(soucet)
    print("The sum of all the numbers is", soucet_cisel, ".")           
elif int(number) > 3:
     print("You've chosen poorly. Terminating program.")
     exit()
elif int(number) == 0:
     print("You've chosen poorly. Terminating program.")
     exit()

print("-" * 40)

print("LEN|" + (" " * 7) + "OCCURENCES" + (" " * 7) + "|NR.")

print("-" * 40)

if int(number) == 1:
    prvni_text = TEXTS[0].split()
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 1:
              pocet_slov += 1
    print(" 1 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 2:
              pocet_slov += 1
    print(" 2 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 3:
              pocet_slov += 1
    print(" 3 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 4:
              pocet_slov += 1
    print(" 4 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 5:
              pocet_slov += 1
    print(" 5 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 6:
              pocet_slov += 1
    print(" 6 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 7:
              pocet_slov += 1
    print(" 7 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 8:
              pocet_slov += 1
    print(" 8 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 9:
              pocet_slov += 1
    print(" 9 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 10:
              pocet_slov += 1
    print("10 |", "*" * pocet_slov, len("*" * pocet_slov))
    pocet_slov = 0
    for slovo in prvni_text:
         if len(slovo.strip(", . ! ?")) == 11:
              pocet_slov += 1
    print("11 |", "*" * pocet_slov, len("*" * pocet_slov))
elif int(number) == 2:
     druhy_text = TEXTS[1].split()
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 1:
              pocet_slov += 1
     print(" 1 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 2:
              pocet_slov += 1
     print(" 2 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 3:
              pocet_slov += 1
     print(" 3 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 4:
              pocet_slov += 1
     print(" 4 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 5:
              pocet_slov += 1
     print(" 5 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 6:
              pocet_slov += 1
     print(" 6 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 7:
              pocet_slov += 1
     print(" 7 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 8:
              pocet_slov += 1
     print(" 8 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 9:
              pocet_slov += 1
     print(" 9 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 10:
              pocet_slov += 1
     print("10 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in druhy_text:
         if len(slovo.strip(", . ! ?")) == 11:
              pocet_slov += 1
     print("11 |", "*" * pocet_slov, len("*" * pocet_slov))
elif int(number) == 3:
     treti_text = TEXTS[2].split()
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 1:
              pocet_slov += 1
     print(" 1 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 2:
              pocet_slov += 1
     print(" 2 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 3:
              pocet_slov += 1
     print(" 3 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 4:
              pocet_slov += 1
     print(" 4 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 5:
              pocet_slov += 1
     print(" 5 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 6:
              pocet_slov += 1
     print(" 6 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 7:
              pocet_slov += 1
     print(" 7 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 8:
              pocet_slov += 1
     print(" 8 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 9:
              pocet_slov += 1
     print(" 9 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 10:
              pocet_slov += 1
     print("10 |", "*" * pocet_slov, len("*" * pocet_slov))
     pocet_slov = 0
     for slovo in treti_text:
         if len(slovo.strip(", . ! ?")) == 11:
              pocet_slov += 1
     print("11 |", "*" * pocet_slov, len("*" * pocet_slov))




