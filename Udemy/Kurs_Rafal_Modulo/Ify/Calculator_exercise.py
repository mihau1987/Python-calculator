choice = input("* - multiplication, / - division, + - adding, - - subtrackt, ** - exponentiation: ")
a = int(input("First: "))
b = int(input("Second: "))

if (choice == "*"):
    print(a*b)
elif (choice == "/"):
    if (b == 0):
        print("Dont you dare!")
    else:
        print(a/b)
elif (choice == "+"):
    print(a+b)
elif (choice == "-"):
    print(a-b)
elif (choice == "**"):
    print(a**b)
else:
    print("Wrong choice!")

