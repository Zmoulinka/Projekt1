"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lucie Matějková
email: luciematejko@seznam.cz
discord: kuroel1369
"""

import random
oddelovac = ("-" * 40)

print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
print(oddelovac)

def generovani_cisla():
    cisla = list(range(1, 10))
    random.shuffle(cisla)
    return ''.join(map(str, cisla[:4]))

gen_cislo = generovani_cisla()
# print(gen_cislo)

def posouzeni(gen_cislo, tip):
    bulls = sum(g == t for g, t in zip(gen_cislo, tip))
    cows = sum(min(gen_cislo.count(cislo), tip.count(cislo)) for cislo in set(tip) & set(gen_cislo)) - bulls
    
    return bulls, cows

pocet_pokusu = 0
while True:
    tip = input("Enter a 4 digit number: ")
    pocet_pokusu += 1

    if not tip.isdigit() or len(tip) != 4 or len(set(tip)) != 4 or tip[0] == '0':
        print("Invalid input. Please enter a 4-digit number with unique digits and without zeros.")
        continue
    elif tip == gen_cislo:
        print("Congratulations! You've guessed the right number which is " + gen_cislo + "!")
        print(f"You've guessed it in {str(pocet_pokusu)} {'guess' if pocet_pokusu == 1 else 'guesses'}!")
        exit()
        

    bulls, cows = posouzeni(gen_cislo, tip)

    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

    if bulls == 4:
        print("Congratulations! You've guessed the right number" + gen_cislo + "!")
        exit()

