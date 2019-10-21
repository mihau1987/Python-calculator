min_Likes = 500

min_Shares = 100

num_Likes = 490

num_Shares = 90

if num_Likes >= min_Likes and num_Shares >= min_Shares:
    print("W związku z rosnącym zainteresowaniem w social mediach nasze ceny spadają o 10%")
elif num_Likes < min_Likes:
    print("Zbyt mała ilość lajków aby uruchomić promocje")
else:
    print("W związku z brakiem zainteresowania w social mediach ceny naszych produktów pozostają bez zmian")


if num_Likes >= min_Likes and num_Shares >= min_Shares:
    print("W związku z rosnącym zainteresowaniem w social mediach nasze ceny spadają o 10%")
elif num_Shares < min_Shares:
    print("Zbyt mała ilość udostępnień aby uruchomić promocje")
else:
    print("W związku z brakiem zainteresowania w social mediach ceny naszych produktów pozostają bez zmian")



is_Pizza_Ordered = True

is_Big_Drink_Ordered = True

is_Weekend = False

if (is_Pizza_Ordered or is_Big_Drink_Ordered) and not is_Weekend:
    print("Brawo, otrzymujesz kupon na darmowego burgera")
elif is_Weekend:
    print("Promocja obowiązuje jedynie w dni poza weekendowe")
else:
    print("Zachęcamy do dalszych zakupów")
