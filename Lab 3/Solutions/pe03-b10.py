num1 = int(input('Enter the first positive integer = '))
num2 = int(input('Enter the second positive integer = '))

if num1 > 0 and num2 > 0:

    while num1 != num2:
    
        if num1 < num2:
        
            num2 = num2 - num1
            
        else:
        
            num1 = num1 - num2
        
    print('Greatest Common Divisor is {}'.format(num1))

else:

    print('You have entered invalid numbers!')
