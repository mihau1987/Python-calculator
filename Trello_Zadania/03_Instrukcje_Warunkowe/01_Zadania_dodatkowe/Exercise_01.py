'''Napisz program, który przyjmuje 2 imiona, a następnie sprawdza czy:

wprowadzone napisy są imionami (hipotetycznie dowolne imię musi składać się jedynie z liter)
popraw imiona jeśli są błędnie napisane np. agNIEszka na Agnieszka
imiona zawierają taką samą liczbę liter
czy oba imiona zaczynają się od tej samej litery
czy oba imiona kończą się na tę samą literę'''

a = input("Podaj imię no 1: ")
b = input("Podaj imię no 2: ")

if a.isalpha() and b.isalpha():
    print("Wprowadzone napisy są imionami")
    a = a.capitalize()
    b = b.capitalize()
    print(a,b)
    if len(a) == len(b):
        print("Imiona zawierają taką samą ilość liter")
    if a[0] == b[0]:
        print("Imiona zaczynają się od tej samej litery")
    if a[-1] == b[-1]:
        print("Imiona kończą się tą sama literą")
else:
    print("Napisy nie są imionami")



    
