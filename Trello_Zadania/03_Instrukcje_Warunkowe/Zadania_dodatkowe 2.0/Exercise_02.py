'''
Podaj górną i dolną granicę częstotliwości słuchu ludzkiego (16Hz do 20kHz).
Sprawdź dźwięki takie jak:

szczekanie psa - 500Hz
silnik samochodu - 300Hz
bolid - 4Hz
mowa - 1000Hz
skrzek nietoperza - 80 000Hz
Wyświetl komunikat czy dźwięk jest słyszalny.
'''
print("Zakres częstotliwości sluchu czlowieka wynosi 16 - 20000Hz")

dolna_granica = 16
gorna_granica = 20000


#Podejście no 1:
'''
szczekanie_psa = 500
silnik_samochodu = 300
skrzek_nietoperza = 80000

if szczekanie_psa < gorna_granica and szczekanie_psa > dolna_granica:
    print("Dzwiek szczekania psa jest slyszalny dla czlowieka")
if silnik_samochodu < gorna_granica and silnik_samochodu > dolna_granica:
    print("Dzwiek silnika samochodowego jest slyszalny dla czlowieka")
if skrzek_nietoperza < gorna_granica and skrzek_nietoperza > dolna_granica:
    print("Dzwiek jest slyszalny dla ucha ludzkiego")
else:
    print("Dzwiek nie jest slyszalny dla czlowieka")
'''


#Podejście no 2:
dzwiek = int(input("Podaj wysokosc dzwieku w Hz: "))

if dzwiek < gorna_granica and dzwiek > dolna_granica:
    print("Podany dzwiek jest slyszalny dla czlowieka")
else:
    print("Podany dzwiek nie jest słyszalny dla czlowieka")



            
    


