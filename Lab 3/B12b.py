
def find_Num(number):
    
    print (f"{number}, " , end = "") if number != 1 else print (f"{number}" , end = "")

    if number <= 1:
        return 1
    
    elif number % 2 == 0: #even
        number = number // 2
        return find_Num(number)
    
    else: # odd
        number = number * 3 + 1
        return find_Num(number)


def main():
    num = int(input('Enter a positive integer = '))
    
    if num > 0:
        find_Num(num)
            
    else:
        print('ERROR!: You have entered an invalid number')
    
if __name__ == '__main__':
    
    main()