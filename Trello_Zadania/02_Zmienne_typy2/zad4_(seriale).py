serials = {"Breaking Bad": "10", "Game Of Thrones": "9", "Better Call Saul": "8", "Blackadder": "10"}

print(list(serials.keys())) # Dlaczego taki zapis a nie po prostu - print(serials)

name = input("Jaki serial chcesz obejrzeć? ")

print("Serial {} otrzymał ocenę {}".format(name, serials[name])) # Wyjaśnienie całej tej linii - skąd format itd

new = input("Jaki serial chcesz dodać do bazy? ")

rating = input("Jaką ocenę otrzymał " + new + "? ")

serials[new] = float(rating) #Dlaczego float? Bez float równiez zadziałalo

print(list(serials.keys()))


