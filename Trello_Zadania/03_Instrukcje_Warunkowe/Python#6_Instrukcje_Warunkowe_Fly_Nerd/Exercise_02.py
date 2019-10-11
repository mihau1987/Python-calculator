wzrost = float(input("Podaj swoj wzrost: "))

waga = float(input("Podaj swoją wagę: "))

BMI = waga/(wzrost**2)

print("Twoje BMI wynosi:", BMI)


if BMI <= 18.5:
    print("Niedowaga")
elif BMI > 18.5 and BMI < 24:
    print("Waga normalna")
elif BMI > 24 and BMI < 26.5:
    print("Lekka nadwaga")
elif BMI > 26.5 and BMI < 30:
    print("Nadwaga")
else:
    print("Udaj się niezwłocznie do lekarza!")
