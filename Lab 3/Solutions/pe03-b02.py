num = int(input('Enter positive integer number from 1 to 100 = '))

if num < 1 or num > 100:

    print('Invalid integer number!')

else:
    
    is_perfect_square = False    
    i = 1
    
    while i <= 10:
        
        square = i * i
    
        if num == square:
            
            is_perfect_square = True
            break;
    
        i += 1
    
    if is_perfect_square:
        
        print('{} is a perfect square'.format(num))
        
    else:
        
        print('{} is NOT a perfect square'.format(num))
