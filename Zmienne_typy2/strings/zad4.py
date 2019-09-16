# Zadanie 4
# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# Połącz dane w jeden ciąg book za pomocą spacji
# Policz liczbę wszystkich znaków w napisie book

title = input("Title of your favourite book: ")
author = input("Name of author: ")
num_page = int(input("How many pages? "))
print("Title of book is:",type(title))
print("The name of author is:",type(author))
print("Number of pages is type:",type(num_page))
print("Your favourite book is:",title.title())
print("The name of author is:",author.title())
print("The number of pages in this book:",num_page)

book = title + " " + author + " " + str(num_page)

print(book)

print(len(book))
