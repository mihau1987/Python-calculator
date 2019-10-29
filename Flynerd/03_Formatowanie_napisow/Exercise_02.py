start = float(input("Stan początkowy konta wynosi: "))

RRSO = float(input("Stopa oprocenotowania w skali roku: "))

lata = int(input("Liczba lat na lokacie: "))

koniec = start*(1 + RRSO*lata)

print("Po {} latach kapitał będzie wynosił {} zł".format(lata, koniec))
