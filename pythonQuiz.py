print("Welcome to Quiz")

playing = input("Do you want to play? ")

if playing.lower() == "yes":
    print("Lets Play")
elif playing == "no":
    print("Lets play on the other day")

score = 0

answer = input("What is the name of our planet? ")
if answer == "Earth":
    print('Correct')
    score += 1 
else:
    print('Incorrect')

answer = input("What is the name of the fourt planet? ")
if answer == "Mars":
    print('Correct')
    score += 1 
else:
    print('Incorrect')

print("You got " + str(score) + "qustion correct")
print("You got " + str((score / 2) * 100) + "% question percentage correct")


    

    
    