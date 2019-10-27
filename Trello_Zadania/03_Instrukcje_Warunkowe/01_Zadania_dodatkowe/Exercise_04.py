'''
Standardowe limity prędkość wynoszą odpowiednio:

na autostradzie – 140 km/h,
na drodze ekspresowej dwujezdniowej – 120 km/h,
na drodze ekspresowej jednojezdniowej – 100 km/h,
na drodze jednojezdniowej dwukierunkowej – 90 km/h,
w terenie zabudowanym - 50km/h
Poproś użytkownika o podanie dowolnej prędkości,
a następnie wyświetl na jakiej drodze na pewno się nie porusza (zgodnie z prawem).
'''




velocity = int(input("Please enter your speed: "))

if velocity > 50:
    print("Nie jesteś na terenie zabudowanym")
elif velocity > 90:
    print("Nie jestes na drodze jednojezdniowej dwukierunkowej")
elif velocity > 100:
    print("Nie na drodze ekspresowej jednojezdniowej")
elif velocity > 120:
    print("Nie jesteś na na drodze ekspresowej dwujezdniowej")
elif velocity > 140:
    print("Nie jestes na autostradzie")
