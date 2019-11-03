szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.3f | %16s | %10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)


szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

szer = 80
print("-"*szer)

waluta = "dolar"
us = 1
pln = 4.08
print("Aktualnie %d %s kosztuje %.2f zł" %(us, waluta, pln))
print("Aktualnie %r %r kosztuje %r zł" %(us, waluta, pln))

print("Aktualnie {:d} {:s} kosztuje {:.2f} zł".format(us, waluta, pln))

print("{} ma {}".format("Ala", "Kota"))
print("{1} ma {0}".format("Ala", "Kota"))

print("Moja %s o wadze %dg ma ok. %d kcal i %.1f węglowodanów"
      % ("czekolada", 100, 545, 58.5))
print("Moja {} o wadze {}g ma ok. {} kcal i {:.1f} weglowodanow".format("czekolada", 100, 545, 58.5))
