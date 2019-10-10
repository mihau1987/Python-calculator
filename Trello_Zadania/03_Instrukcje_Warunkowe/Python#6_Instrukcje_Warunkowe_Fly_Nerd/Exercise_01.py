#Zadanie 1
#Skrypt zapyta użytkownika o wiek. Jeżeli użytkownik jest przed 18 wyświetli informację „Użytkownik niepełnoletni” oraz zwróci ile lat zostało użytkownikowi do pełnoletności.
#Użytkownikom pełnoletnim wyświetli informację „Użytkownik pełnoletni”.
#Sprawdź czy wiek użytkownika nie przekracza 100 lat i wyświetl komunikat „200 lat ♫”.


age = int(input("Podaj swój wiek: "))

if age > 18 and age < 100:
    print("Użytkownik pełnoletni")
elif age < 18:
    print("Użytkownik niepełnoletni, do pełnoletności zostało Ci:", 18 - age)
elif age > 100 and age <= 200:
    print("200 lat .|-.|")
else:
    print("Wolne żarty ;)")
