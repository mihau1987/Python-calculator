'''Tekst 1 strony A4 to 2500 znaków, i około 300 słów.
Praca dyplomowa powinna zajmować conajmniej 25 str A4.
Użytkownik programu podaje jakiego przelicznika użyje - znaki czy słowa.
Następnie program pyta:
"ile
{znaków/slow} pracy dyplomowej do tej pory napisałeś?". Użytkownik odpowiada.

Dla liczby mniejszej niż 20 stron komputer wyświetla 'tak mało? masz jeszcze {liczba stron} do napisania.
*Dla liczby 20-25 powinni pojawić hasło dopingujace
Dla liczby powyżej 25 - gratulacje ;D'''

znaki = 2500

slowa = 300

param = input("Jakiego przelicznika użyjesz znaki/slowa: ")

liczba_stron = int(input("Ile znakow/slow pracy dyplomowej do tej pory napisałeś? "))

if param == "znaki":
    liczba_stron_a4 = liczba_stron/znaki
    print("")
    
