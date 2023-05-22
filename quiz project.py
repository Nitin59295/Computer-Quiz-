print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print ("Okay! let's play then :) ")
score = 0

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Is window's an operating system? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is SSD? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the brain of a computer system? ")
if answer.lower() == "cpu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does GUI stands for? ")
if answer.lower() == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("YAY! quiz finished and you got " + str(score) + " Questions correct! " )
print("YAY! quiz finished and you got " + str((score / 6) * 100) + "%." )

