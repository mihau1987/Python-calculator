'''Oblicz z pomocą pythona zapotrzebowanie kaloryczne:

a) dla 25-letniej kobiety o wzroście 1.7m i wadze 63kg, która uprawia sport kilka razy w tygodniu.
b) siebie samej / samego.'''

#a):
wiek = 25
wzrost = 170
waga = 63
S = -161

PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + S

print("Zapotrzebowanie kaloryczne wynosi:",PPM * 1.6)

#b):

wiek = 32
wzrost = 185
waga = 78
S = 5

PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + S

print("Zapotrzebowanie kaloryczne wynosi:",PPM * 1.6)



