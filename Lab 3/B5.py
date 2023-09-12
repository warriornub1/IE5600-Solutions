number_input = str(input("Enter number and position: "))
number, position = number_input.split(",")
position = int(position)
if position <= 0 :
    print("Error: Digit position must be greater than 0")
    
elif position > len(number):
    print("Error: Digit position is more than the number of digits.")
    
else:
    ''' # Easiest way
    num = number[position - 1]
    print(f"Number : {num}")
    '''
    
    temp = int(number)
    count = len(number)
    while(count is not position): # count != position
        
        temp //= 10
        
        count -= 1
    print(f"Number : {temp % 10}")