'''hits_titles = ["BROTHERS IN ARMS", "BOHEMIAN RHAPSODY", "STAIRWAY TO HEAVEN", "RIDERS ON THE STORM", "WISH YOU WERE HERE"]
hits_titles.append("CHILD IN TIME")
hits_titles.append("AGAIN")
hits_titles.insert(2, "HOTEL CALIFORNIA")
hits_titles.insert(0, "THE SOUND OF SILENCE")
hits_titles.remove("HOTEL CALIFORNIA")
hits_titles[0] = "ENJOY THE SILENCE"
hits_To_Read = hits_titles.copy()
hits_To_Read.reverse()
hits_To_Read.sort()
print(hits_To_Read.pop(0))
print(hits_To_Read.pop(0))
print(hits_To_Read)

new_list = ["NOTHING COMPARES 2 U", "WISH YOU WERE HERE"]

hits_To_Read.extend(new_list)

print(hits_To_Read)

print(hits_To_Read.count("WISH YOU WERE HERE"))

print(hits_To_Read.count("RIDERS ON THE STORM"))

hits_To_Read.clear()

print(hits_To_Read)

#print(hits_titles)'''

fam_drum = ["Donati", "Colaiuta", "Weckl", "Bissonette", "Gadd", "Chambers"]

fam_drum.append("Ślimak")
fam_drum.append("Łosowski")
fam_drum.insert(2, "Lang")
fam_drum.insert(0, "Mr Rich")
fam_drum.remove("Lang")
fam_drum[0] = "Buddy Rich"
print(fam_drum.index("Ślimak"))

print(fam_drum)

drummers = fam_drum.copy()

drummers.reverse()

print(drummers)

drummers.sort()

print(drummers.pop(0))
print(drummers.pop(0))

additional_drummers = ["Beata Polak", "Tomasz Goehs"]
drummers.extend(additional_drummers)

print(drummers)

print(drummers.count("Ślimak"))
print(drummers.count("Chambers"))

drummers.clear()

print(drummers)

