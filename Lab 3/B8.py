import random


cont = choice = True

while(cont):
    count = 0
    age = random.randint(0, 100)
    while(1):
        guess_age = int(input("Enter your guess of the computer age = "))
        if guess_age < age:
            print("Your guess is too small!")
        elif guess_age > age:
            print("Your guess is too big!")
        else:
            print("Congratulations! You have guessed the computer age correctly")
            count += 1
            break
        count += 1
    print(f"You took {count} attempt(s)")
    
    choice = True
    while(choice):
        c = str(input("Do you want to continue with the game (Y: Yes, N: No = )")).upper()
        if c not in ("Y" or "N"):
            print("Wrong char, Try again !")
            
        elif c == 'Y':
            print("Ok restarting loop")
            choice = False
        else:
            print("Breaking out of loop...")
            choice = False
            cont = False