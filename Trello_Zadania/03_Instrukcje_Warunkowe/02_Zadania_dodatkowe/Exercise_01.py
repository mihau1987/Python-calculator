'''
Napisz program, który zawiera listę zwierząt.
Poproś użytkownika o 3 zwierzęta, a następnie sprawdz czy:

- wprowadzone napisy są zwierzętami z listy
- zawierają taką samą liczbę liter
- czy zawierają taka samą liczbę liter A
- czy kończą się na tę samą literę
'''

#1. Tworzę listę zwierząt

#2. Tworzę input z zapytaniem 

#3. Tworzę warunek który sprawdza czy napisy są zwierzętami z listy

animals = ["cat", "dog", "aligator", "anaconda", "albatros", "lemur", "amur"]

ani_1 = input("Enter animal no 1 name: ")
ani_2 = input("Enter animal no 2 name: ")
ani_3 = input("Enter animal no 3 name: ")

if ani_1 and ani_2 and ani_3 in animals:
    print("Animals are in the list")
    if len(ani_1) == len(ani_2) == len(ani_3):
        print("Lenght is the same")
    if ani_1.count("a") and ani_2.count("a") and ani_3.count("a"):
        print("They all have letter A")
    if ani_1[-1] == ani_2[-1] == ani_3[-1]:
        print("They all end's with the same letter")
else:
    print("These animals are not on the list")
    


#Coś mi się wydaje że skopałem temat inputów, może powinny być oddzielone przecinkiem, czyli metoda split się kłania?



