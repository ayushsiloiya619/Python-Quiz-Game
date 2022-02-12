print("Welcome the Quiz!")
user_react = input("Do you want to play? ")
if user_react.lower() != "yes":
    quit()
print("Ok let's play :) ")
score = 0

ans = input("What is the full form of CPU? ")
if ans.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong attempt! ")

ans = input("Full form of RAM? ")
if ans.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong attempt! ")

ans = input("Full form of ROM? ")
if ans.lower() == "reads only memory":
    print("Correct!")
    score += 1
else:
    print("Wrong attempt! ")

ans = input("Full form of GPU? ")
if ans.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong attempt! ")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4)*100) + "%. ")
