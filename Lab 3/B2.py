number = int(input("Enter Number : "))
if number < 0 or number > 100:
    print("Error")
else:
    i = 1
    check_sq = False
    while(i < 10):
        check_num = i*i
        if number == check_num:
            check_sq = True
        i+= 1
    print("Perfect Square "if check_sq == True else "Not a Perfect Square")