'''
Tutaj każdą literkę wyodrębnisz i wykorzystasz oddzielnie.
Do zmiennej q zapisz tekst "THE EYES".
Wyświetl napis zbudowany z liter zmiennej q w kolejności: 0,1,2,5,3,7,4,6.
Wyświetlając literki skorzystaj z print lub dodaj do siebie literki budując napis.'''


q  = "THE EYES"
print(q)
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])


'''
Tutaj użyjesz notacji, która pozwoli wyodrębnić fragment napisu rozpoczynając od określonej pozycji do końca.
Do zmiennej q zapisz  "a gentleman" a potem wyświetl litery w kolejności 3,6,7,2,0,4,5,1,8 - do końca'''


q = "a gentleman"
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:12])


'''
Wiesz jak z napisu  "THE MORSE CODE" zrobić tekst "HERE COME DOTS"? Gdzie się da korzystaj z notacji "od-do"'''


p = "THE MORSE CODE"


print(p[1:3]+p[6]+p[8],p[10:12]+p[4]+p[2],p[12]+p[11]+p[0]+p[7])


'''
Zostajesz zatrudniony w firmie, która wykonuje analizę oglądalności poszczególnych programów TV.
Na bardzo początkowym etapie, Twój program musi przeczytać dane z pliku tekstowego z zapisanym harmonogramem poszczególnych programów.
Plik zawiera linie zbudowane tak, że tytuł programu znajduje się w cudzysłowie,
a kończy się napisem o:, po którym następuje godzina, np tak:'''



line = "Program 'Kropka nad i' nadamy o:22"

time = line[line.find(":")+1:]

print(time)

tmp = line[line.find("'")+1:]

title = tmp[:tmp.find("'")]

print(title, time)


#To samo wykonaj dla linii: 'Program "Pytanie na śniadanie" nadamy o: 6:00'

line = "'Pytanie na śniadanie' nadamy o: 6:00"

time = line[line.find(":") + 2:]

print(time)

tmp = line[line.find("'")+1:]

print(tmp)

title = tmp[:tmp.find("'")]

print(title, time)

