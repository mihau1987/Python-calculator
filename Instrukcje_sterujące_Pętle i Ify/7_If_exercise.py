a = float(input("Podaj wzrost: "))
b = float(input("Podaj wagę: "))

BMI = b / (a ** 2)

print("BMI = ",BMI)

if BMI > 14 and BMI < 18:
    print("Niedowaga")
elif BMI > 18.5 and BMI < 24.99:
    print("Waga prawidłowa")
elif BMI > 25 and BMI < 29.99:
    print("Nadwaga")
elif BMI > 30 and BMI < 40:
    print("Otyłość")
else:
    print("Udaj się niezwłocznie do lekarza!")


