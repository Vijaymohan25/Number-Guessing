import random
name=input("Enter Your name : ")

user_input_range=int(input("Enter any number for range : "))

if user_input_range <=0:
    print("You should enter value which is should be above than 0, Try next time")
    quit()

random_number=random.randint(0,user_input_range)
guess=0

while True:
    user_input = int(input("Make a guess : "))
    guess+=1
    if user_input == random_number:
        print("Hooray !, You got it")
        break
    elif user_input < random_number:
        print("You're below")
    else:
        print("You're above")
print("\n* Congratulation * You won the game",name)