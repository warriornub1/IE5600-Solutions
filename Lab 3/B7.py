num = int(input("Enter number : "))
if num <= 0:
    print("Error")
else:
    temp = num
    count = 2
    while(temp != count):
        
        if temp % count == 0:
            print(f"{count} x ", end = "")
            temp /= count
            count = 2
        else:
            count += 1
    print(int(temp))