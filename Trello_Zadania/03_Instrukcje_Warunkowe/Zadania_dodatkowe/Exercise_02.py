import sys

a4_znakow = 2500

a4_slow = 300

parametr = input("Podaj przelicznik którego uzyjesz znaki/słowa?: ")

liczba = int(input("Ile znaków/słów pracy dyplomowej do tej pory napisałeś? "))


if parametr == "znaki":
    #Oblicz liczbę stron ze znaków
    liczba_stron_a4 = liczba/a4_znakow
    print("")
    
elif parametr == "słowa":
    #Oblicz liczbę stron ze słów
    liczba_stron_a4 = liczba/a4_slow
    print("")
else:
    print("Nie ma takiego przelicznika")
    #Zakończ program
    sys.exit(0)
    
if liczba_stron_a4 < 20:
    print("Tak mało? Masz jeszcze", 25 - liczba_stron_a4)
elif liczba_stron_a4 > 25:
    print("Gratulacje")
else:
    print("Zapierdzielaj szybciej bo czas ucieka!")


# Jutro raz jeszcze! Samemu plus trello z ifów
    

