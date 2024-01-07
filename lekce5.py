# 1. Spočítejte součet všech prvků v daném seznamu pomocí for cyklu
seznam = [1, 2, 3, 4, 5]

# 2. Napište kód, který zkontroluje, zda je jméno přítomno ve slovníku a pokud ano, vypište přidružený věk.
data = {"Jan": 30, "Marie": 25, "Petr": 35}

# 3. Máte dva seznamy. Najděte společné prvky mezi nimi a uložte je do nového seznamu.
seznam1 = [1, 2, 3, 4, 5]
seznam2 = [3, 4, 5, 6, 7]

# 4. Napište program, který vezme seznam čísel a vytiskne pouze sudá čísla.
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 5. Máte seznam slov. Najděte a vypište nejdelší slovo v seznamu.
slova = ["jabko", "hory", "kočka", "programování", "knihovna"]

#1
seznam = [1, 2, 3, 4, 5]
#for cislo in seznam:
    #print(cislo)
soucet = 0
for cislo in seznam:
    soucet += cislo
print(soucet)

#2

jmeno = "Jan" #input("zadej jmeno")
for test in ["Jan", "Marie", "Petr"]:
    jmeno = test
    data = {"Jan": 30, "Marie": 25, "Petr": 35}
if jmeno in data:
    print(data["Jan"])
    
#3
seznam1 = [1, 2, 3, 4, 5]
seznam2 = [3, 4, 5, 6, 7]
seznam3 = []
for x in seznam1:
    if x in seznam2:
        seznam3.append(x)
        print(seznam3)

#4 
seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for cislo in seznam:
    if(cislo % 2) ==0:
        print(cislo)

#5
slova = ["jabko", "hory", "kočka", "programování", "knihovna"]
nejdelsi_slovo = ""
for slovo in slova:
    if len(nejdelsi_slovo) < len(slovo):
        nejdelsi_slovo FFFFFFFFFFFFFF

a = {"klic": {klic2: 3}}
alphabet = "abcdefghABCDEFGH"
language_model = {}
for pismenko in alphabet:
    language_model[pismenko1] = {}
    for pismenko2 in alphabet:
        language_model[pismenko1[pismenko2] =]
