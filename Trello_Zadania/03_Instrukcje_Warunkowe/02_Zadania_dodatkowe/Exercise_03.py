'''
Napisz konwerter walut.
Użytkownik podaje jedną z walut kod literowy np USD, EUR, HUF, a następnie kwotę do wymiany.
Podstawowa waluta to PLN. Wyświetl liczby zaokrąglone do 2 miejsc po przecinku.
Konwerter powinien działać w 2 strony.

Kiedy wymienisz 500 USD na PLN ile banknotów dostaniesz.
Zakładamy, że chcesz jak najwięcej banknotów z każdego nominału od (100, z reszty liczysz 50 itd, 20, 10)
'''


currency = input("Which currency you like to convert the money into?: ")

amount_PLN = float(input("Enter the amount of money you wish to convert: "))

option = int(input("Enter: \n 1- from PLN\n 2- to PLN:\n"))

EUR = 4.27

USD = 3.86

HUF = 0.01


if currency == "EUR":
        if option == 1:
            print(round(amount_PLN/EUR,2))
        if option == 2:
            print(round(amount_PLN*EUR,2))
elif currency == "USD":
    print(round(amount_PLN * USD,2))
    print(round(amount_PLN/USD,2))
elif currency == "HUF":
    print(round(amount_PLN * HUF,2))
    print(round(amount_PLN/HUF,2))








