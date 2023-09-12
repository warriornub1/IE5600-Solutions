num = int(input('Enter positive integer number = '))

if num > 0:
    
    first_digit = num
    
    while first_digit > 9:
        
        first_digit //= 10
    
    print('First digit of {} is {}'.format(num, first_digit))
    
else:
    
    print('Invalid positive integer number!')
