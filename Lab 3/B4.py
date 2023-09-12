number = int(input("Enter Number : "))
if number < 0:
    print("Error")
else:
    num = number
    while(num // 10): # 2
        num //= 10 # 258 // 10 = 2
    print(f'Left most number is : {num}')