

base = int(input("Enter base of Triangle (Odd number Integer, Minimum is 3 unit : "))
if base % 2 == 0 or base < 3:
    print("Error")
else:
    height = (base + 1) / 2
    print(f"You have requested a triangle with a base of {base} unit")
    print(f"This triangle a computed height of {height} unit")
    print(f"Here is your triangle")
    
    
    for n in range(1, base , 2):
        
        no_of_space = int((base - n) / 2)
        print(" " * no_of_space, end = "")
        print("*" * n)
    
