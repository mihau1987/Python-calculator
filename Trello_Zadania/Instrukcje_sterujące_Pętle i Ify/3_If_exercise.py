#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
#Oblicz średnią opinię o książce.
#W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
#ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

print("Ocena Trylogii Lord of The Rings w skali 1 - 10")

a = int(input("Opinia No 1: "))


b = int(input("Opinia No 2: "))


c = int(input("Ocena No 3: "))

srednia_ocen = (a + b + c)/3

print("Średnia ocen wynosi: ",srednia_ocen)

if srednia_ocen >= 8:
    print("Bardzo dobra pozycja!")
elif srednia_ocen > 5 and srednia_ocen < 7:
    print("Przeciętna lektura")
elif srednia_ocen <= 4:
    print("Nie warta uwagi")

