#beczka piwa = 30 l
#kufel = 0.5 l

beczka = 30
kufel = 0.5
cena_piwa = 11
cena_studencka = 5

standard_prize = beczka/kufel * cena_piwa

barmans_prize = (beczka/kufel * cena_studencka) + 10 * cena_piwa

print(standard_prize)
print(barmans_prize)

if standard_prize < barmans_prize:
    print("Barman zarobił więcej")
else:
    print("Barman zarobił mniej")
