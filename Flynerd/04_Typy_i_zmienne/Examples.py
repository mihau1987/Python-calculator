#Pozbywanie sie automatycznego znaku nowej linii:

print("czeko", end='')
print("lada\n", end='')

print("czeko", end=' ')
print("lada\n", end='')

#Surowy napis (r):

txt = r"Nowe linie zapisujemy jako \n a tabulatory jako \t"
print(txt)

'''Python collections - ang ARRAYS:

There are four collection data types in the Python programming language:

LIST is a collection which is ordered and changeable. Allows duplicate members.
TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.
SET (ZBIÓR) is a collection which is unordered and unindexed. No duplicate members.
DICTIONARY is a collection which is unordered, changeable and indexed. No duplicate members.


When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning,
and, it could mean an increase in efficiency or security.



