def get_number():
    
    reloop = True
    
    while reloop:
        number = input("Enter a number : ").strip()
        if len(number) == 0:
            return None
        else:
            if number.find('.') == -1:
                try:
                    return int(number)
                except ValueError:
                    print("Input a value number again")
            else:
                try:
                    return float(number)
                except ValueError:
                    print("Input a value number again")

def get_numbers():
    
    numbers = list()
    while True:
        num = get_number()
        if num == None:
            return numbers
        else:
            numbers.append(num)

def calculate_arithmetic_mean(nums):
    
    if nums == []:
        return None
    else:
        summation = 0
        for num in nums:
            
            summation += num
            
    return  summation / len(nums)


def calculate_geometric_mean(nums):
    
    product = 1
    
    if nums == []:
        return None
    else:
        for num in nums:
            
            product *= num
        
        return product ** ( 1 / len(nums) )


def calculate_geometric_mean(nums):
    
    reciprocal_summation = 0
    
    if nums == []:
        return None
    
    else:
        for num in nums:
            
            reciprocal_summation += 1 / num
        
        return len(nums) / reciprocal_summation