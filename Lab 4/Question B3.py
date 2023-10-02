def main():
    first = str(input("Enter first string : "))
    second = str(input("Enter second string : "))
    
    first = first.split(" ")
    second = second.split(" ")
    
    main, third_list = [], []
    main = first if len(first) > len(second) else second
    
    for num in range(0, len(main)):
        
        first_word = first[num] if len(first) > num else ""
        second_word = second[num] if len(second) > num else ""
        third_list.append(first_word + second_word)
        
    print(third_list)
    
    
    
    # Alternative
    third_list = []
    bigger_main = first if len(first) > len(second) else second
    smaller_main = second if len(first) > len(second) else first
    
    for num in range(0 , len(smaller_main)):
        third_list.append(first[num] + second[num])
        
        
    third_list[len(third_list):] = bigger_main[len(smaller_main):]
    print(third_list)
if __name__ == '__main__':
    main()