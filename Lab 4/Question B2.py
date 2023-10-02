def main():
    
    key = True
    num_list = []
    
    while key:
        try:
            number = input("Enter number or (enter c to exit): ")
            
            if number == 'c':
                key = False
                print("Exiting.....")
                break
            
            if int(number) <= 0:
                raise ValueError
            else:
                number = float(number)
                num_list.append(number)
                
        except ValueError:
            print("Not a number or < 0. Try again")
    
    if not num_list:
        print("No number entered")
    else:
        print("Calculating.........")
        print(f"Number of element : {len(num_list)}")
        num_of_element = len(num_list)
        sub_A, sub_G, sub_H = 0, 1, 0
        for num in num_list:
            print(num)
            sub_A += num
            sub_G *= num
            sub_H += (1/num)
        
        A = sub_A / num_of_element
        G = (sub_G) ** (1 / num_of_element)
        H = num_of_element / (sub_H)
        
        print("Arithmetic mean: {:.3f}, Geometric mean: {:.3f}, {:.3f}".format(A, G, H))
        
if __name__ == "__main__":
    main()