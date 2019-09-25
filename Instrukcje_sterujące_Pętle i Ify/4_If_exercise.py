#Utwórz zmienną przechowującą dowolny ciąg znaków.
#Sprawdź czy string jest dłuższy od 5 oraz czy zawiera literę a.
#Jeśli zawiera, wszystkie litery a podmień na z


a_Line = "Palin and Cleese"

print(len(a_Line))

print(a_Line.find("a"))


if a_Line.find("a"):
    print(a_Line.replace("a", "z"))

