# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy ( jest to prawdopodobne?)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

a = int(input("Podaj wysokość windy: "))
b = int(input("Podaj szerokość windy: "))
c = int(input("Podaj głębokość windy: "))

a1 = int(input("Podaj wysokość lodówki: "))
b1 = int(input("Podaj szerokość lodówki: "))
c1 = int(input("Podaj głębokość lodówki: "))

print("Miejsce pozostałe w windzie po wstawieniu do niej lodówki to:",(a+b+c) - (a1+b1+c1), "cm")
