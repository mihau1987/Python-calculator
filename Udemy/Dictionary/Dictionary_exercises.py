'''1. Utwórz obiekt dictionary o nazwie channels z następującymi kluczami i wartościami:
-Google - 1480
-Email - 300
-Natural Traffic - 440
-TV Spot - 700
2. Wyświetl wartość skojarzoną z kluczem "Email"
3. Utwórz nowy słownik chanelsUpdate z kluczami i wartościami:
-Natural Traffic -  520
-News - 600
4.Zaktualizuj słownik chanels wartościami z chanelsUpdate
5. Wyświetl wszystkie klucze z chanels
6. Usuń wartość 'Email' ze słownika'''

channels = {"Google": "1480","Email": "300","Natural Traffic": "440","TV Spot": "700"}

print(channels["Email"])

channels_Update = {"Natural Traffic": "520","News": "600"}

channels.update(channels_Update)

print(channels)

print(channels.keys())

channels.pop("Email")

print(channels)
