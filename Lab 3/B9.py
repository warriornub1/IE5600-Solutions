def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

base = int(input("Enter the Number of Rows Required = "))
if base < 1:
    print("Error, Enter a number >= 1")
else:
    
    print(f"You have requested a Pascal triangle of 9 rows :)")



    for n in range(0, base):
        print(' ' * int(base - n), end = '') 
        for k in range(0, n+1):
            
            print_num = 0
            print_num = int(factorial(n) / ( (factorial(k)) * factorial(n - k) ))
            print(print_num, end = " ")
        print()
        
    
