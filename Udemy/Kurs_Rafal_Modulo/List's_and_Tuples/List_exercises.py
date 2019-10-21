#1. Utwórz listę hitsTitles zawierającą tytuły: 'BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE'
#2. Dodaj do listy kolejne dwie piosenki: 'CHILD IN TIME' i 'AGAIN'
#3. Wygląda na to, że w systemie głosowania była luka. Na pozycji 3 powinna się znaleźć piosenka 'HOTEL CALIFORNIA'
#4. Ops... wygląda na to, że system był bardziej zepsuty... oczywiście to wina IT. Piosenka 'THE SOUND OF SILENCE' powinna znaleźć się na pierwszym miejscu
#5. To na jakiej pozycji jest teraz 'HOTEL CALIFORNIA'? Odnajdź numer indeksu dla tej piosenki
#6. A jednak 'HOTEL CALIFORNIA' powinien zostać usunięty z listy
#7. No i na pierwszym miejscu tytuł "THE SOUND OF SILENCE" powinien zostać zamieniony na "ENJOY THE SILENCE"
#8. Utwórz kopię listy, która będzie służyła do odczytania przebojów na antenie. Nowa lista ma nazywać się hitsToRead
#9. Lista do odczytania ma zawierać elementy w odwrotnej kolejności. Odwróć kolejność elementów na liście hitsToRead.
#10. A jednak dzisiaj lista przebojów będzie  wyjątkowo prezentowana w kolejności alfabetycznej. Posortuj hitsToRead w kolejności alfabetycznej
#11. Prowadzący listę przebojów po odczytaniu tytułu usuwa z listy hitsToRead usuwa odczytany element. Dlatego korzysta z metody pop :). Zasymuluj odczyt dwóch pierwszych pozycji
#12. W czasie audycji słuchacze domagali się aby zagrać dodatkowo 'NOTHING COMPARES 2 U' i 'WISH YOU WERE HERE'. Utwórz listę additionalSongs zawierającą te dwa tytuły.
#13. Dodaj do listy hitsToRead elementy z listy additionalSongs
#14. Ile razy będzie zagrane 'WISH YOU WERE HERE' a ile razy 'RIDERS ON THE STORM'. Wyświetl ile razy te piosenki występują na liście hitsToRead.
#15. Audycja się kończy. Wyczyść listę hitsToRead

'''hits_titles = ["BROTHERS IN ARMS", "BOHEMIAN RHAPSODY", "STAIRWAY TO HEAVEN", "RIDERS ON THE STORM", "WISH YOU WERE HERE"]
hits_titles.append("CHILD IN TIME")
hits_titles.append("AGAIN")
hits_titles.insert(2, "HOTEL CALIFORNIA")
hits_titles.insert(0, "THE SOUND OF SILENCE")
hits_titles.remove("HOTEL CALIFORNIA")
hits_titles[0] = "ENJOY THE SILENCE"
hits_To_Read = hits_titles.copy()
hits_To_Read.reverse()
hits_To_Read.sort()
print(hits_To_Read.pop(0))
print(hits_To_Read.pop(0))
print(hits_To_Read)

new_list = ["NOTHING COMPARES 2 U", "WISH YOU WERE HERE"]

hits_To_Read.extend(new_list)

print(hits_To_Read)

print(hits_To_Read.count("WISH YOU WERE HERE"))

print(hits_To_Read.count("RIDERS ON THE STORM"))

hits_To_Read.clear()

print(hits_To_Read)

#print(hits_titles)'''

#The same thing but with drummers

fam_drum = ["Donati", "Colaiuta", "Weckl", "Bissonette", "Gadd", "Chambers"]

fam_drum.append("Ślimak")
fam_drum.append("Łosowski")
fam_drum.insert(2, "Lang")
fam_drum.insert(0, "Mr Rich")
fam_drum.remove("Lang")
fam_drum[0] = "Buddy Rich"
print(fam_drum.index("Ślimak"))

print(fam_drum)

drummers = fam_drum.copy()

drummers.reverse()

print(drummers)

drummers.sort()

print(drummers.pop(0))
print(drummers.pop(0))

additional_drummers = ["Beata Polak", "Tomasz Goehs"]
drummers.extend(additional_drummers)

print(drummers)

print(drummers.count("Ślimak"))
print(drummers.count("Chambers"))

drummers.clear()

print(drummers)

