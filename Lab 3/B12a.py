
num = int(input('Enter a positive integer = '))

if num > 0:
    while num != 1:
        print(f"{num}, " , end = "")
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        
    print(num)
        
else:
    print('ERROR!: You have entered an invalid number')