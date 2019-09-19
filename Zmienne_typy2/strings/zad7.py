# Zadanie 7
# Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową.
# Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości.



txt = "The end of {0:s} was in year{1: d}"

print(txt.format("WWII", 1945))


# Powyżej - zrobiłem to tak jak pamiętałem z udemy, wiem że to niezgodne z poleceniem


txt = "The end of {0:s} was in year{1: d}"

num = 1945

print(txt.format("WWII", num))

#Oho wpadłem w międzyczasie jeszcze na powyższe rozwiązanie, chyba to jest bardziej zgodne z poleceniem, yes?


