# Zadanie 2
# Zmodyfikuj skrypt zad1.py tak, by przyjmował wartości od użytkownika


spalanie_100 = float(input("Podaj ilość litrów spalanych na godzinę: "))

trasa = float(input("Podaj ilość km do przejechania: "))

cena_benz = float(input("Podaj cenę benzyny: "))

print("Przy trasie 120 km spalanie wynosi:",(trasa * spalanie_100)/100)

print("Całkowity koszt wyprawy to:",(trasa * spalanie_100)/100 * 5.04) 

