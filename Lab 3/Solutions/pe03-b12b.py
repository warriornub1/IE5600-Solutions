def collatzSequence(n):
    
    if n > 0:
        
        print(n, end='.') if n == 1 else print(n, end=', ')
    
        if n == 1:
            
            return
            
        else:
            
            collatzSequence(n // 2) if n % 2 == 0 else collatzSequence(n * 3 + 1)



def main():
    
    num = int(input('Enter a positive integer = '))
    
    collatzSequence(num)



if __name__ == '__main__':
    
    main()
