num = int(input('Enter a positive integer = '))

if num > 0:
    
    while num != 1:
        
        print(num, end=', ')
        
        if num % 2 == 0:
            
            num //= 2
            
        else:
            
            num = num * 3 + 1
    
    print(num, end='.')

else:
    
    print('ERROR!: You have entered an invalid number')
