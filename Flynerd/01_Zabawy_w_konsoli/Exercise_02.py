'''Oblicz z pomocą pythona zapotrzebowanie kaloryczne:

a) dla 25-letniej kobiety o wzroście 1.7m i wadze 63kg, która uprawia sport kilka razy w tygodniu.
b) siebie samej / samego.'''

#a):

wiek = 25
wzrost = 170
waga = 63
S =  -161

PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + S

print("Twoje PPM wynosi:",PPM,"kcal")

print("Twoje PPM z uwzględnieniem aktywności wynosi:",PPM*1.4,"kcal")

#b):

wiek_2 = 32
wzrost_2 = 185
waga_2 = 79
S_2 = 5

PPM = 10 * waga_2 + 6.25 * wzrost_2 - 5 * wiek_2 + S_2

print("Twoje PPM wynosi:",PPM,"kcal")

print("Twoje PPM z uwzględnieniem aktywności wynosi:",PPM*1.6,"kcal")



