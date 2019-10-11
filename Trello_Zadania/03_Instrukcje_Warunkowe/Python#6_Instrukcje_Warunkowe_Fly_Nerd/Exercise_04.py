# WORK IN PROGRESS

fem_nam = ["Katarzyna", "Natalia", "Monika", "Agnieszka"]

male_nam = ["Jan", "Adrian", "Wojtek", "Eryk"]

name = input("Podaj swoje imię: ")

if name in fem_nam:
    print("This is female name")
elif name in male_nam:
    print("This is male name")
else:
    print("Name is not on the list")
    
