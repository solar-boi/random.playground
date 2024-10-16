print("welcome to my computer quiz!")

#there is an error in this code below because after inputting yes, YES, or no the program ends
playing = input.lower("Do you want to play? ")
if playing.lower != "YES" : 
    quit()

print("Okay! Let's play" )
score = 0 

# question number one 
# note the two differnt ways of lowering the characters to accomodate for YeS YES yes scenarios 
answer = input("what does CPU stand for? ").lower
if answer.lower == "central processing unit ": 
    print('correct!')
    # another way of writing the below would have been score = 0 + 1"
    score += 1 
else: 
    print("Incorrect!")

# question number two 
answer = input("what does GPU stand for? ").lower
if answer == "graphics processing unit ": 
    print('correct!')
    score += 1 

else: 
    print("Incorrect!")

# question number three
answer = input("what does RAM stand for? ").lower
if answer == "random access memory ": 
    print('correct!')
    score += 1 

else: 
    print("Incorrect!")

# question number four 
answer = input("what does PSU stand for? ").lower
if answer == "power supply unit ": 
    print('correct!')
    score += 1 

else: 
    print("Incorrect!")

print ("you got " + str(score) + " questions correct!")
# print ("you got " + str((score / 4) * 100 + "%.") + " questions correct!")

