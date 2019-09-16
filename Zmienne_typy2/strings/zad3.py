# Do zmiennej quote przypisz zdanie:
# „Honesty is the first chapter in the book of wisdom.”, a następnie:
#
# Policz wszystkie znaki w napisie
# Nie modyfikując zmiennej wyświetl słowo wisdom
# Wyświetl tylko pierwszą połowę tekstu
# Wyświetl tylko kropkę
# Wyświetl od połowy tylko co trzecią literę cytatu
# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
# Wyświetl cały cytat odwrotnie
# Zamień wisdom na słowo friendship

quote = "Honesty is the first chapter in the book of wisdom."

print(len(quote))

print(quote[-7:])

print(quote[:26])

print(quote[quote.find(".")])

print(quote[25:51:3])

print(quote[0:51:2])

print(quote[::-1])

print(quote.replace("wisdom", "friendship"))
