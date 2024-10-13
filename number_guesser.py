### 9 HOURS of Python Projects - From Beginner to Advanced 
### YouTube Video (pick up from minute 32:00), 
### Saturday Night, 10:45 PM (10/12/2024)


import random 

# random.randrange(11) - will do 0 through 11 (not including 11)
 
top_of_range = int(input("type a number: "))

if top_of_range.isdigit():
    top_of_range = int(top_of_range)   

    if top_of_range <= 0:
        print("please type a number greater than 0 next time") 
        quit()
else: 
    print ("please type a number next time")
    quit() 

random_number = random.randint(0,top_of_range)
print(random_number)

while True: 
    user_guess = input("make a guess: ")
    if user_guess.isdigit(): 
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue 

    if user_guess == random_number:
        print("you got it! ")
    else: 
        print("")




