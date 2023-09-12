import random

# The following initialisation essentially make this while loop a do...while loop since the game must be payed at least one time.
continue_game = True

while continue_game:

    random_num = random.randrange(100) + 1
    attempt = 0
    guess = 0
    
    while guess != random_num:
    
        guess = int(input('Enter your guess of the computer''s age = '))
        
        if guess < random_num:
        
            print('Your guess is too small!')
            
        elif guess > random_num:
        
            print('Your guess is too big!')
        
        attempt += 1
        
    print('Congratulations! You have guessed the computer''s age correctly')
    print('You took {} attempt(s)'.format(attempt))
    prompt = input('Do you want to continue with the game (Y: Yes, N: No) = ').upper()
    
    if prompt == 'N':
    
        continue_game = False

print('Goodbye!')
