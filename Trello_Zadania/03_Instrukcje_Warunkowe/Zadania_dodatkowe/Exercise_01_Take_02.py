name_1 = input("Enter name no 1: ")

name_2 = input("Enter name no 2: ")

if name_1.isalpha() and name_2.isalpha():
    print("These strings are names")
    name_1 = name_1.capitalize()
    name_2 = name_2.capitalize()
    print(name_1, name_2)
    if len(name_1) == len(name_2):
        print("Length of names is the same")
    if name_1[0] == name_2[0]:
        print("The same first letter in both names")
    if name_1[-1] == name_2[-1]:
        print("The same last letter in both names")
            
else:
    print("These strings arent names")
