#Sortowanie.
#Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.

#Znajdź największą liczbę??????

#Wyświetl liczby od największej do najmniejszej.

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

lista = [a, b, c]

print(lista)

lista.sort()
lista.reverse()

print("Wyżej wymienione liczby w kolejności od największej do najmniejszej:","\n",lista)
