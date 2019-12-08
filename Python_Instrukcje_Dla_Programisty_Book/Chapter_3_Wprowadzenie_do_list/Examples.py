#Uzyskanie dostępu do elementów listy

bicycles = ["trekingowy", "gorski", "miejski", "szosowy"]
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

#Użycie poszczególnych wartości listy

message = "Moim pierwszym rowerem był rower " + bicycles[1].title() + "."

print(message)

#Zmienianie dodawanie i usuwanie elemenów

motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles)

motorcycles[0] = "ducati" #Zmiana elementu listy

print(motorcycles)

motorcycles.append("harley davidson") #Umieszczanie elementu na końcu listy, metoda APPEND

print(motorcycles)

motorcycles_2 = []

print(motorcycles_2)

motorcycles_2.append("honda")
motorcycles_2.append("yamaha")
motorcycles_2.append("suzuki")

print(motorcycles_2)

motorcycles_2.insert(0, "Ducati") #Wstawianie elementu w dowolnie wybrane miejsce, metoda INSERT
print(motorcycles_2)
motorcycles_2.insert(2, "harley davidson")
print(motorcycles_2)

print(motorcycles_2)

del motorcycles_2[0] #Usuwanie elementu za pomocą polecenia del, na podstawie położenia
print(motorcycles_2)
del motorcycles_2[1]
print(motorcycles_2)

del motorcycles_2[1]
print(motorcycles_2)




