age = int(input("Podaj swój wiek: "))

if age > 18 and age < 100:
    print("Użytkownik pełnoletni")
elif age < 18:
    print("Użytkownik niepełnoletni")
elif age > 100:
    print("200 lat .|-.|")
