#Zapisz kalkulator BMI, który wcześniej był w konsoli do pliku,
#tak aby pytał użytkownika o potrzebne do obliczeń dane.

'''wzrost = float(input("Podaj swój wzrost: "))

waga = float(input("Podaj swoją wagę: "))

BMI = waga/wzrost ** 2

print("Twoje BMI wynosi:", BMI)'''

wzrost_2 = int(input("Podaj swój wzrost w cm: "))

waga_2 = int(input("Podaj swoja wage: "))

wiek = int(input("Podaj swoj wiek: "))

S = int(input("Podaj wspolczynnik zalezny od plci k -161 m +5: "))

PPM = 10 * waga_2 + 6.25 * wzrost_2 - 5 * wiek + S

print("Twoje PPM wynosi:", PPM)

print("Twoje PPM przy umiarkowanej aktywności wynosi:", PPM * 1.6)


