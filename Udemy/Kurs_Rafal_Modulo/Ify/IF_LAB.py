muscle_Pain = False
fever = True
weakness = True

if fever and weakness and muscle_Pain:
    print("suspition of influenza")
else:
    print("The flu is unlikely")


muscle_Pain = False
fever = True
weakness = True

if muscle_Pain and fever and weakness:
    print("suspition of influenza")
elif not(muscle_Pain and fever) and weakness:
    print("Just take a rest!")
else:
    print("You may be cold")
