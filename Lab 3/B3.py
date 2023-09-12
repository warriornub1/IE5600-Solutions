number = int(input("Enter Number : "))
if number < 0 or number > 100:
    print("Error")
else:
    remainder = number % 10
    print("Remainder : {}".format(remainder))