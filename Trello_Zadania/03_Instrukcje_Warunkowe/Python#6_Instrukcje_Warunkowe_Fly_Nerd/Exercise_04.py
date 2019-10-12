# WORK IN PROGRESS

#1. Rozwiązanie za pomocą listy:

'''fem_nam = ["Katarzyna", "Natalia", "Monika", "Agnieszka"]

male_nam = ["Jan", "Adrian", "Wojtek", "Eryk"]

name = input("Podaj swoje imię: ")

if name in fem_nam:
    print("This is female name")
elif name in male_nam:
    print("This is male name")
else:
    print("Name is not on the list")

# Dalej niestety nie wiem'''

#2. Rozwiązanie przy pomocy słownika:

names = {"Kasia": "zenskie", "Ania": "zenskie", "Wiesia": "zenskie",
         "Arnold": "meskie", "Ferdynand": "meskie", "Marian": "meskie"}

name = input("Podaj imię: ")

if (name in list(names.keys())):
    print(name, "to imię", names[name])
else:
    print("Nie mamy tego imienia dodaj je do listy!")
    
    plec = input("To imię meskie czy zenskie? Wpisz m/z: ")
    if (plec == "m"):
        names[name] = "meskie"
    else:
        names[name] = "zenskie"

print(list(names.keys()))






    
