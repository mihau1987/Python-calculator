age = int(input("Podaj swój wiek: "))

if age > 18 and age < 100:
    print("Użytkownik pełnoletni")
elif age < 18:
    print("Użytkownik niepełnoletni, do pełnoletności zostało Ci:", 18 - age)
elif age > 100:
    print("200 lat .|-.|")
