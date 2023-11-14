name = input("Type your name: ")
print("Welcom", name, "to this adventure.")

answer = input(
    "Choose your path, each path have different adventure."
).lower()

if answer == "left":
    answer = input("YOU GOING TO A CITY OF MANILA.")

    if answer == "Walk":
        print("You walk a month to arrive in Manila....")
    elif answer == "Run":
        print("You run a week to arrive in Manila....")
    else:
        print("Choose only this two option....")

elif answer == "right":
    answer = input("YOU GOING TO A CITY OF QUEZON CITY.")

    if answer == "Back":
        print("You back because you feel is dangerous....")
    elif answer == "Go":
        answer = input("You go to adventure in Quezon City. Find some people do you want to talk to them? ....")

        if answer == "Yes":
            print("You find people that you become your friend.")
        elif answer == "No":
            print("You passing to them and go to your adventure.")
        else:
            print("Choose only this two option.")
    else:
        print("Choose only this to option....")
 
else:
    print("You stay in your house and dont go to a adventure.")

print("ADVENTURE YOU LIFE", name)