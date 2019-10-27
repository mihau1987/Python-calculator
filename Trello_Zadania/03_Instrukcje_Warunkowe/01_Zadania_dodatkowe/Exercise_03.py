'''
Poprosić użytkownika o podanie zakresu temperatur, które wg niego są optymalne do uprawiania sportów outdoorowych.
Użytkownik powinen bodac 2 wartość w jednej lini jako zakres oddzielony przecinkiem np. 16, 23.
Następnie poproś o podanie aktualnej temperatury na dworze.
Sprawdź czy można uprawiać sport na dworze i wyświetl komunikat:
temperatura idealna do uprawiania sportów outdoorowych / pogoda nie sprzyja....'''


temperature_level = input("Enter range of temperature perfect for outdoor sports: ")

temperature_level = temperature_level.split(",")

print(temperature_level)

current_temperature = int(input("Enter current temperature value: "))

if current_temperature > int(temperature_level[0]) and current_temperature < int(temperature_level[1]):
    print("Temperature is perfect for outdoor sports")
#Rozszerz zadanie 2. Przyjmij margines 10% temperatury optymalnej. Wyświetl komunikat - temperatura nieidealna, ale poprawna do uprawiania sportów zimowych.
elif current_temperature > int(temperature_level[0])- int(temperature_level[0])*0.1 and current_temperature < int(temperature_level[1])*1.1:
    print("Good enough")
else:
    print("The weather is not quite good")


Margines 10%:

10 - 20

9 - 22

10 - 10*0.1
